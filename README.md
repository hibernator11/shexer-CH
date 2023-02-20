# shexer-CH
shexer-CH


### World War I LOD dataset

This SPARQL sentence was used to retrieve examples of events including actors and places based on the CIDOC-CRM vocabulary. An [integrated Shape Expression](https://raw.githubusercontent.com/hibernator11/shexer-CH/main/ww1lod/shaper_nl_class_integration.shex) was created including the three elements as an illustrative example of how a value of a contraint can be defined by another shape. 

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX cidoc-crm: <http://www.cidoc-crm.org/cidoc-crm/>

SELECT ?s ?actor ?place WHERE {
  ?s a cidoc-crm:E5_Event .
  ?s cidoc-crm:P14_carried_out_by ?actor .
  ?actor a cidoc-crm:E39_Actor .
  ?s cidoc-crm:P7_took_place_at ?place .
  ?place a cidoc-crm:E53_Place .
} 
LIMIT 10
```

