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


Custom Tag Factory
==================

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

The solution: state in the ``@htm`` decorator.

Stateful Decorator
==================

We currently call an ``html()`` function, passing a template string with components, and getting a VDOM.
This ``html()``  function, which we write, is wrapped by the ``@htm`` decorator, which does the magic of tagged strings, calling, caching, etc.

What if ``@htm`` was actually a stateful decorator?
Meaning, it kept an instance of a passed-in class, which was then used to construct components.
In this case, components could ask for arguments and the data would come from the instance.

.. literalinclude:: f04.py

.. invisible-code-block: python

  from f04 import result04

>>> result04
('header', {}, ['Result', ': Hello ', 'Component'])

This solution works well for templating in components, as these are constructed under our control.
It doesn't work for the variables in the template string itself.
Those values come from the stack, as picked apart in ``tagged``.

Scanning for Decorators
=======================

This solution has a drawback: once the factory is instantiated, it's there forever.
While not module scope, it's something that is hard to clean out, for example in tests.

.. literalinclude:: f05.py

.. invisible-code-block: python

  from f05 import result05

>>> result05
('header', {}, ['Result', ': Hello ', 'Component'])
