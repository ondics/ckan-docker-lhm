CHANGELOG
=========

21.10.2025 (v1.2.0):

* ENH: In Dockerfile ckanext-openapiview auf commit 9131c3f gesetzt zur Kompatibilität mit ckan 2.9.9

20.10.2025:

* ENH: Datensatzschema um Felder politicalGeocodingLevelURI und politicalGeocodingURI erweitert

17.10.2025:

* ENH: in Zusätzliche Informationen bei Ressourcen neuer Tabelleneintrag "Format (DCAT)" und Tabellenzeile Format
* ENH: Mapping Datei von CKAN nach DCAT konformen Feldern für Ressourcen format und mediaType
* ENH: dcat Profile Anpassungen für govdata konforme dct:format und dcat:mediaType
* ENH: Erweiterung DCATdeProfile durch eigenes Profil OGDMunichDCATProfile

16.10.2025:

* ENH: Verlinkung Musterdatenkatalog

06.06.2024:

* FIX: Base Image für Dockerfile.debug aktualisiert

22.05.2024:

* FIX: Import logic Funktionen aus plugin.py entfernt

21.05.2024 (v1.1.0):

* ENH: API-Link zu Datensatz (in datasetview)
* ENH: Metadaten-Links zu rdf, json, tt3, n3 (in datasetview)
* ENH: OpenAPI View Plugin installiert

25.04.2024:

* ENH: Datensatzfelder Musterdatenkatalog, Update-Zyklus und HVD hinzugefügt über ckanext-scheming

18.04.2024:

* FIX: Image Version für debug workflow angepasst

17.04.2024:

* ENH: Workflows für ckan-sddi-odp Packages

16.04.2024:

* ENH: Readme geschrieben
* ENH: Dockerfile.debug hinzugefügt

15.04.2024:

* ENH: harvest Extension in Dockerfile hinzugefügt
* ENH: view Plugins aus production.ini von bisherigem Portal hinzugefügt
* ENH: ACHTUNG: CKAN_STORAGE_PATH ENV wieder anpassen zu /var/lib/ckan vor Update
* ENH: einige config von production.ini des bisherigen Portals übernommen

12.04.2024:

* ENH: dcat, dcatde Extensions in Dockerfile hinzugefügt

10.04.2024:

* ENH: sddi-odp Dockerfile erstellt, Ausgangsdatei sddi-base Dockerfile
