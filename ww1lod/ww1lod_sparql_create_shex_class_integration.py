from shexer.shaper import Shaper
from shexer.consts import NT

target_classes = [
    "http://www.cidoc-crm.org/cidoc-crm/E5_Event",
    "http://www.cidoc-crm.org/cidoc-crm/E39_Actor", 
    "http://www.cidoc-crm.org/cidoc-crm/E53_Place"
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
                   "http://www.w3.org/2004/02/skos/core#": "skos",
                   "http://encyclopedia.1914-1918-online.net/lod/schema#": "enc",
                   "http://ldf.fi/ww1lod/schema#": "ww1lod"
}

url_endpoint="http://ldf.fi/ww1lod/sparql"

list_of_url_input= [

#event
"http://ldf.fi/ww1lod/62bff175",
"http://ldf.fi/ww1lod/21084a29",
"http://ldf.fi/ww1lod/73b7794c",
"http://ldf.fi/ww1lod/eda57b6b",
"http://ldf.fi/ww1lod/655e0c1d",

#place
"http://ldf.fi/ww1lod/aca7bec4",
"http://ldf.fi/ww1lod/1912cfe4",
"http://ldf.fi/ww1lod/1912cfe4",
"http://ldf.fi/ww1lod/4e451641",	

#actor
	
"http://ldf.fi/ww1lod/ba7a31a0",
"http://ldf.fi/ww1lod/ba7a31a0",
]

shaper = Shaper(target_classes=target_classes,
                list_of_url_input=list_of_url_input, 
                input_format=NT,
                namespaces_dict=namespaces_dict)  # Default: no prefixes

output_file = "shaper_nl_class_integration.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.7)

print("Done!")
