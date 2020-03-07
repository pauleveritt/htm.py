from factories.basic_sniffing import html

CONFIG = dict(heading_label='Result')


# noinspection PyPep8Naming
def Heading(config, header='Default'):
    label = config['heading_label']
    return html('<header>{label}: Hello {header}</header>')


result02 = str(html('<{Heading} header="Component"><//>', config=CONFIG))
