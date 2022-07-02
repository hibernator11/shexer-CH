from shexer.shaper import Shaper
from shexer.consts import NT, SHEXC, SHACL_TURTLE

target_classes = [
#     "http://www.europeana.eu/schemas/edm/WebResource"
#     "http://rdfs.org/sioc/services#Service"
#     "http://www.europeana.eu/schemas/edm/ProvidedCHO"
     "http://www.openarchives.org/ore/terms/Aggregation"
#     "http://www.w3.org/2004/02/skos/core#Concept"
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
                   "http://purl.org/dc/terms/": "dc-terms",
                   "http://www.w3.org/2003/01/geo/wgs84_pos#": "geo",
                   "http://purl.org/ontology/bibo/": "bibo",
                   "http://www.europeana.eu/schemas/edm/": "edm",
                   "http://www.openarchives.org/ore/terms/": "ore",
                   "http://www.w3.org/2004/02/skos/core#": "skos",
                   "http://purl.org/dc/elements/1.1/": "dc",
                   "http://usefulinc.com/ns/doap": "doap",
                   "http://rdfs.org/sioc/services#": "services"
                   }

url_endpoint="https://lod.onb.ac.at/sparql/anno"

shaper = Shaper(target_classes=target_classes,
                #raw_graph=raw_graph,
                #graph_file_input=input_nt_file,
                url_endpoint=url_endpoint, 
                input_format=NT,
                limit_remote_instances=200,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = "shaper_onb_aggregation.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.4)

print("Done!")
