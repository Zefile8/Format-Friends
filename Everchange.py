import sqlite3
import random
from urllib.request import urlopen

#line exceptions
exceptions = ("!Everchanging Format","$whitelist","#Forbidden","#Limited","#Semi-Limited","#Unlimited")

#prepare vars
banlist_file = open("Everchanging Format.lflist.conf","w+")
banlist = []
toadd = []
output = []
selectoutname = ""

#grab current banlist
banlist_url = urlopen("https://raw.githubusercontent.com/NoLegs1/everchanging/main/Everchanging%20Format.lflist.conf")
# banlist_url = urlopen("https://raw.githubusercontent.com/NoLegs1/everchanging/main/testchanging.lflist.conf")
textlist = banlist_url.read().decode("utf-8").splitlines()
for line in textlist:
    if not any(exc in line for exc in exceptions):
        banlist.append(line)

# connecting databases
cdb1 = sqlite3.connect('./expansions/cards.cdb')
cdb2 = sqlite3.connect('./repositories/delta-puppet/cards.delta.cdb')
# debug databases
# cdb1 = sqlite3.connect('./cards.cdb')
# cdb2 = sqlite3.connect('./cards.delta.cdb')

# cursor object
cursor_obj1 = cdb1.cursor()
cursor_obj2 = cdb2.cursor()

# select relevant columns
selectall = '''SELECT id, name FROM texts'''
cursor_obj1.execute(selectall)
cursor_obj2.execute(selectall)
output1 = cursor_obj1.fetchall()
output2 = cursor_obj2.fetchall()
#getting the cards list in one variable
combine = output1 + output2
# remove duplicates
for i in combine:
  if i not in output:
    output.append(i)

# Close the connection
cdb1.commit()
cdb2.commit()
cdb1.close()
cdb2.close()

# select card to remove and remove cardpool from databases
selectout=random.randint(0, len(banlist)-1)
selectout = banlist[selectout].replace(" ", "")[:-1]
for case in output:
    curcase = case[0]
    curcase = str(curcase)
    for line in banlist:
        if curcase in line:
            output.remove(case)
            if curcase == selectout and selectoutname == "":
                selectoutname = case[1]
                banlist.remove(line)
print("Removed:")
print("-"+selectoutname+" ("+selectout+")")

# write to file
banlist_file.write('''!Everchanging Format\n$whitelist\n#Forbidden''')
i = 0
for line in banlist:
    line = line.replace(" ", "")
    if int(line[-1]) != i:
        i = int(line[-1])
        if i == 1 : banlist_file.write("\n#Limited")
        if i == 2 : banlist_file.write("\n#Semi-Limited")
        if i == 3 : banlist_file.write("\n#Unlimited")
    banlist_file.write("\n"+line[:-1]+" "+str(i))

if i != 3:
    i = 3
    banlist_file.write("\n#Unlimited")

# select cards to add
print("Added:")
for i in range(1, 7):
    selectin = output[random.randint(0, len(output)-1)]
    banlist_file.write("\n"+str(selectin[0])+" 3")
    print("-"+selectin[1]+" ("+str(selectin[0])+")")
    output.remove(selectin)

banlist_file.flush()
banlist_file.close()

import time
time.sleep(600)