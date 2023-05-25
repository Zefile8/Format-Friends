import sqlite3
import random
from urllib.request import urlopen

#line exceptions
exceptions = ("!Everchanging Format","$whitelist","#Forbidden","#Limited","#Semi-Limited","#Unlimited")

#prepare vars
banlist_file = open("Everchanging Format.lflist.conf","w+")
banlist = []
database = []
selectin = []
selectout = []
try:
    nbremove = int(input("Nb to remove: "))
except:
    nbremove = 2
try:
    nbadd = int(input("Nb to add: "))
except:
    nbadd = 10

#grab current banlist
banlist_url = urlopen("https://raw.githubusercontent.com/NoLegs1/everchanging/main/Everchanging%20Format.lflist.conf")
textlist = banlist_url.read().decode("utf-8").splitlines()
for line in textlist:
    if not any(exc in line for exc in exceptions):
        banlist.append(line)

# connecting databases
cdb1 = sqlite3.connect('./expansions/cards.cdb')
cdb2 = sqlite3.connect('./repositories/delta-puppet/cards.delta.cdb')

# cursor object
cursor_obj1 = cdb1.cursor()
cursor_obj2 = cdb2.cursor()
# select relevant columns
selectall = '''SELECT id, name FROM texts'''
cursor_obj1.execute(selectall)
cursor_obj2.execute(selectall)
database1 = cursor_obj1.fetchall()
database2 = cursor_obj2.fetchall()
#getting the cards list in one variable
combine = database1 + database2
# remove duplicates
for i in combine:
  if i not in database:
    database.append(i)
# Close the connection
cdb1.commit()
cdb2.commit()
cdb1.close()
cdb2.close()


# select card(s) to remove
selectout = random.sample(banlist, nbremove)
banlist = [notout for notout in banlist if notout not in selectout]
print("Removed:")
for line in selectout:
    print("-"+" ("+line.replace(" ", "")[:-1]+")")

# write banlist to file
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
while i < 3:
    i += 1
    if i == 1 : banlist_file.write("\n#Limited")
    if i == 2 : banlist_file.write("\n#Semi-Limited")
    if i == 3 : banlist_file.write("\n#Unlimited")

# select cards to add
i = 0
print("Added:")
while i<nbadd:
    duplicate = 0
    selectin = random.choice(database)
    exceptions = banlist + selectout
    for line in exceptions:
        lineid = line.replace(" ", "")[:-1]
        if str(selectin[0]) == lineid:
            print("duplicate found: "+selectin[1])
            duplicate = 1
    if duplicate == 0:
        newline = str(selectin[0])+" 3"
        banlist.append(newline)
        banlist_file.write("\n"+str(selectin[0])+" 3")
        print("-"+selectin[1]+" ("+str(selectin[0])+")")
        i += 1

banlist_file.flush()
banlist_file.close()

import time
time.sleep(600)