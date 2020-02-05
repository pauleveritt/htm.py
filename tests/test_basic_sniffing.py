"""
Do each as one small test file per scenario, to let the components
etc. better tell the story.

Similar, but we sniff at the arguments the component wants,
then pass them in, rather than passing in the universe.

Also, the ``Heading`` signature doesn't need to set default for
``children``. The component doesn't need it, doesn't ask for it,
so doesn't get it. Also, ``config`` isn't a kw arg any more. It's
required.

"""
import unittest

from htm.basic_sniffing import html

CONFIG = dict(heading_label='Result')


def Heading(config, header='Default'):
    label = config['heading_label']
    return html('<header>{label}: Hello {header}</header>')


class TestBasicSniffing(unittest.TestCase):

    def test_basic_sniffing(self):
        expected = '<header>Result: Hello Component</header>'
        actual = html("""<{Heading} header='Component'><//>""",
                      config=CONFIG)

        self.assertEqual(expected, str(actual))
