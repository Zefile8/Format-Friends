import string
import json

list_name = "GARBO.lflist.conf"
map_name = "mappings.json"
edits = 0

with open(map_name) as map_file:
    map_data = json.load(map_file)
    mappings = map_data['mappings']
    for old, new in mappings:
        oldstr = str(old)
        newstr = str(new)
        with open(list_name, 'r') as list:
                list_data = list.read()
        list_data_new = list_data.replace(oldstr, newstr)
        if list_data != list_data_new:
            edits=edits+1
            with open(list_name, 'w') as list:
                list.write(list_data_new)

print("\nid updates: " + str(edits)+"\n")