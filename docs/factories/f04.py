from factories.stateful_factory import html, ComponentFactory


# noinspection PyPep8Naming
def Heading(factory: ComponentFactory, header='Default'):
    label = factory.config['heading_label']
    return html('<header>{label}: Hello {header}</header>')


result04 = html('<{Heading} header="Component"><//>')
