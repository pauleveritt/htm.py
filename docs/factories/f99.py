import functools
from inspect import signature, Parameter

from factories.custom_tagged import tag
from factories.stateful_factory import html
from htm import htm_parse, htm_eval


class ComponentFactory:
    def __init__(self):
        self.config = dict(heading_label='Result')

    def __call__(self, tag_callable, **kwargs):
        sig = signature(tag_callable)
        parameters = sig.parameters

        if 'factory' in parameters:
            kwargs['factory'] = self

        # Pick through the callable's signature and get what is needed
        extra_key = "_"
        while extra_key in parameters:
            extra_key += "_"

        sig = sig.replace(
            parameters=[*parameters.values(),
                        Parameter(extra_key, Parameter.VAR_KEYWORD)
                        ]
        )
        args = dict(sig.bind(**kwargs).arguments)
        args.pop(extra_key, None)

        return tag_callable(**args)


def htm(func=None, *, cache_maxsize=128, component_factory=None):
    cached_parse = functools.lru_cache(maxsize=cache_maxsize)(htm_parse)

    # We are passed a class for the component factory. Make
    # an instance in here.
    cf = component_factory()

    def _htm(h):
        @tag
        @functools.wraps(h)
        def __htm(strings, values, **kwargs):
            kwargs['component_factory'] = cf
            ops = cached_parse(strings)
            return htm_eval(h, ops, values, **kwargs)

        return __htm

    if func is not None:
        # func is None when the decorator is "called", e.g.
        # @htm(component_factory=ComponentFactory)
        # Thus, we only get in here when it is:
        # @htm
        return _htm(func)

    # Again, when the decorator is "called", return _htm, don't invoke it
    return _htm


@htm(component_factory=ComponentFactory)
def html(tag, props, children, **kwargs):
    component_factory: ComponentFactory = kwargs['component_factory']
    if callable(tag):
        return component_factory(tag, children=children, **props, **kwargs)
    return tag, props, children


# noinspection PyPep8Naming
def Heading(factory: ComponentFactory, header='Default'):
    label = factory.config['heading_label']
    return html('<header>{label}: Hello {header}</header>')


if __name__ == '__main__':
    result = html('<{Heading} header="Component"><//>')
    print(result)
    expected = ('header', {}, ['Result', ': Hello ', 'Component'])
    assert expected == result
