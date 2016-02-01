#!/usr/bin/env python
# download Moldova shapefile from here: http://www.gadm.org/country
# ogr2ogr -f "GeoJSON" boost-moldova.geojson MDA_adm1.shp MDA_adm1

import json

translation = {
    'Anenii Noi': 'District Council Anenii Noi',
    'Şoldăneşti': 'District Council Soldanesti',
    'Ştefan Voda': 'District Council Stefan-Voda',
    'Bălţi': 'Council of the municipality of Balti',
    'Basarabeasca': 'District Council Basarabeasca',
    'Bender': '',
    'Briceni': 'District Council Briceni',
    'Cahul': 'District Council Cahul',
    'Calarasi': 'District Council Calarasi',
    'Cantemir': 'District Council Cantemir',
    'Causeni': 'District Council Causeni',
    'Chişinău': 'Council of the municipality of Chisinau',
    'Cimişlia': 'District Council Cimislia',
    'Criuleni': 'District Council Criuleni',
    'Donduseni': 'District Council Donduseni',
    'Drochia': 'District Council Drochia',
    'Dubăsari': 'District Council Dubasari',
    'Edineţ': 'District Council Edinet',
    'Făleşti': 'District Council Falesti',
    'Floreşti': 'District Council Floresti',
    'Găgăuzia': 'District Council ATU Gagauzia',
    'Glodeni': 'District Council Glodeni',
    'Hîncesti': 'District Council Hincesti',
    'Ialoveni': 'District Council Ialoveni',
    'Leova': 'District Council Leova',
    'Nisporeni': 'District Council Nisporeni',
    'Ocniţa': 'District Council Ocnita',
    'Orhei': 'District Council Orhei',
    'Rîşcani': 'District Council Riscani',
    'Rezina': 'District Council Rezina',
    'Sîngerei': 'District Council Singerei',
    'Soroca': 'District Council Soroca',
    'Străşeni': 'District Council Straseni',
    'Taraclia': 'District Council Taraclia',
    'Teleneşti': 'District Council Telenesti',
    'Transnistria': '',
    'Ungheni': 'District Council Ungheni',
}

with open('archive/boost-moldova.geojson', 'r') as i:
    with open('data/boost-moldova.geojson', 'w') as o:
        bm = json.load(i)
        for feature in bm['features']:
            fname = feature['properties']['NAME_1']
            if fname in translation:
                feature['properties']['name'] = translation[fname]
        json.dump(bm, o)

    
        
        
