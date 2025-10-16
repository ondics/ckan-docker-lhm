###############################################################################
# Build stage
###############################################################################
ARG CKAN_VERSION_BUILD_STAGE=2.9.9-dev
ARG CKAN_VERSION_BUILD_SPATIAL=2.9.9-focal
ARG CKAN_VERSION_RUNTIME_STAGE=2.9.9-focal

FROM ckan/ckan-base:${CKAN_VERSION_BUILD_STAGE} as extbuild

USER root

# ckanext-hierarchy ###########################################################
ARG CKANEXT_HIERARCHY_VERSION="v1.2.0"
ENV CKANEXT_HIERARCHY_VERSION=${CKANEXT_HIERARCHY_VERSION}

RUN set -ex && \
    mkdir -p /wheels && \
    pip install -r https://raw.githubusercontent.com/ckan/ckanext-hierarchy/${CKANEXT_HIERARCHY_VERSION}/dev-requirements.txt

RUN set -ex && \
  pip wheel --wheel-dir=/wheels -r https://raw.githubusercontent.com/ckan/ckanext-hierarchy/${CKANEXT_HIERARCHY_VERSION}/requirements.txt && \
  pip wheel --wheel-dir=/wheels git+https://github.com/ckan/ckanext-hierarchy.git@${CKANEXT_HIERARCHY_VERSION}#egg=ckanext-hierarchy && \
  curl -o /wheels/ckanext-hierarchy.txt https://raw.githubusercontent.com/ckan/ckanext-hierarchy/${CKANEXT_HIERARCHY_VERSION}/requirements.txt && \
  ls -lah /wheels

# ckanext-grouphierarchy ######################################################
ARG CKANEXT_SDDI_VERSION="1.1.3"
ENV CKANEXT_SDDI_VERSION=${CKANEXT_SDDI_VERSION}

RUN set -ex && \
  pip wheel --wheel-dir=/wheels \
    git+https://github.com/tum-gis/ckanext-grouphierarchy-sddi.git@${CKANEXT_SDDI_VERSION}#egg=ckanext-grouphierarchy && \
  pip wheel --wheel-dir=/wheels -r \
    https://raw.githubusercontent.com/tum-gis/ckanext-grouphierarchy-sddi/${CKANEXT_SDDI_VERSION}/requirements.txt && \
  curl -o /wheels/ckanext-grouphierarchy.txt \
    https://raw.githubusercontent.com/tum-gis/ckanext-grouphierarchy-sddi/${CKANEXT_SDDI_VERSION}/requirements.txt && \
  ls -lah /wheels

# ckanext-relation ############################################################
ARG CKANEXT_RELATION_VERSION="1.0.3"
ENV CKANEXT_RELATION_VERSION=${CKANEXT_RELATION_VERSION}

RUN set -ex && \
  pip wheel --wheel-dir=/wheels \
    git+https://github.com/tum-gis/ckanext-relation-sddi.git@${CKANEXT_RELATION_VERSION}#egg=ckanext-relation && \
  pip wheel --wheel-dir=/wheels -r \
    https://raw.githubusercontent.com/tum-gis/ckanext-relation-sddi/${CKANEXT_RELATION_VERSION}/requirements.txt && \
  curl -o /wheels/ckanext-relation.txt \
    https://raw.githubusercontent.com/tum-gis/ckanext-relation-sddi/${CKANEXT_RELATION_VERSION}/requirements.txt && \
  ls -lah /wheels

# ckanext-scheming ############################################################
ARG CKANEXT_SCHEMING_VERSION="9a33dcd"
ENV CKANEXT_SCHEMING_VERSION=${CKANEXT_SCHEMING_VERSION}
ENV CKANEXT_SCHEMING_GITHUB_URL="https://github.com/ckan/ckanext-scheming"

# RUN set -ex && \
#   pip wheel --wheel-dir=/wheels \
#     git+${CKANEXT_SCHEMING_GITHUB_URL}.git@${CKANEXT_SCHEMING_VERSION}#egg=ckanext-scheming

