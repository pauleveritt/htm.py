from venusian import Scanner

from factories import venusian_factory

from factories.venusian_factory import html, ComponentFactory


# noinspection PyPep8Naming
def Heading(factory: ComponentFactory, header='Default'):
    label = factory.config['heading_label']
    return html('<header>{label}: Hello {header}</header>')


# Make a Scanner to look for decorators
scanner = Scanner(component_factory=ComponentFactory())
scanner.scan(venusian_factory)

# Now render
result05 = html('<{Heading} header="Component"><//>')
