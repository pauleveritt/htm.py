"""

Pass kwargs from calling ``html()`` all the way through to the component.

"""
from inspect import Parameter, signature

from hyperpython import h

from .custom_htm import htm


@htm
def html(tag, props, children, **kwargs):
    if callable(tag):
        return tag_factory(tag, children=children, **props, **kwargs)
    return h(tag, props, children)


def tag_factory(tag_callable, **kwargs):
    sig = signature(tag_callable)
    parameters = sig.parameters

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
