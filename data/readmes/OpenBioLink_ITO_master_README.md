# Intelligence Task Ontology and Knowledge Graph (ITO). An AI ontology.
## A comprehensive knowledge graph of artificial intelligence tasks and benchmarks
The Intelligence Task Ontology and Knowledge Graph (ITO) provides comprehensive, curated and interlinked data of artificial intelligence tasks, benchmarks, AI performance metrics, benchmark results and research papers.

**You can explore ITO in our [ITO Explorer](https://openbiolink.github.io/ITOExplorer/) dashboard or browse the ITO class hierarchy [online at BioPortal](https://bioportal.bioontology.org/ontologies/ITO/?p=classes&conceptid=https%3A%2F%2Fidentifiers.org%2Fito%3AITO_00141).**

### Examples
ITO aims to provide a richly structured hierarchy of processes, algorithms, data and performance metrics. Data on thousands of AI benchmark results have been imported from [Papers With Code](https://paperswithcode.com/) and are further curated.

An example of a benchmark result embedded in an ontological hierarchy:

![MRI Example Hierarchy](/media/example-hierarchy-1-detail-with-score.PNG)

Exploring the class hierarchy:

> ![Class hierarchy screen capture](media/screencapture-class-hierarchy-in-webprotege.gif)

Exploring the hierarchy of perfomance measures:

> ![Property hierarchy screen capture](media/screencapture-property-hierarchy-in-webprotege.gif)


### Using ITO

ITO is made available as an OWL (Web Ontology Language) file. You can use the [Protege ontology editor](https://protege.stanford.edu/) to explore and edit the resource. You can use a wide variety of frameworks for OWL, RDF and the SPARQL graph query language to access and query the ontology. We recommend using the [Blazegraph](https://blazegraph.com/) triple store. 

Example: [Google Colab notebook demonstrating SPARQL queries with ITO](https://colab.research.google.com/drive/1g3gDgakBcmAfIi4opXX99KXB7yALK66S?usp=sharing).

We also make light-weight JSON files containing an export of the curated hierarchies of AI process / task classes and performance metrics. Note that these exports do not contain the bulk of data from the OWL file, such as benchmark results.

### Citing ITO

> Kathrin Blagec, Adriano Barbosa-Silva, Simon Ott, Matthias Samwald. „A curated, ontology-based, large-scale knowledge graph of artificial intelligence tasks and benchmarks“. arXiv:2110.01434 [cs], October 2021. http://arxiv.org/abs/2110.01434

### Licensing

The ontology file and JSON extract files are distributed under a [CC-BY-SA 3.0 AT](https://creativecommons.org/licenses/by-sa/3.0/at/) license.

ITO includes data from the Papers With Code project (https://paperswithcode.com/). Papers With Code is licensed under the CC-BY-SA license. Data from Papers With Code are partially altered (manual curation to improve ontological structure and data quality).

ITO includes data from the EDAM ontology. The EDAM ontology is licensed under a CC-BY-SA license.

We offer ITO and related resources as-is and make no representations or warranties of any kind concerning the resources, express, implied, statutory or otherwise, including without limitation warranties of title, merchantability, fitness for a particular purpose, non infringement, or the absence of latent or other defects, accuracy, or the present or absence of errors, whether or not discoverable, all to the greatest extent permissible under applicable law.

### Contact

[Samwald research group](https://samwald.info/) @ Section for Artificial Intelligence and Decision Support, Medical University of Vienna
matthias.samwald (at) meduniwien.ac.at

[![Samwald research group logo](/media/samwald-research-group-logo.PNG)](https://samwald.info)

This project received funding from netidee.

![netidee logo](/media/netidee-logo.PNG)

