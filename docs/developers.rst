==========
Developers
==========


Installation
============

BPW comes as a ``Django`` app providing all the data models necessary and the templates for the front end
layout. This app can be integrated in a ``Django`` project representing the concrete project to be targeted.

Requirements
------------
You need the following ``Python/Django`` libraries, probably best installed in an own ``virtualenv`` environment:

* Python 2.7+ (earlier versions untested)
* `Django <https://www.djangoproject.com/>`_ 1.4+ (earlier versions untested)
* Python Image Library PIL 1.1.7+ (for Django ImageField type)

If you want to keep track with changes in the DB model, ``South`` will be your friend:

* `South <http://south.aeracode.org/>`_ 0.7.6+ (earlier versions untested)

Installation
------------
You can install BPW with ``PIP`` like this::

	pip install -e git+https://github.com/holgerd77/django-big-projects-watch.git@master#egg=django-big-projects-watch

Create your ``Django`` project::

	django-admin.py startproject myprojectwatchblog

Configure your ``settings.py``'s basic settings for DB, ''STATIC_URL'' and ''MEDIA_URL'' (best: '/media/') and
add the following app to your ''INSTALLED_APPS'::

	INSTALLED_APPS = (
   	...
   	'big_projects_watch',
	)

Import the urls from the BPW app ``urls.py`` to your project ``urls.py`` module::

	from big_projects_watch.urls import urlpatterns 

Language Selection
------------------
At the moment BPW supports the following languages:

* English (en)
* German (de)

The language is chosen depending on the ``LANGUAGE_CODE`` param in the ``settings.py`` module, e.g.::

	LANGUAGE_CODE = 'de-de'


How to contribute: Translation
==============================

The main area for contribution for this project is translation, since the scope of the software is relatively
wide. So if you have got some time, speak English as a base language and another language like Spanish, Russian, 
French,... you are very welcome to help out (you don't need to be a developer for this task)!

You find the basic english language file called ``django.po`` on the 
`BPW GitHub Page <https://github.com/holgerd77/django-big-projects-watch>`_
in the following folder::
	
	big_projects_watch/locale/en/LC_MESSAGES/
	
Open this file and copy its contents. Then write the translation of the ``msg`` id strings between the 
double quotes after the ``msstr`` attribute. For longer strings you can use a format like this::

	#: models.py:123
	msgid "Structural parts of the project being stable over time."
	msgstr ""
	"Structural parts of the project being stable over time, e.g. 'Terminals', "
	"'Gates', 'Traffic Control', 'Integration of Public Transportation', not too "
	"much (<10), often useful as well: one entry for the project as a whole."
	
Just replace the ``msgstr`` with the translation in your language. If there is already a ``msgstr`` in 
english in the ``django.po`` file, use this string as a translation basis instead of ``msgid`` and
replace the english string with your language translation.

When you are ready with your translation open an issue on GitHub and past your text there or (advanced
developer version) make a pull request.

.. note:: If you have got limited time: please choose accuracy over speed, it's more helpful if you translate
          20 strings in an appropriate manner and take some time to think about the translation than translating
          50 strings and often missing the context or have spelling errors!


Generating/compiling message files
==================================

For generating the message files for a specific locale from the source identifiers, change to the ``big_projects_watch``
app directory and generate the message file for the desired locale with::

	django-admin.py makemessages -l de

Then translate the missing identifier strings and compile the message files with::

	django-admin.py compilemessages
 

Release Notes
=============

**Changes in version 0.1-pre-alpha** (2012-08-08)

* Initial verion

