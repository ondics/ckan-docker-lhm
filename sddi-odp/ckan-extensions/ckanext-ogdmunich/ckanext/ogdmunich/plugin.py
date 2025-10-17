# -*- coding: utf-8 -*- 

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging
from ckan.lib.helpers import json
import ckan.lib.navl.dictization_functions as df
from ckanext.spatial.interfaces import ISpatialHarvester
import json
from ckan.logic import NotFound, get_action
from ckan import model
from ckan.model import Session
from ckanext.ogdmunich import dcat_ap

import json
import os

Invalid = df.Invalid
log = logging.getLogger(__name__)

# Helper functions

def get_dcat_format(ckan_format):
    '''Return CKAN resource field format for DCAT'''
    dir_path = os.path.join(os.path.dirname(__file__), "resources")
    mapping_file = os.path.join(dir_path, "dcat_format_mapping.json")
    dcat_format = None

    if os.path.isfile(mapping_file):
        with open(mapping_file, encoding="utf-8") as json_data:
            format_mapping = json.load(json_data)
        if format_mapping.get(str(ckan_format).upper()):
            dcat_format = format_mapping[str(ckan_format).upper()]['format']
    return dcat_format

def package_tracking(package_id):
    mypackage = toolkit.get_action('package_show')(data_dict={'id': package_id, 'include_tracking': True})
    return mypackage['tracking_summary']['total']


def most_popular_groups():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    groups = toolkit.get_action('group_list')(
        data_dict={'sort': 'package_count desc', 'all_fields': True})

    # Truncate the list to the 11 most popular groups only.
    groups = groups[:11]
    groupsWithPackages = []
    for grp in groups:
        if grp['package_count'] and grp['package_count'] >0:
            groupsWithPackages.append(grp)

    return groupsWithPackages

def hvd_category_list(field):
    skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))
    os.chdir(skript_verzeichnis)
    hvd_list_path = os.path.join('resources', 'hvd_categories.json')
    with open(hvd_list_path, 'r') as f:
        hvd_list = json.load(f)
    return hvd_list

def frequency_list(field):
    skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))
    os.chdir(skript_verzeichnis)
    frequency_list_path = os.path.join('resources', 'frequency.json')
    with open(frequency_list_path, 'r') as f:
        frequency_list = json.load(f)
    return frequency_list

# Validator functions

def is_musterdatensatz(value: str):
    if not value:
        return
    prefix = "https://musterdatenkatalog.de/def/musterdatensatz/"
    if value.startswith(prefix):
        return value
    else:
        raise Invalid(f'{value} ist keine gültige URI für den Musterdatenkatalog.\nMuss mit `https://musterdatenkatalog.de/def/musterdatensatz/` beginnen')

