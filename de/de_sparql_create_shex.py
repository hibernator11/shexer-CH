from shexer.shaper import Shaper
from shexer.consts import NT, SHEXC, SHACL_TURTLE

target_classes = [
#    "https://id.kb.se/vocab/Record"
#    "https://id.kb.se/vocab/Item"
#    "https://id.kb.se/vocab/Title"
#    "https://id.kb.se/vocab/MediaObject"
    "http://data.archiveshub.ac.uk/def/ArchivalResource"
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
                   "http://purl.org/ontology/bibo/": "bibo",
                   "http://data.archiveshub.ac.uk/def/": "dev"
                   }

url_endpoint="https://slod.fiz-karlsruhe.de/sparql"

shaper = Shaper(target_classes=target_classes,
                #raw_graph=raw_graph,
                #graph_file_input=input_nt_file,
                url_endpoint=url_endpoint, 
                input_format=NT,
                limit_remote_instances=15,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = "shaper_de_archivalresource.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.7)

print("Done!")
