"""
Do each as one small test file per scenario, to let the components
etc. better tell the story.

Simplest possible case: a value passed into the ``html`` function
is passed all the way along to a component.
"""
import unittest

from htm.passthrough import html

CONFIG = dict(heading_label='Result')


# noinspection PyPep8Naming
def Heading(header='Default', children=()):
    return html('<header>Hello {header}</header>')


def render():
    return str(html(
        """<{Heading} header='Component'><//>""")
    )


class TestInjector(unittest.TestCase):
    def test_pass_through(self):
        expected = '<header>Hello Component</header>'
        self.assertEqual(expected, render())
