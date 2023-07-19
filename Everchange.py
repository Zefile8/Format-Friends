import sqlite3
import random
import time
from urllib.request import urlopen

#inputs
format = str(input("Format: "))
if format == "":
    format = "Everchanging"
try:
    nbremove = int(input("Nb to remove: "))
except:
    nbremove = 2
try:
    nbadd = int(input("Nb to add: "))
except:
    nbadd = 10

#line exceptions
name_exception = ("!"+format+" Format")
exceptions = (name_exception,"$whitelist","#Forbidden","#Limited","#Semi-Limited","#Unlimited")

#prepare vars
filename = (format+" Format.lflist.conf")
banlist_file = open(filename,"w+")
banlist = []
database = []
selectin = []
selectout = []
tokens = ['176393 0','645088 0','904186 0','1426715 0','1799465 0','2625940 0','2819436 0','3285552 0','4417408 0','7392746 0','7610395 0','8025951 0','8198621 0','9047461 0','9925983 0','9929399 0','10389143 0','11050416 0','11050417 0','11050418 0','11050419 0','11738490 0','12958920 0','12965762 0','13536607 0','13935002 0','14089429 0','14470846 0','14470847 0','14957441 0','15341822 0','15341823 0','15394084 0','15590356 0','15629802 0','16943771 0','16946850 0','17228909 0','17418745 0','18027139 0','18027140 0','18027141 0','19280590 0','20001444 0','20368764 0','21179144 0','21770261 0','21830680 0','22110648 0','22404676 0','22493812 0','22953212 0','23116809 0','23331401 0','23837055 0','24874631 0','25415053 0','25419324 0','26326542 0','27198002 0','27204312 0','27450401 0','27882994 0','28053764 0','28062326 0','28355719 0','28674153 0','29491335 0','29843092 0','29843093 0','29843094 0','30069399 0','30650148 0','30811117 0','31480216 0','31533705 0','31986289 0','32335698 0','32446631 0','34479659 0','34767866 0','34822851 0','35268888 0','35514097 0','38030233 0','38041941 0','38053382 0','39972130 0','40703223 0','40844553 0','41329459 0','42671152 0','42956964 0','43140792 0','43664495 0','44026394 0','44052075 0','44092305 0','44097051 0','44308318 0','44330099 0','44586427 0','44689689 0','46173680 0','46173681 0','46647145 0','47658965 0','48068379 0','48115278 0','48411997 0','49808197 0','51208047 0','51611042 0','51987572 0','52340445 0','52900001 0','53855410 0','53855411 0','54537490 0','55326323 0','56051649 0','56597273 0','58371672 0','59160189 0','60025884 0','60406592 0','60514626 0','60764582 0','60764583 0','62125439 0','62543394 0','63184228 0','63442605 0','64213018 0','64382840 0','64382841 0','65500516 0','65810490 0','66200211 0','66661679 0','67284108 0','67284109 0','67284110 0','67284111 0','67489920 0','67922703 0','67949764 0','68815402 0','69550260 0','69811711 0','69868556 0','69890968 0','70391589 0','70465811 0','70875956 0','70950699 0','71645243 0','72291079 0','73915052 0','73915053 0','73915054 0','73915055 0','74440056 0','74627017 0','74983882 0','75119041 0','75524093 0','75622825 0','75732623 0','76589547 0','79387393 0','81767889 0','82255873 0','82324106 0','82340057 0','82556059 0','82994510 0','83239740 0','84816245 0','85243785 0','85771020 0','85771021 0','86801872 0','86871615 0','87669905 0','88923964 0','89907228 0','90884404 0','91512836 0','93104633 0','93130022 0','93224849 0','93912846 0','94703022 0','94973029 0','97452818 0','98596597 0','98875864 0','18494512 0','30327675 0','30327676 0','30765616 0','31600514 0','36629636 0','40551411 0','59900656 0','64583601 0','70465811 0','85969518 0']
alts = ['41356846 0','86120752 0','4280259 0','6150045 0','14558128 0','81480460 0','73580472 0','23995347 0','23995348 0','89631140 0','89631141 0','89631142 0','89631143 0','89631144 0','89631145 0','89631146 0','31833039 0','85289966 0','78193832 0','91152257 0','91152258 0','55878039 0','82044279 0','57728571 0','70095155 0','10443958 0','1546124 0','46986415 0','46986416 0','46986417 0','46986418 0','46986419 0','36996508 0','46986420 0','46986421 0','38033122 0','38033123 0','38033124 0','38033125 0','38033126 0','43892409 0','98502114 0','98502115 0','16195943 0','1861630 0','83965311 0','84257639 0','46173681 0','80193356 0','94145022 0','20366275 0','94977270 0','95440947 0','21844577 0','58932616 0','89943724 0','20721929 0','40044919 0','31887906 0','68881650 0','4376659 0','40542826 0','31764354 0','78661339 0','81172177 0','73134081 0','5043012 0','5043011 0','99267151 0','45231178 0','15341823 0','81439174 0','6368039 0','69140099 0','73642297 0','52038442 0','59438931 0','62015409 0','60643554 0','36354008 0','78437365 0','31122091 0','18144506 0','11050417 0','11050418 0','11050419 0','65741787 0','77585514 0','38342336 0','37390590 0','40640058 0','40640059 0','97590748 0','60764583 0','90330454 0','87322378 0','7852510 0','68540058 0','32012842 0','83764718 0','83011277 0','32003339 0','84013238 0','90590304 0','10000001 0','10000002 0','16178682 0','16178683 0','19230407 0','14470847 0','29843092 0','29843093 0','29843094 0','39751093 0','61307543 0','42035045 0','27911550 0','24433921 0','27847700 0','74677423 0','74677424 0','74677425 0','74677426 0','74677427 0','64335804 0','88264979 0','14878872 0','83555667 0','41463182 0','23401840 0','73915053 0','73915054 0','73915055 0','63288574 0','10000021 0','10000022 0','47852925 0','18807108 0','44508095 0','41209828 0','70781053 0','70781054 0','70781055 0','90740330 0','84080938 0','10000011 0','10000012 0','41462084 0','49791928 0','15259704 0','10802916 0','35686187 0','32448766 0','80604091 0','56043446 0','14898067 0','56993277 0','77754945 0','57116034 0','91998120 0','91998121 0']

#grab current banlist
url_name = ("https://raw.githubusercontent.com/NoLegs1/everchanging/main/"+format+"%20Format.lflist.conf")
try:
    banlist_url = urlopen(url_name)
except:
    print("Name error!")
    time.sleep(600)
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
    exceptions = banlist + selectout + tokens + alts
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

time.sleep(600)