class OGDMunichThemePlugin(plugins.SingletonPlugin):
    '''Theme plugin for OGD Munich.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(ISpatialHarvester, inherit=True)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IValidators)

    def get_blueprint(self):
        return dcat_ap.get_blueprints()

    def get_validators(self):
        return {"ogdmunich_is_musterdatensatz": is_musterdatensatz}

    def get_package_dict(self, context, data_dict):
        # Check the reference below to see all that's included on data_dict
        package_dict = data_dict['package_dict']
        iso_values = data_dict['iso_values']
    
    #log.warning(data_dict)

        def _get_extra(package_dict, key):
            for extra in package_dict.get('extras', []):
                if extra['key'] == key:
                    return extra['value']

        package_dict['extras'].append(
            {'key' : 'topic-category', 'value': iso_values.get('topic-category')}
        )
        package_dict['extras'].append(
            {'key': 'geographical_granularity', 'value': 'stadt'}
        )
        responsibleparty = _get_extra(package_dict, 'responsible-party')
        responsibleparty = responsibleparty[1:-1] #remove first and last character to decode json to array
        responsiblepartyDecoded = json.loads(responsibleparty)
    
        isPointOfContact = False
        for key, value in responsiblepartyDecoded.items():
            if key == 'roles':
                rolesList = value
                if 'pointOfContact' in rolesList:
                    isPointOfContact = True

        maintainer = 'n.a'
        if isPointOfContact and 'name' in responsiblepartyDecoded:
            maintainer = responsiblepartyDecoded['name']

        package_dict['maintainer'] = maintainer
        package_dict['maintainer_email'] = iso_values.get('contact-email')
        package_dict['author_email'] = iso_values.get('contact-email')

        url = 'https://geogdi.muenchen.de/portal/master/?uuid='
        package_dict['url'] = url + _get_extra(package_dict, 'guid')
        package_dict['extras'].append(
            {'key' : 'dates', 'value': _get_extra(package_dict, 'dataset-reference-date')}
        )

        #set format default value for resouorces
        for resource in package_dict.get('resources', []):
            if not resource.get('format'):
                resource['format'] = 'WMS'

        groups = self.handle_groups(iso_values)
        if groups:
            package_dict['groups'] = groups

        package_dict['license_id'] = self.handle_license(_get_extra(package_dict, 'access_constraints'))

        # owner_org = self.handle_organisation(maintainer)
        # if owner_org:
        # 	package_dict['owner_org'] = owner_org
        return package_dict

    def handle_groups(self, iso_values):
        cats = iso_values['topic-category']
        validated_groups = []
        context = {'model': model, 'session': Session, 'user': 'harvest'}
        for cat in cats:
            groupname = self.get_group_by_gdi(cat)		
            if groupname:
                    try:
                            data_dict = {'id': groupname}
                            get_action('group_show')(context, data_dict)
                            validated_groups.append({'name': groupname})
                    except NotFound as e:
                            print("group not found!")
                            log.warning('Group %s from category %s is not available' % (groupname, groupname))

        return validated_groups

    def get_group_by_gdi(self, groupValueGDI):
        print("value from gdi %s " % groupValueGDI)
        if groupValueGDI == 'transport_verkehr':
            return 'transport-verkehr'
        elif groupValueGDI == 'umwelt_klima' or groupValueGDI=='environment':
            return 'umwelt-klima'
        else:
            return ''

    def handle_license(self, values):
        licenseId = 'dl-de-by-2.0'
        if values and len(values) > 2:
            values = values[1:-1]
            context = {'model': model, 'session': model.Session, 'user': 'harvest'}
            license_list = get_action('license_list')(context, {})
            values = values.replace("\\", "")
            for license in license_list:
                searchString = '\"id\": \"' + license.get('id')+ '\"'
                if searchString in values:
                    licenseId =  license.get('id')
        return licenseId	

    def handle_organisation(self, orgNameGDI):
        org_name = 'landeshauptstadt-muenchen'
        orgNameGDI = orgNameGDI.encode('utf-8')
        if orgNameGDI == 'Landeshauptstadt München - Kommunalreferat':
            org_name = 'landeshauptstadt-muenchen-kommunalreferat'
        elif orgNameGDI == 'Landeshauptstadt München -  Kommunalreferat - GeodatenService München':
            org_name = 'landeshauptstadt-muenchen-kommunalreferat-geodatenservice-muenchen'
        elif orgNameGDI == 'Landeshauptstadt München - Baureferat':
            org_name = 'landeshauptstadt-muenchen-baureferat'
        elif orgNameGDI == 'Landeshauptstadt München - Direktorium':
            org_name= 'landeshauptstadt-muenchen-direktorium'
        elif orgNameGDI == 'Landeshauptstadt München - Kreisverwaltungsreferat':
            org_name = 'landeshauptstadt-muenchen-kreisverwaltungsreferat'
        elif orgNameGDI == 'Landeshauptstadt München - Kulturreferat':
            org_name = 'landeshauptstadt-muenchen-kulturreferat'
        elif orgNameGDI == 'Landeshauptstadt München - Personal- und Organisationsreferat':
            org_name = 'landeshauptstadt-muenchen-personal-und-organisationsreferat'
        elif orgNameGDI == 'Landeshauptstadt München - Referat für Arbeit und Wirtschaft':
            org_name = 'landeshauptstadt-muenchen-referat-fuer-arbeit-und-wirtschaft'
        elif orgNameGDI == 'Landeshauptstadt München - Referat für Bildung und Sport':
            org_name = 'landeshauptstadt-muenchen-referat-fuer-bildung-und-sport'
        elif orgNameGDI == 'Landeshauptstadt München - Referat für Gesundheit und Umwelt':
            org_name = 'landeshauptstadt-muenchen-referat-fuer-gesundheit-und-umwelt'
        elif orgNameGDI == 'Landeshauptstadt München - Referat für Informations- und Telekommunikationstechnik':
            org_name = 'landeshauptstadt-muenchen-referat-fuer-informations-und-telekommunikationstechnik'
        elif orgNameGDI == 'Landeshauptstadt München - Referat für Stadtplanung und Bauordnung':
            org_name = 'landeshauptstadt-muenchen-referat-fuer-stadtplanung-und-bauordnung'
        elif orgNameGDI == 'Landeshauptstadt München - Stadtkämmerei':
            org_name = 'landeshauptstadt-muenchen-stadtkaemmerei'
        elif orgNameGDI == 'Landeshauptstadt München - Sozialreferat':
            org_name = 'landeshauptstadt-muenchen-sozialreferat'
        elif orgNameGDI == 'Landeshauptstadt München -  Direktorium - Statistisches Amt':
            org_name = 'landeshauptstadt-muenchen-direktorium-statistisches-amt'
        else:
            org_name = 'landeshauptstadt-muenchen'
        org_dict = get_action('organization_show')({}, {'id': org_name})
        return org_dict['id']

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('assets', 'ogdmunich_assets')

    def get_helpers(self):
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'ogdmunich_most_popular_groups': most_popular_groups,  'ogdmunich_package_tracking':package_tracking,
                'ogdmunich_hvd_category_list': hvd_category_list,
                'ogdmunich_frequency_list': frequency_list,
                'ogdmunich_get_dcat_format': get_dcat_format}
