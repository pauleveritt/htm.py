"""

Alternative decorator that uses hyperpython and a pluggable,
stateful factory.

"""

from hyperpython import h

from htm import htm


@htm
def html(tag, props, children, **kwargs):
    if callable(tag):
        return tag_factory(tag, children=children, **props, **kwargs)
    return h(tag, props, children)


def tag_factory(tag_callable, **kwargs):
    return tag_callable(**kwargs)
