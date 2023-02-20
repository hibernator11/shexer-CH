from shexer.shaper import Shaper
from shexer.consts import NT

target_classes = [
    "http://schema.org/Person",
    "http://schema.org/Book",
    "http://schema.org/Place",
    "http://schema.org/Organization"
]

namespaces_dict = {"http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
                   "http://www.w3.org/2000/01/rdf-schema#": "rdfs", 
                   "http://example.org/": "ex",
                   "http://weso.es/shapes/": "",
                   "http://www.w3.org/2001/XMLSchema#": "xsd",
                   "http://www.cidoc-crm.org/cidoc-crm/": "cidoc-crm",
                   "http://schema.org/": "schema",
                   "http://rdfs.org/ns/void#": "void",
                   "http://creativecommons.org/ns#": "creativeCommons",
                   "http://purl.org/dc/terms/": "dc",
                   "http://www.w3.org/2003/01/geo/wgs84_pos#": "geo",
                   "http://purl.org/ontology/bibo/": "bibo"
                   }

url_endpoint="https://data.bibliotheken.nl/sparql"

list_of_url_input= [
#author
"http://data.bibliotheken.nl/id/thes/p067739768",
"http://data.bibliotheken.nl/id/thes/p068474202",
"http://data.bibliotheken.nl/id/thes/p069180229",

#work
"http://data.bibliotheken.nl/doc/nbt/p036355941",
"http://data.bibliotheken.nl/doc/nbt/p037962930",
"http://data.bibliotheken.nl/doc/nbt/p03797453X",


#place
"http://data.bibliotheken.nl/id/thes/p075582449",
"http://data.bibliotheken.nl/id/thes/p075582457",
"http://data.bibliotheken.nl/id/thes/p075582465",
"http://data.bibliotheken.nl/id/thes/p075582473",
"http://data.bibliotheken.nl/id/thes/p075582481",
]

shaper = Shaper(target_classes=target_classes,
                list_of_url_input=list_of_url_input, 
                input_format=NT,
                namespaces_dict=namespaces_dict)  # Default: no prefixes

output_file = "shaper_nl_class_integration2.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.7)

print("Done!")
