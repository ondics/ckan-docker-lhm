from setuptools import setup, find_packages
import sys, os

version = '1.4.0'

setup(
    name='ckanext-ogdmunich',
    version=version,
    description="Extension for OGD Munich",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='solvistas GmbH',
    author_email='opendata-support@solvistas.com',
    url='www.solvistas.com',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.ogdmunich'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
	    ogdmunich=ckanext.ogdmunich.plugin:OGDMunichThemePlugin

        [ckan.rdf.profiles]
        ogdmunich_dcat=ckanext.ogdmunich.profiles:OGDMunichDCATProfile
    ''',
)
