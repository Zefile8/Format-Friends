import sqlite3
import random
from urllib.request import urlopen

#line exceptions
exceptions = ("!Evershifting Format","$whitelist","#Forbidden","#Limited","#Semi-Limited","#Unlimited")

#prepare vars
banlist_file = open("Evershifting Format.lflist.conf","w+")
banlist = []
database = []
selectin = []
selectout = []
nbremove = 2
nbadd = 10
nbremove = int(input("Nb to remove: "))
nbadd = int(input("Nb to add: "))

#grab current banlist
banlist_url = urlopen("https://raw.githubusercontent.com/NoLegs1/everchanging/main/Evershifting%20Format.lflist.conf")
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

# remove banlist matches from database
print("Removed:")
for case in database:
    caseid = case[0]
    casename = case[1]
    caseid = str(caseid)
    for line in banlist:
        if caseid in line:
            database.remove(case)
            if line in selectout:
                banlist.remove(line)
                print("-"+casename+" ("+line.replace(" ", "")[:-1]+")")
#failsafe
for line in banlist:
    if line in selectout:
        banlist.remove(line)
        print("-"+"name not found"+" ("+line.replace(" ", "")[:-1]+")")

# write banlist to file
banlist_file.write('''!Evershifting Format\n$whitelist\n#Forbidden''')
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
selectin = random.sample(database, nbadd)
print("Added:")
for i in selectin:
    banlist_file.write("\n"+str(i[0])+" 3")
    print("-"+i[1]+" ("+str(i[0])+")")

banlist_file.flush()
banlist_file.close()

import time
time.sleep(600)