# RUN set -ex && \
#   pip wheel --wheel-dir=/wheels \
#     git+${CKANEXT_SCHEMING_GITHUB_URL}.git#egg=ckanext-scheming

# ckanext datesearch ##########################################################
ARG CKANEXT_DATESEARCH_VERSION="1.0.2"
ENV CKANEXT_DATESEARCH_VERSION=${CKANEXT_DATESEARCH_VERSION}
ENV CKANEXT_DATESEARCH_VERSION_GITHUB_URL="https://github.com/MarijaKnezevic/ckanext-datesearch"

RUN set -ex && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_DATESEARCH_VERSION_GITHUB_URL}.git@${CKANEXT_DATESEARCH_VERSION}#egg=ckanext-datesearch

# ckanext-composite ###########################################################
ARG CKANEXT_COMPOSITE_VERSION="1e6d7bb"
ENV CKANEXT_COMPOSITE_VERSION=${CKANEXT_COMPOSITE_VERSION}
ENV CKANEXT_COMPOSITE_GITHUB_URL="https://github.com/EnviDat/ckanext-composite"

RUN set -ex && \
  pip install -r \
    https://raw.githubusercontent.com/EnviDat/ckanext-composite/${CKANEXT_COMPOSITE_VERSION}/dev-requirements.txt && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_COMPOSITE_GITHUB_URL}.git@${CKANEXT_COMPOSITE_VERSION}#egg=ckanext-composite

# ckanext-repeating ###########################################################
ARG CKANEXT_REPEATING_VERSION="1.0.0"
ENV CKANEXT_REPEATING_VERSION=${CKANEXT_REPEATING_VERSION}
ENV CKANEXT_REPEATING_GITHUB_URL="https://github.com/MarijaKnezevic/ckanext-repeating"

RUN set -ex && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_REPEATING_GITHUB_URL}.git@${CKANEXT_REPEATING_VERSION}#egg=ckanext-repeating

# ckanext-password-policy #####################################################
ARG CKANEXT_PASSWORD_POLICY_VERSION="5618dc9"
ENV CKANEXT_PASSWORD_POLICY_VERSION=${CKANEXT_PASSWORD_POLICY_VERSION}
ENV CKANEXT_PASSWORD_POLICY_GITHUB_URL="https://github.com/keitaroinc/ckanext-password-policy"

RUN set -ex && \
  pip install -r \
    https://raw.githubusercontent.com/keitaroinc/ckanext-password-policy/${CKANEXT_PASSWORD_POLICY_VERSION}/requirements.txt && \
  curl -o /wheels/ckanext-password-policy.txt \
    https://raw.githubusercontent.com/keitaroinc/ckanext-password-policy/${CKANEXT_PASSWORD_POLICY_VERSION}/requirements.txt && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_PASSWORD_POLICY_GITHUB_URL}.git@${CKANEXT_PASSWORD_POLICY_VERSION}#egg=ckanext-password-policy

# ckanext-harvest #############################################################
ARG CKANEXT_HARVEST_VERSION="v1.5.6"
ENV CKANEXT_HARVEST_VERSION=${CKANEXT_HARVEST_VERSION}
ENV CKANEXT_HARVEST_GITHUB_URL="https://github.com/ckan/ckanext-harvest"

RUN set -ex && \
  pip install -r \
    https://raw.githubusercontent.com/ckan/ckanext-harvest/${CKANEXT_HARVEST_VERSION}/dev-requirements.txt && \
  curl -o /wheels/ckanext-harvest.txt \
    https://raw.githubusercontent.com/ckan/ckanext-harvest/${CKANEXT_HARVEST_VERSION}/requirements.txt && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_HARVEST_GITHUB_URL}.git@${CKANEXT_HARVEST_VERSION}#egg=ckanext-harvest

