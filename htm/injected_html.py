"""

Alternative decorator that uses hyperpython and a pluggable,
stateful factory.

"""

from hyperpython import h

from htm import htm


@htm
def html(tag, props, children):
    if callable(tag):
        return tag_factory(tag, children=children, **props)
    return h(tag, props, children)


def tag_factory(tag_callable, **kwargs):
    return tag_callable(**kwargs)
