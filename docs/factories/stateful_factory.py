"""

Pass kwargs from calling ``html()`` all the way through to the component.

"""
from inspect import Parameter, signature

from .stateful_htm import htm


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


@htm(component_factory=ComponentFactory)
def html(tag, props, children, **kwargs):
    component_factory: ComponentFactory = kwargs['component_factory']
    if callable(tag):
        return component_factory(tag, children=children, **props, **kwargs)
    return tag, props, children
