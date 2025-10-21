CKAN SDDI-ODP
=========

In diesem Repo wurde das Image [sddi-base](https://github.com/it-at-m/ckan-docker/pkgs/container/ckan-sddi-base) als Vorlage verwendet und an die Anforderungen/Extensions der LHM angepasst (siehe unten).  

CKAN-Version 2.9.9

## Installation 
 
    $ docker pull ghcr.io/ondics/ckan-sddi-odp:odp-katalog-1.2.0

## CKAN Extensions

Dieses Image verwendet verschiedene CKAN Extensions.  

Zunächst gibt es View-Plugins.  
Diese ermöglichen die Ressourcenvorschau im Web:  
    
    image_view  
    text_view  
    recline_view  
    recline_map_view  
    recline_graph_view  
    recline_grid_view  
    webpage_view  

Weiterhin werden die [`Datastore und Datapusher`](https://docs.ckan.org/en/2.9/maintaining/datastore.html) Extensions verwendet.  
Diese ermöglichen zusammen das Hochladen von strukturierten Ressourcen (wie CSV oder Excel) in die Datastore Datenbank. Dies erlaubt mehr Möglichkeiten für die Ressourcenvorschau im Web, sowie die Nutzung der Datastore API um die Inhalte dieser Ressourcen direkt zu durchsuchen und zu bearbeiten.  

Insgesamt sind folgende Plugins aktiviert:  

    ENV CKAN__PLUGINS "image_view text_view recline_view recline_map_view recline_graph_view recline_grid_view \
    webpage_view datastore datapusher ogdmunich pages showcase harvest ckan_harvester csw_harvester dcat dcatde \
    dcat_rdf_harvester dcat_json_harvester dcat_json_interface structured_data \
    spatial_metadata spatial_query envvars"

Die folgenden weiteren Extensions gehen über sddi-base hinaus und werden über das Dockerfile installiert und eingerichtet:  

| Extension | Version | Beschreibung |
|---|---|---|
|`ogdmunich` | `1.5.0` | Theme für das ODP München |
| [`pages`](https://github.com/ckan/ckanext-pages) | `v0.5.2` | Erstellen von zusätzlichen Seiten |
| [`showcase`](https://github.com/ckan/ckanext-showcase) |  `v1.6.1` | Präsentation von Apps und Webanwendungen und Verknüpfung mit Datensätzen |
| [`harvest`](https://github.com/ckan/ckanext-harvest) | `v1.5.6` | Harvesting von Daten ins Open Data Portal |
| [`dcat`](https://github.com/ckan/ckanext-dcat) | `v2.3.0` | Abbildung CKAN Metadaten auf DCAT Konformität und umgekehrt |
| [`dcatde`](https://github.com/GovDataOfficial/ckanext-dcatde) | `6.9.0` | Abbildung CKAN Metadaten auf DCAT-AP Konformität und umgekehrt |
| [`spatial`](https://github.com/MarijaKnezevic/ckanext-spatial) | `c2118b9` | Ermöglicht Datensatzsuche anhand von Geodaten |

## Autor

(C) Copyright 2025, Ondics GmbH im Auftrag von LHM München