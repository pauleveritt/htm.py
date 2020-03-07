from factories.passthrough import html


# noinspection PyPep8Naming
def Heading(header='Default', children=()):
    return html('<header>Hello {header}</header>')


result01 = html('<{Heading} header="Component"><//>')
