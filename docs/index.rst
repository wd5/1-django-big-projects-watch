.. django-big-projects-watch documentation master file, created by
   sphinx-quickstart on Mon Aug  6 14:08:32 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

django-big-projects-watch - Documentation
=========================================

.. warning:: This software is now powering the information system around the Berlin airport project run by
             the Pirate Party in Berlin senate (see: https://ber.piratenfraktion-berlin.de). Since we were
             really busy setting everything up, I lost a bit sight of the documentation, so this docs are
             quite outdated at the moment. I'll try to fix this in the coming weeks, though I can't promise
             anything. If you are interested in the software and have questions, please contact me on
             GitHub or Twitter (`@HolgerD77 <https://twitter.com/HolgerD77>`_).
             
             Berlin, January 18th, 2013

Django Big Projects Watch (BPW) is an **open source CMS** build with ``Python/Djano`` for the **civic oversight**
of **big publicly funded projects**, you can find the source code on 
`GitHub <https://github.com/holgerd77/django-big-projects-watch>`_.

BPW can be used by transparency activists and others to easily build and
maintain a representable project watch website for the interested public to get a better understanding
about the evolution of different parts of a project, a view of who is acting with what purposes and how
project goals changed over time. 

.. image:: images/screenshot_admin_dashboard_intro.png

Features
--------
* **Admin interface** to manage project parts, participants, project goals and events
* **Front end** presenting and connecting the project data entered in suitable way
* Basic **layout customization** via admin interface (Header color, header image, footer, contact page) 
* **Dashboard** showing most recent/important data from different parts (newest events, project parts overview, ...)
* Management of associated **documents**
* **Linking to the web** as much as possible


.. note:: Sorry, *screenshots* provided are in *german* at the moment, I hope they are useful anyway 
          and give at least an impression of the system.

.. warning:: This software is still ``pre-alpha``, so it's not quite ready for production use.
             You should be able to install and test the software without problems though.
             Await a production ready ``alpha`` version around September/October 2012.

Manual
------

.. toctree::
   :maxdepth: 2
   
   users
   developers


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

