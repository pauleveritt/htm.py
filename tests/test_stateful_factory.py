"""
Do each as one small test file per scenario, to let the components
etc. better tell the story.

Change ``html()`` to be a custom, stateful factory, with data that can
be used by components.

"""
import unittest

from htm.stateful_factory import html

CONFIG = dict(heading_label='Result')


def Heading(config, header='Default'):
    label = config['heading_label']
    return html('<header>{label}: Hello {header}</header>')


class TestStatefulFactory(unittest.TestCase):

    def test_stateful_factory(self):
        expected = '<header>Result: Hello Component</header>'
        actual = html("""<{Heading} header='Component'><//>""",
                      config=CONFIG)

        # self.assertEqual(expected, str(actual))
