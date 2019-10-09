import json
import os

# get the json file by
# entities = self.sg.schema_entity_read()

f = open("schema.json","r")
entities = json.load(f)
f.close()

# Record all link of entity[field]
entitylink = {}
# Record all type of entity[field]
entitytype = {} 

for entity in entities:
	if entity not in entitylink: 
		entitylink[entity]= {}

	if entity not in entitytype: 
		entitytype[entity]= {}


	if entity in ["EventLogEntry","Reply"]:
		continue

	for field in entities[entity]["fields"].keys():



		#
		# this flood the graph without interest
		# 
		if field in ["image_source_entity","created_by","updated_by"]:
			continue


		if entities[entity]["fields"][field]["data_type"]["value"] == "entity" or entities[entity]["fields"][field]["data_type"]["value"] == "multi_entity": 
			entitylink[entity][field] = entities[entity]["fields"][field]["typeEntity"]
		else:

			entitytype[entity][field] = entities[entity]["fields"][field]["data_type"]["value"]

#
# Output
#
print("""digraph g { graph [ rankdir = "LR" ]; """);

for entity in entities:

  print("""
   "%s" [
    shape=none
    label=<
      <table border="0" cellspacing="0" cellborder="1">
        <tr><td bgcolor="lightblue2"><font face="Times-bold" point-size="20">%s</font></td></tr>
   """ % (entity,entity))

  for field in entities[entity]["fields"].keys():
	if field in entitytype[entity]:
    		print("""<tr><td bgcolor="grey96" align="left" port="%s"><font face="Times-bold">%s </font>  <font color="#535353">%s  </font></td></tr> """ % (field,field,  entitytype[entity][field]))
	else:
    		print("""<tr><td bgcolor="grey96" align="left" port="%s"><font face="Times-bold">%s</font>  <font color="#535353">  </font></td></tr> """ % (field,field))

  print(""" </table> 
       >]; """)
	
#
# Connection between table
#
for entity in entitylink:
  #if entity != "Asset":
  #   continue
  for field in entitylink[entity]:
	#
	# this flood the graph without interest
	# 
	if field =="image_source_entity":
		continue

	for c in entitylink[entity][field]: 
               print(" %s:%s -> %s; " % ( entity, field , c ) )

print("}");