# ckanext-geoview #############################################################
ARG CKANEXT_GEOVIEW_VERSION="v0.1.0"
ENV CKANEXT_GEOVIEW_VERSION=${CKANEXT_GEOVIEW_VERSION}
ENV CKANEXT_GEOVIEW_GITHUB_URL="https://github.com/ckan/ckanext-geoview"

RUN set -ex && \
  mkdir -p /wheels && \
  pip install -r \
    https://raw.githubusercontent.com/ckan/ckanext-geoview/${CKANEXT_GEOVIEW_VERSION}/dev-requirements.txt && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_GEOVIEW_GITHUB_URL}.git@${CKANEXT_GEOVIEW_VERSION}#egg=ckanext-geoview

# ckanext-showcase #############################################################
ARG CKANEXT_SHOWCASE_TAG="v1.6.1"
ENV CKANEXT_SHOWCASE_TAG=${CKANEXT_SHOWCASE_TAG}
ENV CKANEXT_SHOWCASE_GITHUB_URL="https://github.com/ckan/ckanext-showcase"

RUN set -ex && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_SHOWCASE_GITHUB_URL}.git@${CKANEXT_SHOWCASE_TAG}#egg=ckanext-showcase

# ckanext-pages #############################################################
ARG CKANEXT_PAGES_TAG="v0.5.2"
ENV CKANEXT_PAGES_TAG=${CKANEXT_PAGES_TAG}
ENV CKANEXT_PAGES_GITHUB_URL="https://github.com/ckan/ckanext-pages"

RUN set -ex && \
  pip wheel --wheel-dir=/wheels \
  git+${CKANEXT_PAGES_GITHUB_URL}.git@${CKANEXT_PAGES_TAG}#egg=ckanext-pages

# ckanext-dcat ################################################################
ARG CKANEXT_DCAT_VERSION="v2.3.0"
ENV CKANEXT_DCAT_VERSION=${CKANEXT_DCAT_VERSION}
ENV CKANEXT_DCAT_GITHUB_URL="https://github.com/ckan/ckanext-dcat"

RUN set -ex \
  && pip install --upgrade pip setuptools wheel \
  && pip install --upgrade --ignore-installed "packaging>=23.0" \
  && mkdir -p /wheels \
  && pip wheel --wheel-dir=/wheels \
       --extra-index-url=https://pypi.org/simple \
       -r https://raw.githubusercontent.com/ckan/ckanext-dcat/${CKANEXT_DCAT_VERSION}/dev-requirements.txt \
  && pip wheel --wheel-dir=/wheels \
       --extra-index-url=https://pypi.org/simple \
       -r https://raw.githubusercontent.com/ckan/ckanext-dcat/${CKANEXT_DCAT_VERSION}/requirements.txt \
  && curl -o /wheels/ckanext-dcat.txt \
       https://raw.githubusercontent.com/ckan/ckanext-dcat/${CKANEXT_DCAT_VERSION}/requirements.txt \
  && pip wheel --wheel-dir=/wheels \
       --extra-index-url=https://pypi.org/simple \
       git+${CKANEXT_DCAT_GITHUB_URL}.git@${CKANEXT_DCAT_VERSION}#egg=ckanext-dcat

# ckanext-dcatde ################################################################
ARG CKANEXT_DCATDE_VERSION="6.9.0"
ENV CKANEXT_DCATDE_VERSION=${CKANEXT_DCATDE_VERSION}
ENV CKANEXT_DCATDE_GITHUB_URL="https://github.com/GovDataOfficial/ckanext-dcatde"

