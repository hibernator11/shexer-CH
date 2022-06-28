from shexer.shaper import Shaper
from shexer.consts import NT, SHEXC, SHACL_TURTLE

target_classes = [
    "http://example.org/Person",
    "http://example.org/Gender"
]

namespaces_dict = {"http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
                   "http://example.org/": "ex",
                   "http://weso.es/shapes/": "",
                   "http://www.w3.org/2001/XMLSchema#": "xsd"
                   }

raw_graph = """
<http://example.org/sarah> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Person> .
<http://example.org/sarah> <http://example.org/age> "30"^^<http://www.w3.org/2001/XMLSchema#int> .
<http://example.org/sarah> <http://example.org/name> "Sarah" .
<http://example.org/sarah> <http://example.org/gender> <http://example.org/Female> .
<http://example.org/sarah> <http://example.org/occupation> <http://example.org/Doctor> .
<http://example.org/sarah> <http://example.org/brother> <http://example.org/Jim> .

<http://example.org/jim> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Person> .
<http://example.org/jim> <http://example.org/age> "28"^^<http://www.w3.org/2001/XMLSchema#int> .
<http://example.org/jim> <http://example.org/name> "Jimbo".
<http://example.org/jim> <http://example.org/surname> "Mendes".
<http://example.org/jim> <http://example.org/gender> <http://example.org/Male> .

<http://example.org/Male> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Gender> .
<http://example.org/Male> <http://www.w3.org/2000/01/rdf-schema#label> "Male" .
<http://example.org/Female> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Gender> .
<http://example.org/Female> <http://www.w3.org/2000/01/rdf-schema#label> "Female" .
<http://example.org/Other> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Gender> .
<http://example.org/Other> <http://www.w3.org/2000/01/rdf-schema#label> "Other gender" .
"""



input_nt_file = "target_graph.nt"

shaper = Shaper(target_classes=target_classes,
                raw_graph=raw_graph,
                input_format=NT,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = "shaper_example.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.1)

print("Done!")
