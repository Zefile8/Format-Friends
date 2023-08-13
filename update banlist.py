import string
import re

#get banlist to edit
list_name = "banlist.lflist.conf"
banned_comment = "#forbidden"
limited_comment = "#limited"
semi_comment = "#semi-limited"
unlimited_comment = "#unlimited"
with open(list_name, 'r') as list:
    list_data = list.read()

#info vars
banned = 0
limited = 0
semi = 0
unlimited = 0
oof = 0

#get decklists
banned_deck = "¤banlist 1 - banned.ydk"
limited_deck = "¤banlist 2 - limited.ydk"
semi_deck = "¤banlist 3 - semi-limited.ydk"
unlimited_deck = "¤banlist 4 - unlimited.ydk"
oof_deck = "¤banlist 5 - O.O.F..ydk"

#get decklist
f = open(banned_deck)
lines = f.readlines()
#get ids
for curline in lines:
    id = re.search('[0-9]*',curline)
    #check id
    if id is not None and id[0] != "":
        #remove duplicates
        while True:
            duplicate = re.search(id[0]+' [0-3]',list_data)
            if duplicate is None:
                break
            list_data = list_data.replace('\n'+duplicate[0], '')
        #add ids to section
        list_data = list_data.replace(banned_comment, banned_comment+"\n"+id[0]+" 0", 1)
        banned = banned+1

#get decklist
f = open(limited_deck)
lines = f.readlines()
#get ids
for curline in lines:
    id = re.search('[0-9]*',curline)
    #check id
    if id is not None and id[0] != "":
        #remove duplicates
        while True:
            duplicate = re.search(id[0]+' [0-3]',list_data)
            if duplicate is None:
                break
            list_data = list_data.replace('\n'+duplicate[0], '')
        #add ids to section
        list_data = list_data.replace(limited_comment, limited_comment+"\n"+id[0]+" 1", 1)
        limited = limited+1

#get decklist
f = open(semi_deck)
lines = f.readlines()
#get ids
for curline in lines:
    id = re.search('[0-9]*',curline)
    #check id
    if id is not None and id[0] != "":
        #remove duplicates
        while True:
            duplicate = re.search(id[0]+' [0-3]',list_data)
            if duplicate is None:
                break
            list_data = list_data.replace('\n'+duplicate[0], '')
        #add ids to section
        list_data = list_data.replace(semi_comment, semi_comment+"\n"+id[0]+" 2", 1)
        semi = semi+1

#get decklist
f = open(unlimited_deck)
lines = f.readlines()
#get ids
for curline in lines:
    id = re.search('[0-9]*',curline)
    #check id
    if id is not None and id[0] != "":
        #remove duplicates
        while True:
            duplicate = re.search(id[0]+' [0-3]',list_data)
            if duplicate is None:
                break
            list_data = list_data.replace('\n'+duplicate[0], '')
        #add ids to section
        list_data = list_data.replace(unlimited_comment, unlimited_comment+"\n"+id[0]+" 3", 1)
        unlimited = unlimited+1

#get decklist
f = open(oof_deck)
lines = f.readlines()
#get ids
for curline in lines:
    id = re.search('[0-9]*',curline)
    #check id
    if id is not None and id[0] != "":
        #remove from list
        while True:
            toremove = re.search(id[0]+' [0-3]',list_data)
            if toremove is None:
                break
            list_data = list_data.replace('\n'+toremove[0], '')
        oof = oof+1

#export modified
with open(list_name, 'w') as list:
    list.write(list_data)

#report changes
print("\nnb banned: "+str(banned))
print("nb limited: "+str(limited))
print("nb semi: "+str(semi))
print("nb unlimited: "+str(unlimited))
print("nb oof: "+str(oof)+"\n")
