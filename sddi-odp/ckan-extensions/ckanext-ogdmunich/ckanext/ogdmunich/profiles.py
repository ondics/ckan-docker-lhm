import json
import os
import logging

import ckan.plugins.toolkit as toolkit

from rdflib.namespace import Namespace, RDF
from ckanext.dcat.profiles import RDFProfile, CleanedURIRef
from ckanext.dcatde.profiles import DCATdeProfile
from ckanext.dcat.utils import resource_uri
from rdflib import Literal, URIRef

import pycountry

# Namespaces von dcat und dcatde Extension kopiert
DCAT = Namespace("http://www.w3.org/ns/dcat#")
DCT = Namespace('http://purl.org/dc/terms/')
DCATDE = Namespace("http://dcat-ap.de/def/dcatde/")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
DCAT_LANGUAGE_PREFIX = "http://publications.europa.eu/resource/authority/language/"


class OGDMunichDCATProfile(DCATdeProfile):

    def __init__(self, graph, dataset_type="dataset", compatibility_mode=False):
        dir_path = os.path.join(os.path.dirname(__file__), "resources")
        mapping_file = os.path.join(dir_path, "dcat_format_mapping.json")

        if os.path.isfile(mapping_file):
            with open(mapping_file, encoding="utf-8") as json_data:
                self.format_mapping = json.load(json_data)

        super().__init__(graph, dataset_type, compatibility_mode)
    
    
    def parse_dataset(self, dataset_dict, dataset_ref):
        """ Transforms DCAT-AP.de-Data to CKAN-Dictionary """

        # call super method
        super(OGDMunichDCATProfile, self).parse_dataset(dataset_dict, dataset_ref)

    def graph_from_dataset(self, dataset_dict, dataset_ref):
        """ Transforms CKAN-Dictionary to DCAT-AP.de-Data """

        # call super method
        super(OGDMunichDCATProfile, self).graph_from_dataset(
            dataset_dict, dataset_ref
        )

        g = self.g
        log = logging.getLogger(__name__)
        
        # format Code  von https://github.com/rostock/ckanext-hro_dcatapde/blob/master/ckanext/hro_dcatapde/profile.py
        for resource_dict in dataset_dict.get('resources', []):
            for distribution in g.objects(dataset_ref, DCAT.distribution):
                if str(distribution) == resource_uri(resource_dict):
                    for format_string in g.objects(distribution, DCT['format']):
                        if self.format_mapping.get(str(format_string).upper()):
                            dcatformat = self.format_mapping[str(format_string).upper()]['format']
                            if dcatformat is not None:
                                g.remove((distribution, DCT['format'], None))
                                g.add((distribution, DCT['format'], URIRef(dcatformat)))
                            dcatmediatype = self.format_mapping[str(format_string).upper()]['media_type']
                            if dcatmediatype is not None:
                                g.remove((distribution, DCAT['mediaType'], None))
                                g.add((distribution, DCAT['mediaType'], URIRef(dcatmediatype)))

    def graph_from_catalog(self, catalog_dict, catalog_ref):
        """ Creates a Catalog representation """

        log = logging.getLogger(__name__)
        g = self.g

        # call super method
        super(OGDMunichDCATProfile, self).graph_from_catalog(
            catalog_dict, catalog_ref
        )

        # Katalog Sprache (dct:language)
        locale = toolkit.config.get("ckan.locale_default", "de")
        try:
            if locale and not locale.startswith(DCAT_LANGUAGE_PREFIX):
                language = pycountry.languages.get(alpha_2=locale)
                language_uri = DCAT_LANGUAGE_PREFIX + language.alpha_3.upper()
                g.remove((catalog_ref, DCT.language, None))
                g.add((catalog_ref, DCT.language, URIRef(language_uri)))
        except (KeyError, AttributeError):
            log.error('INVALID: ' + 'Catalog Language' + ': ' + language_uri)
        
        # Katalog Herausgeber (dct:publisher)
        publisher_uri = toolkit.config.get("ckanext.ogdmunich_publisher_uri", "https://opendata.muenchen.de/pages/portal")
        publisher_name = toolkit.config.get("ckanext.ogdmunich_publisher_name", "Landeshauptstadt München")
        g.add((catalog_ref, DCT.publisher, URIRef(publisher_uri)))
        g.add((URIRef(publisher_uri), RDF.type, FOAF.Organization))
        g.add((URIRef(publisher_uri), FOAF.name, Literal(publisher_name)))