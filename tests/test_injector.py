import unittest
from htm.injected_html import html


# noinspection PyPep8Naming
def Heading(header='Some Default', children=()):
    return html('<header>Hello {header}</header>')


class TestInjector(unittest.TestCase):
    def test_single_arg(self):
        expected = '<header>Hello My Components</header>'
        actual = str(html("""
    <{Heading} header='My Components'><//>
"""))
        self.assertEqual(expected, actual)