RUN set -ex \
  && pip install --upgrade pip setuptools wheel \
  && pip install --upgrade --ignore-installed "packaging>=23.0" \
  && mkdir -p /wheels \
  && pip wheel --wheel-dir=/wheels \
       --extra-index-url=https://pypi.org/simple \
       -r https://raw.githubusercontent.com/GovDataOfficial/ckanext-dcatde/${CKANEXT_DCATDE_VERSION}/dev-requirements.txt \
  && pip wheel --wheel-dir=/wheels \
       --extra-index-url=https://pypi.org/simple \
       -r https://raw.githubusercontent.com/GovDataOfficial/ckanext-dcatde/${CKANEXT_DCATDE_VERSION}/base-requirements.txt \
  && curl -o /wheels/ckanext-dcatde.txt \
       https://raw.githubusercontent.com/GovDataOfficial/ckanext-dcatde/${CKANEXT_DCATDE_VERSION}/base-requirements.txt \
  && pip wheel --wheel-dir=/wheels \
       --extra-index-url=https://pypi.org/simple \
       git+${CKANEXT_DCATDE_GITHUB_URL}.git@${CKANEXT_DCATDE_VERSION}#egg=ckanext-dcatde

# ckanext-xloader ##########################################################
ARG CKANEXT_XLOADER_VERSION="1.0.1"
ENV CKANEXT_XLOADER_VERSION=${CKANEXT_XLOADER_VERSION}
ENV CKANEXT_XLOADER_GITHUB_URL="https://github.com/ckan/ckanext-xloader"

RUN set -ex && \
  pip install -r \
    https://raw.githubusercontent.com/ckan/ckanext-xloader/${CKANEXT_XLOADER_VERSION}/requirements.txt && \
  curl -o /wheels/ckanext-xloader.txt \
    https://raw.githubusercontent.com/ckan/ckanext-xloader/${CKANEXT_XLOADER_VERSION}/requirements.txt && \
  pip install -U requests[security] && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_XLOADER_GITHUB_URL}.git@${CKANEXT_XLOADER_VERSION}#egg=ckanext-xloader

# ckanext-ogdmunich #############################################################
# COPY ckan-extensions/ ${APP_DIR}/src
# RUN set -ex && \
#   cd ${APP_DIR}/src/ckanext-ogdmunich && \
#   pip wheel --wheel-dir=/wheels .

# ckanext-openapiview #############################################################

RUN set -ex && \
  pip wheel --wheel-dir=/wheels \
  git+https://github.com/open-data/ckanext-openapiview.git#egg=ckanext-openapiview

# ckanext-spatial #############################################################
FROM ghcr.io/keitaroinc/ckan:${CKAN_VERSION_BUILD_SPATIAL} as extbuild-spatial

ARG CKANEXT_SPATIAL_VERSION="c2118b9"
ENV CKANEXT_SPATIAL_VERSION=${CKANEXT_SPATIAL_VERSION}

USER root

# Install any system packages necessary to build extensions
RUN set -ex && \
 apt-get update && \
 apt-get install -y --no-install-recommends \
  python3-dev python3-pip libxml2-dev libxslt1-dev libgeos-c1v5 python-is-python3 && \
  mkdir -p /wheels && \
  pip install -U pip

RUN set -ex && \
  pip install -r https://raw.githubusercontent.com/MarijaKnezevic/ckanext-spatial/${CKANEXT_SPATIAL_VERSION}/requirements.txt && \
  curl -o /wheels/ckanext-spatial.txt \
    https://raw.githubusercontent.com/MarijaKnezevic/ckanext-spatial/${CKANEXT_SPATIAL_VERSION}/requirements.txt && \
  pip install -r https://raw.githubusercontent.com/MarijaKnezevic/ckanext-spatial/${CKANEXT_SPATIAL_VERSION}/requirements-postgis.txt && \
  curl -o /wheels/ckanext-spatial-postgis.txt \
    https://raw.githubusercontent.com/MarijaKnezevic/ckanext-spatial/${CKANEXT_SPATIAL_VERSION}/requirements-postgis.txt && \
    ls -lah /wheels

RUN set -ex && \
  pip wheel --wheel-dir=/wheels \
    git+https://github.com/MarijaKnezevic/ckanext-spatial.git@${CKANEXT_SPATIAL_VERSION}#egg=ckanext-spatial

