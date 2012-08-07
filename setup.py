from setuptools import setup

import os

setup(
    name='django-big-projects-watch',
    version='0.1',
    description='Open source CMS supporting the civic oversight of big public projects',
    author='Holger Drewes',
    author_email='Holger.Drewes@googlemail.com',
    url='https://github.com/holgerd77/django-big-projects-watch',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    packages=[
        'big_projects_watch',
    ],
    #install_requires=[
        #'Django>=1.2',
        #'Scrapy>=0.14',
        # Scheduling
        #'django-kombu',
        #'django-celery',
    #],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
