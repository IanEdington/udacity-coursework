#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with another type of infobox data, audit it, clean it,
come up with a data model, insert it into a MongoDB and then run some queries against your database.
The set contains data about Arachnid class.
Your task in this exercise is to parse the file, process only the fields that are listed in the
FIELDS dictionary as keys, and return a dictionary of cleaned values.

The following things should be done:
- keys of the dictionary changed according to the mapping in FIELDS dictionary
- trim out redundant description in parenthesis from the 'rdf-schema#label' field, like "(spider)"
- if 'name' is "NULL" or contains non-alphanumeric characters, set it to the same value as 'label'.
- if a value of a field is "NULL", convert it to None
- if there is a value in 'synonym', it should be converted to an array (list)
  by stripping the "{}" characters and splitting the string on "|". Rest of the cleanup is up to you,
  eg removing "*" prefixes etc
- strip leading and ending whitespace from all fields, if there is any
- the output structure should be as follows:
{ 'label': 'Argiope',
  'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
  'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
  'name': 'Argiope',
  'synonym': ["One", "Two"],
  'classification': {
                    'family': 'Orb-weaver spider',
                    'class': 'Arachnid',
                    'phylum': 'Arthropod',
                    'order': 'Spider',
                    'kingdom': 'Animal',
                    'genus': None
                    }
}

"URI":                  "http://dbpedia.org/resource/Opisthoncana"
"rdf-schema#label":     "Opisthoncana"
"rdf-schema#comment":   "Opisthoncana is a spider genus of the Salticidae family (jumping spiders). Its sole described species O. formidabilis has only been found on New Ireland near New Guinea."
"binomialAuthority_label":  "Embrik Strand"
"binomialAuthority":    "http://dbpedia.org/resource/Embrik_Strand"
"class_label":          "Arachnid"
"class":                "http://dbpedia.org/resource/Arachnid"
"conservationStatus":   "NULL"
"conservationStatusSystem":     "NULL"
"division_label":       "NULL"
"division":             "NULL"
"family_label":         "{Euophryinae|Jumping spider}"
"family":               "{http://dbpedia.org/resource/Euophryinae|http://dbpedia.org/resource/Jumping_spider}"
"genus_label":          "NULL"
"genus":                "NULL"
"kingdom_label":        "Animal"
"kingdom":              "http://dbpedia.org/resource/Animal"
"order_label":          "Spider"
"order":                "http://dbpedia.org/resource/Spider"
"phylum_label":         "Arthropod"
"phylum":               "http://dbpedia.org/resource/Arthropod"
"species_label":        "NULL"
"species":              "NULL"
"synonym":              "NULL"
"thumbnail_label":      "200px-Distribution.opisthoncana.formidabilis.1.png"
"thumbnail":            "http://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Distribution.opisthoncana.formidabilis.1.png/200px-Distribution.opisthoncana.formidabilis.1.png"
"22-rdf-syntax-ns#type_label":  "{animal|arachnid|eukaryote|species|owl#Thing}"
"22-rdf-syntax-ns#type":    "{http://dbpedia.org/ontology/Animal|http://dbpedia.org/ontology/Arachnid|http://dbpedia.org/ontology/Eukaryote|http://dbpedia.org/ontology/Species|http://www.w3.org/2002/07/owl#Thing}"
"depiction_label":      "Distribution.opisthoncana.formidabilis.1.png"
"depiction":            "http://upload.wikimedia.org/wikipedia/commons/0/0d/Distribution.opisthoncana.formidabilis.1.png"
"name":                 "Opisthoncana"

"""
import codecs
import csv
import json
import pprint
import re

CSV_Path = 'arachnid.csv'
FIELD_Map ={'rdf-schema#label': 'label',
            'URI': 'uri',
            'rdf-schema#comment': 'description',
            'synonym': 'synonym',
            'name': 'name',
            'family_label': 'family',
            'class_label': 'class',
            'phylum_label': 'phylum',
            'order_label': 'order',
            'kingdom_label': 'kingdom',
            'genus_label': 'genus'}


def process_file(filename, fields):

    csv_field_names = fields.keys()
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = next(reader)

        for row in reader:
            '''
                - keys of the dictionary changed according to the mapping in FIELDS dictionary
                - trim out redundant description in parenthesis from the 'rdf-schema#label' field, like "(spider)"
                - if 'name' is "NULL" or contains non-alphanumeric characters, set it to the same value as 'label'.
                - if a value of a field is "NULL", convert it to None
                - if there is a value in 'synonym', it should be converted to an array (list)
                  by stripping the "{}" characters and splitting the string on "|". Rest of the cleanup is up to you,
                  eg removing "*" prefixes etc
                - strip leading and ending whitespace from all fields, if there is any
            '''
            row_data = {"classification": {}}
            for field in csv_field_names:
                if FIELD_Map[field] in ["kingdom", "family", "order", "phylum", "genus", "class"]:
                    if row[field] == 'NULL':
                        row_data['classification'][FIELD_Map[field]] = None
                    else:
                        row_data['classification'][FIELD_Map[field]] = row[field].strip()
                elif field =='rdf-schema#label':
                    if row[field] == 'NULL':
                        row_data[FIELD_Map[field]] = None
                    else:
                        row_data[FIELD_Map[field]] = row[field].split('(')[0].strip()
                elif (field =='name') & (row[field] == 'NULL'):
                    row_data[FIELD_Map[field]] = row['rdf-schema#label'].strip()
                elif field == 'synonym':
                    if row[field] == 'NULL':
                        row_data[FIELD_Map[field]] = None
                    else:
                        row_data[FIELD_Map[field]] = parse_array(row[field])
                else:
                    if row[field] == 'NULL':
                        row_data[FIELD_Map[field]] = None
                    else:
                        row_data[FIELD_Map[field]] = row[field].strip()
            data.append(row_data)

    return data


def parse_array(v):
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [i.strip() for i in v_array]
        return v_array
    return [v]


def test():
    data = process_file(CSV_Path, FIELD_Map)

    pprint.pprint(data[48])
    assert data[0] == {
                        "synonym": None,
                        "name": "Argiope",
                        "classification": {
                            "kingdom": "Animal",
                            "family": "Orb-weaver spider",
                            "order": "Spider",
                            "phylum": "Arthropod",
                            "genus": None,
                            "class": "Arachnid"
                        },
                        "uri": "http://dbpedia.org/resource/Argiope_(spider)",
                        "label": "Argiope",
                        "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
                    }


if __name__ == "__main__":
    test()
