"""

Stateful ``html`` factory.

"""
import functools
from inspect import Parameter, signature

from hyperpython import h

from htm import htm_parse, tag, htm_eval


class Htm:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        cache_maxsize = 128
        cached_parse = functools.lru_cache(maxsize=cache_maxsize)(htm_parse)

        def _htm(h1):
            @tag
            @functools.wraps(h1)
            def __htm(strings, values, **kwargs):
                ops = cached_parse(strings)
                return htm_eval(h1, ops, values, **kwargs)

            return __htm

        if self.func is not None:
            return _htm(self.func)
        return _htm


def htm(func=None, *, cache_maxsize=128):
    cached_parse = functools.lru_cache(maxsize=cache_maxsize)(htm_parse)

    def _htm(h):
        @tag
        @functools.wraps(h)
        def __htm(strings, values, **kwargs):
            ops = cached_parse(strings)
            return htm_eval(h, ops, values, **kwargs)

        return __htm

    if func is not None:
        return _htm(func)
    return _htm


@Htm
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