## ckanext-keycloak ##########################################################
ARG CKANEXT_KEYCLOAK_VERSION="f8646f8"
ENV CKANEXT_KEYCLOAK_VERSION=${CKANEXT_KEYCLOAK_VERSION}
ENV CKANEXT_KEYCLOAK_GITHUB_URL="https://github.com/gislab-augsburg/ckanext-keycloak"

RUN set -ex && \
  pip install -r \
    https://raw.githubusercontent.com/gislab-augsburg/ckanext-keycloak/${CKANEXT_KEYCLOAK_VERSION}/requirements.txt && \
  curl -o /wheels/ckanext-keycloak.txt \
    https://raw.githubusercontent.com/gislab-augsburg/ckanext-keycloak/${CKANEXT_KEYCLOAK_VERSION}/requirements.txt && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_KEYCLOAK_GITHUB_URL}.git@${CKANEXT_KEYCLOAK_VERSION}#egg=ckanext-keycloak

# ckanext-noanonaccess ##########################################################
ARG CKANEXT_NOANONACCESS_VERSION="5b88a0f"
ENV CKANEXT_NOANONACCESS_VERSION=${CKANEXT_NOANONACCESS_VERSION}
ENV CKANEXT_NOANONACCESS_GITHUB_URL="https://github.com/gislab-augsburg/ckanext-noanonaccess"

RUN set -ex && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_NOANONACCESS_GITHUB_URL}.git@${CKANEXT_NOANONACCESS_VERSION}#egg=ckanext-noanonaccess

# ckanext-clamav ##############################################################
ARG CKANEXT_CALMAV_VERSION="c483b5d"
ENV CKANEXT_CALMAV_VERSION=${CKANEXT_CALMAV_VERSION}
ENV CKANEXT_CALMAV_GITHUB_URL="https://github.com/gislab-augsburg/ckanext-clamav"

RUN set -ex && \
  pip wheel --wheel-dir=/wheels -r \
    https://raw.githubusercontent.com/mutantsan/ckanext-clamav/${CKANEXT_CALMAV_VERSION}/requirements.txt && \
  curl -o /wheels/ckanext-clamav.txt \
    https://raw.githubusercontent.com/mutantsan/ckanext-clamav/${CKANEXT_CALMAV_VERSION}/requirements.txt && \
  pip wheel --wheel-dir=/wheels \
    git+${CKANEXT_CALMAV_GITHUB_URL}.git@${CKANEXT_CALMAV_VERSION}#egg=ckanext-clamav
    
###############################################################################
# Runtime stage
###############################################################################
FROM ghcr.io/keitaroinc/ckan:${CKAN_VERSION_RUNTIME_STAGE} as runtime

ENV CKAN__PLUGINS "image_view text_view recline_view recline_map_view recline_graph_view recline_grid_view \
  webpage_view openapi_view datastore xloader ogdmunich pages showcase resource_proxy geo_view geojson_view wmts_view shp_view \
  harvest ckan_harvester csw_harvester dcat dcatde \
  dcat_rdf_harvester dcat_json_harvester dcat_json_interface structured_data \
  spatial_metadata spatial_query scheming_datasets keycloak noanonaccess clamav envvars"

# Extra env for compatibility with ckan/base Docker images for downstream k8s
ENV CKAN_INI=${APP_DIR}/production.ini
ENV CKAN_STORAGE_PATH=/var/lib/ckan
# ENV CKAN_STORAGE_PATH=/srv/app/data
ENV TZ="UTC"

USER root

