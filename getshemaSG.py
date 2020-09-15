import click
import json
import os
import shotgun_api3 
import pprint

@click.command()
@click.option("--nameserver",help="name of subdomain of shotgunstudio.com",required=True)
@click.option("--scriptname",help="name of script define in SG",required=True)
@click.option("--scriptkey",help="key associated to scriptname in SG ",required=True)
def getschema(nameserver, scriptname,scriptkey):
	""" getSchema program get from SG the schema and write ins schema.json """
	sg = shotgun_api3.Shotgun("https://%s.shotgunstudio.com" % (nameserver), scriptname, scriptkey)
	entities = sg.schema_entity_read()
	for k in entities:
		entities[k]["fields"]=sg.schema_field_read(k)

	for k in entities:	
		for e in entities[k]["fields"]:
			if e == "image_source_entity":
				continue
			# To many link for image_source_entity 
			if "valid_types" in entities[k]["fields"][e]["properties"].keys():
				entities[k]["fields"][e]["typeEntity"] = entities[k]["fields"][e]["properties"]["valid_types"]["value"]
			else: 
				entities[k]["fields"][e]["typeEntity"] = []

	with open('schema.json', 'w') as outfile:
    		json.dump(entities, outfile, indent=4)

if __name__ == '__main__':
    getschema()
#
#filters =[ ['project', 'is', {'type': 'Project', 'id': PROJECT_ID}] ]
#fields=["code","entity","id"]
#result = sg.find("CutItem",filters,fields)
#print(result)
