from inspect import Parameter, signature

from factories.custom_factory import html


class ComponentFactory:
    def __init__(self):
        self.config = dict(heading_label='Result')

    def __call__(self, tag_callable, **kwargs):
        sig = signature(tag_callable)
        parameters = sig.parameters

        # Pick through the callable's signature and get what is needed
        extra_key = "_"
        while extra_key in parameters:
            extra_key += "_"

        sig = sig.replace(
            parameters=[*parameters.values(),
                        Parameter(extra_key, Parameter.VAR_KEYWORD)
                        ]
        )
        args = dict(sig.bind(**kwargs).arguments)
        args.pop(extra_key, None)

        return tag_callable(**args)


# noinspection PyPep8Naming
def Heading(tag_factory: ComponentFactory, header='Default'):
    config = tag_factory.config
    label = config['heading_label']
    return html('<header>{label}: Hello {header}</header>', tag_factory=tag_factory)


result03 = html('<{Heading} header="Component"><//>', tag_factory=ComponentFactory())