# Install any system packages necessary to build extensions
RUN set -ex && \
  apt-get update && \
  apt-get install -y --no-install-recommends \
    libxml2-dev libxslt1-dev libgeos-c1v5 && \
    pip install --no-cache-dir -U pip && \
    rm -rf /var/lib/apt/lists/*

# Copy python wheels from build stage
COPY --from=extbuild /wheels ${APP_DIR}/ext_wheels
COPY --from=extbuild-spatial /wheels ${APP_DIR}/ext_wheels

# ckanext-hierarchy ###########################################################
RUN set -ex && \
  pip install --find-links=${APP_DIR}/ext_wheels -r ${APP_DIR}/ext_wheels/ckanext-hierarchy.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-hierarchy

# ckanext-grouphierarchy ######################################################
RUN set -ex && \
  pip install --find-links=${APP_DIR}/ext_wheels -r ${APP_DIR}/ext_wheels/ckanext-grouphierarchy.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-grouphierarchy

# ckanext-relation ############################################################
RUN set -ex && \
  pip install --find-links=${APP_DIR}/ext_wheels -r ${APP_DIR}/ext_wheels/ckanext-relation.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-relation

# ckanext-spatial #############################################################
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-spatial.txt && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-spatial-postgis.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-spatial

# ckanext-scheming ############################################################
# RUN set -ex && \
#   pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-scheming

RUN set -ex && \
  pip install -e git+https://github.com/ckan/ckanext-scheming.git#egg=ckanext-scheming

# ckanext-datesearch ##########################################################
RUN set -ex && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-datesearch

# ckanext-composite ###########################################################
RUN set -ex && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-composite

# ckanext-repeating ###########################################################
RUN set -ex && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-repeating

# ckanext-password-policy #####################################################
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-password-policy.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-password-policy

# ckanext-harvest ################################################################
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-harvest.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-harvest

# ckanext-geoview #############################################################
RUN set -ex && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-geoview

# ckanext-showcase #############################################################
RUN set -ex && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-showcase

# ckanext-pages #############################################################
RUN set -ex && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-pages

# ckanext-dcat ################################################################
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-dcat.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-dcat

# ckanext-dcatde ################################################################
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-dcatde.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-dcatde

# ckanext-xloader #############################################################
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-xloader.txt && \
  pip install -U requests[security] && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-xloader

# ckanext-ogdmunich #############################################################
# RUN set -ex && \
#   pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-ogdmunich

COPY ckan-extensions/ ${APP_DIR}/src
RUN set -ex && \
  cd ${APP_DIR}/src/ckanext-ogdmunich && \
  pip install -e .

# ckanext-openapiview #############################################################
RUN set -ex && \
  pip install -e git+https://github.com/open-data/ckanext-openapiview.git#egg=ckanext-openapiview

# Copy additional files
COPY --chown=ckan:ckan who.ini ${APP_DIR}/who.ini

## ckanext-keycloak #################################################################
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-keycloak.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-keycloak

# ckanext-noanonaccess #############################################################
RUN set -ex && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-noanonaccess

# ckanext-clamav ##############################################################
# uninstall previous version from sddi-base
RUN yes | pip uninstall ckanext-clamav
RUN set -ex && \
  pip install -r ${APP_DIR}/ext_wheels/ckanext-clamav.txt && \
  pip install --no-index --find-links=${APP_DIR}/ext_wheels ckanext-clamav

# install supervisor ########################################################
RUN set -ex && \
  apt-get update && \
  apt-get -y install supervisor
COPY supervisor/supervisor-ckan-worker.conf /etc/supervisor/conf.d
COPY supervisor/supervisord.conf /etc/supervisor
COPY supervisor/start-supervisor.sh /srv/app/docker-afterinit.d

RUN set -ex && \
  ckan config-tool "${CKAN_INI}" "ckan.plugins = ${CKAN__PLUGINS}" && \
  ckan config-tool "${CKAN_INI}" "ckan.spatial.srid = 4326" && \
  ckan config-tool "${CKAN_INI}" "ckanext.spatial.search_backend = solr-bbox" && \
  ckan config-tool "${CKAN_INI}" "scheming.dataset_schemas = ckanext.ogdmunich:ckan_dataset.yaml" && \
  ckan config-tool "${CKAN_INI}" "scheming.presets = ckanext.scheming:presets.json" && \
  ckan config-tool "${CKAN_INI}" "scheming.dataset_fallback = false" && \
  # ckan config-tool "${CKAN_INI}" "licenses_group_url = https://raw.githubusercontent.com/tum-gis/ckanext-grouphierarchy-sddi/main/ckanext/grouphierarchy/licenses_SDDI.json" && \
  ckan config-tool "${CKAN_INI}" "licenses_group_url = file:///srv/app/src/ckanext-ogdmunich/ckanext/ogdmunich/resources/licenses-old.json" && \
  ckan config-tool "${CKAN_INI}" "ckanext.password_policy.password_length = 12" && \
  ckan config-tool "${CKAN_INI}" "ckanext.password_policy.failed_logins = 3" && \
  ckan config-tool "${CKAN_INI}" "ckanext.password_policy.user_locked_time = 600" && \
  ckan config-tool "${CKAN_INI}" "ckanext.pages.about_menu = false" && \
  ckan config-tool "${CKAN_INI}" "ckanext.pages.allow_html = true" && \
  ckan config-tool "${CKAN_INI}" "ckanext.pages.editor = ckeditor" && \
  ckan config-tool "${CKAN_INI}" "ckanext.dcat.rdf.profiles = dcatap_de" && \
  ckan config-tool "${CKAN_INI}" "ckan.harvest.mq.type = redis" && \
  ckan config-tool "${CKAN_INI}" "ckan.harvest.mq.hostname = 127.0.0.1" && \
  ckan config-tool "${CKAN_INI}" "ckan.harvest.mq.port=6379" && \
  ckan config-tool "${CKAN_INI}" "ckan.harvest.mq.redis_db=0" && \
  ckan config-tool "${CKAN_INI}" "ckan.harvest.log_timeframe = 10" && \
  ckan config-tool "${CKAN_INI}" "ckanext.spatial.harvest.user_name = fwadm" && \
  ckan config-tool "${CKAN_INI}" "ckanext.spatial.harvest.continue_on_validation_errors = True" && \
  ckan config-tool "${CKAN_INI}" "ckanext.geoview.ol_viewer.formats = wms kml" && \
  ckan config-tool "${CKAN_INI}" "ckanext.geoview.shp_viewer.srid = 4326" && \
  ckan config-tool "${CKAN_INI}" "ckanext.geoview.shp_viewer.encoding = UTF-8" && \
  ckan config-tool "${CKAN_INI}" "ckanext.spatial.common_map.type = custom" && \
  ckan config-tool "${CKAN_INI}" "ckanext.spatial.common_map.custom.url = https://tile.openstreetmap.org/{z}/{x}/{y}.png" && \
  ckan config-tool "${CKAN_INI}" "ckanext.spatial.common_map.attribution = Map tiles by <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors" && \
  # ckan config-tool "${CKAN_INI}" "ckanext.spatial.common_map.type = wms" && \
  ckan config-tool "${CKAN_INI}" "ckanext.spatial.common_map.wms.url = https://geoportal.muenchen.de/geoserver/gsm/wms" && \
  ckan config-tool "${CKAN_INI}" "ckanext.spatial.common_map.wms.layer = gsm:g_stadtkarte_gesamt" && \
  ckan config-tool "${CKAN_INI}" "ckanext.spatial.common_map.wms.srs = EPSG:25832" && \
  ckan config-tool "${CKAN_INI}" "ckanext.spatial.common_map.wms.attribution = © <a href="https://www.geodatenservice-muenchen.de">Kommunalreferat – GeodatenService</a>, <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>" && \
  echo "${TZ}" > /etc/timezone && \
  mkdir -p ${CKAN_STORAGE_PATH} && \
  chown -R ckan:ckan ${APP_DIR} ${CKAN_STORAGE_PATH} && \
  # Remove wheels
  rm -rf ${APP_DIR}/ext_wheels
# Set timezone
ENV TZ="Europe/Berlin"
RUN echo "${TZ}" > /etc/timezone

USER ckan
