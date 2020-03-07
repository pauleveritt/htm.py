=========
Factories
=========

Let's look at some alternate ways to find component factories and get arguments into them.

Passthrough
===========

We call an html string through a custom function which we pass the template string.
What if we want to pass some extra state as keyword arguments, which are then used in a component in the template?

We need a way to get those keywords passed through the layers, into the component factory.

.. literalinclude:: f01.py

.. invisible-code-block: python

  from f01 import result01

Simplest possible case: a value passed into the ``html`` function is passed all the way along to a component.

>>> result01
('header', {}, ['Hello ', 'Component'])

Basic Sniffing
==============

Similar, but we sniff at the arguments the component wants,
then pass them in, rather than passing in the universe.

Also, the ``Heading`` signature doesn't need to set default for
``children``. The component doesn't need it, doesn't ask for it,
so doesn't get it. Also, ``config`` isn't a kw arg any more. It's
required.

.. literalinclude:: f02.py

.. invisible-code-block: python

  from f02 import result02

>>> result02
('header', {}, ['Result', ': Hello ', 'Component'])


Stateful Tag Factory
====================

We don't particularly want global state available in a component.
Instead, we want application state:

- Stuff computed at startup (e.g. reading a config file)

- A configured callable which might get stuff from a database

- Values that appear during the rendering of a string (and then the renderings of components and subcomponents further down)

We want a *stateful* factory.
At the moment, our custom ``htm`` function just hardcodes a ``tag_factory`` callable.
Instead, we want our ``htm`` function to be *passed* a custom, stateful callable that can reach other parts of the system.

This is kind of tricky to arrange.

First, we'll pass this callable instance into the rendering, similar to above.

.. literalinclude:: f03.py

.. invisible-code-block: python

  from f03 import result03

>>> result03
('header', {}, ['Result', ': Hello ', 'Component'])

This, though, is a drag: we have to pass the instance in every time we use it, but worse, our ``Heading`` component also had to pass it along when returning ``html()``.

