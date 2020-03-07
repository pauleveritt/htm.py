"""

Pass kwargs from calling ``html()`` all the way through to the component.

"""

from .custom_htm import htm


@htm
def html(tag, props, children, **kwargs):
    tag_factory = kwargs['tag_factory']
    if callable(tag):
        return tag_factory(tag, children=children, **props, **kwargs)
    return tag, props, children
