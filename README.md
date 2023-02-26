# shexer-CH
This project is based on the automatic data quality assessment of Linked Open Data repositories made available for the public by Cultural Heritage institutions.

### Background
This work explores how the quality of Linked Open Data made available by Cultural Heritage institutions can be automatically assessed. The results obtained can be useful for other institutions who wish to publish and assess their collections. This work is based on the tool [sheXer](https://github.com/DaniFdezAlvarez/shexer) to mine an RDF dataset to automatically generate the Shape Expressions.

### Shape Expressions 
The following links provide a set of Shape Expression examples based on relevant Cultural Heritage LOD datasets that can be assessed using the [ShEx2 Simple Online Validator tool](http://shex.io/webapps/shex.js/doc/shex-simple.html). These Shape Expressions have been automatically generated using the public SPARQL endpoints.

- [ShEx validation tool National Library of the Netherlands](https://rawgit.com/shexSpec/shex.js/wikidata/packages/shex-webapp/doc/shex-simple.html?manifestURL=https://raw.githubusercontent.com/hibernator11/shexer-CH/main/nl.manifest.json)

- [ShEx validation tool Austrian National Library](https://rawgit.com/shexSpec/shex.js/wikidata/packages/shex-webapp/doc/shex-simple.html?manifestURL=https://raw.githubusercontent.com/hibernator11/shexer-CH/main/onb.manifest.json)

- [ShEx validation tool World War I dataset](https://rawgit.com/shexSpec/shex.js/wikidata/packages/shex-webapp/doc/shex-simple.html?manifestURL=https://raw.githubusercontent.com/hibernator11/shexer-CH/main/ww1lod.manifest.json)


### Austrian National Library

A reproducible [Jupyter Notebook](https://nbviewer.org/github/hibernator11/shexer-CH/blob/main/onb/onb-sparql.ipynb) is provided for the [Austrian National Library dataset](https://labs.onb.ac.at/en/dataset/anno/) in order to show how to query the data based on the [Europeana Data Model vocabulary](https://pro.europeana.eu/page/edm-documentation).

### World War I LOD dataset 

This SPARQL sentence was used to retrieve examples of events including actors and places based on the CIDOC-CRM vocabulary in the [World War I LOD dataset](https://www.ldf.fi/dataset/ww1lod/). An [integrated Shape Expression](https://raw.githubusercontent.com/hibernator11/shexer-CH/main/ww1lod/shaper_nl_class_integration.shex) was created including the three elements as an illustrative example of how the value of a constraint can be defined by another shape. See the [ShEx documentation](https://shex.io/shex-primer/index.html#simple-expressions) for additional details.

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

### References
- Gustavo Candela: Towards a semantic approach in GLAM Labs: the case of the Data Foundry at the National Library of Scotland. CoRR abs/2301.11182 (2023). https://doi.org/10.48550/arXiv.2301.11182
- Daniel Fernandez Alvárez, José Emilio Labra, Daniel Gallo-Avello. Automatic extraction of shapes using sheXer. https://doi.org/10.1016/j.knosys.2021.107975

