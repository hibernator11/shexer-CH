from shexer.shaper import Shaper
from shexer.consts import NT, SHEXC, SHACL_TURTLE

target_classes = [
#    "http://www.cidoc-crm.org/cidoc-crm/E39_Actor",
#    "http://www.cidoc-crm.org/cidoc-crm/E21_Person",
    "http://www.cidoc-crm.org/cidoc-crm/E38_Image"
]

namespaces_dict = {"http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
                   "http://example.org/": "ex",
                   "http://weso.es/shapes/": "",
                   "http://www.w3.org/2001/XMLSchema#": "xsd",
                   "http://www.cidoc-crm.org/cidoc-crm/": "cidoc-crm",
                   "http://edan.si.edu/saam/id/person-institution/": "si-pi"
                   }

url_endpoint="http://edan.si.edu/saam/sparql"

shaper = Shaper(target_classes=target_classes,
                #raw_graph=raw_graph,
                #graph_file_input=input_nt_file,
                url_endpoint=url_endpoint, 
                input_format=NT,
                limit_remote_instances=50,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = "shaper_image.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.7)

print("Done!")
