# Examples of Rich Component Factories

The tests in this directory examples of doing more with components by giving people more control over the factory process.

## Passthrough

When calling a component, sometimes we have extra data we'd like to make available to the components.
In this example, we have a global ``CONFIG`` dict we'd like components to use.

This requires some modifications to ``tagged`` to collect the ``**kwargs`` and pass along, so we have a private copy of ``tagged`` and change ``htm`` to use it.
We also make a change in ``htm`` to forward along the args.

## Basic Sniffing

Components should be able to ask only for the arguments they need.

In this example we implement some (simple, naive) argument sniffing.
The inspection uses the examples from the ``htm`` docs, with a ``tag_factory`` that builds up a ``**kwargs`` from the passed-in values.

## Stateful ``html``

What if ``html`` could be a custom class, with some state, which could be used in the component?


## Later

If your component wants an argument, the factory gets it from the following, in order of precedence:
 
- Props passed in when the component was called
- The ``kwargs`` or a well-known name (e.g. ``children``) passed into the invocation of ``html()``
- Well-known names such as ``children``

