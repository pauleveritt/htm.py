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


Stateful Factory
================

