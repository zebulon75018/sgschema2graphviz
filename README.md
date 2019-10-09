# sgschema2graphviz

[French doc :] (https://vidalcharles.blogspot.com/2019/10/shotgun-graphiz-schema.html)

convert schema of Shotgun projet to graphviz

you should first of all download in json file the SG schema with shotgun_api3.shotgun.Shotgun.schema_entity_read

usage:

* python sgschema2graphviz.py > test2.dot
* dot -Tsvg test2.dot > test2.svg


![Result](/schemasg.jpg)


"Special thanks to the Autodesk® Shotgun® Team. Copyright © AutodeskInc."

