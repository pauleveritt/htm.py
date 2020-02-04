import unittest
from htm.passthrough import html

expected = '<header>Some Label: Hello My Components</header>'


class TestInjector(unittest.TestCase):
    def test_passthrough(self):
        """
Simplest possible case: a value passed into the ``html`` function
is passed all the way along to a component.

        """
        # noinspection PyPep8Naming
        def Heading(header='Some Default', children=(), config=None):
            label = config['heading_label']
            return html('<header>{label}: Hello {header}</header>')

        config = dict(heading_label='Some Label')

        actual = str(html("""
    <{Heading} header='My Components'><//>
""", config=config))

        self.assertEqual(expected, actual)
