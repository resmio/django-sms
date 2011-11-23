#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django-sms',
    version='0.0.1-alpha',
    description='An interface for django sms backends',
    author='Niels Sandholt Busch',
    author_email='niels.busch@gmail.com',
    url='https://bitbucket.org/resmio/django-sms/',
    long_description='',#open('README', 'r').read(),
    packages=[
        'sms',
        'sms.backends',
    ],
    requires=[
        'django(>=1.2)'
    ],
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)