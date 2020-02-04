import unittest
from htm.injected_html import html


# noinspection PyPep8Naming
def Heading(header='Some Default', children=(), config=None):
    label = config['heading_label']
    return html('<header>{label}: Hello {header}</header>')


class TestInjector(unittest.TestCase):
    def test_single_arg(self):
        config = dict(heading_label='Some Label')
        expected = '<header>Some Label: Hello My Components</header>'
        actual = str(html("""
    <{Heading} header='My Components'><//>
""", config=config))
        self.assertEqual(expected, actual)
