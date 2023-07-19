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
tokens = ['176393','645088','904186','1426715','1799465','2625940','2819436','3285552','4417408','7392746','7610395','8025951','8198621','9047461','9925983','9929399','10389143','11050416','11050417','11050418','11050419','11738490','12958920','12965762','13536607','13935002','14089429','14470846','14470847','14957441','15341822','15341823','15394084','15590356','15629802','16943771','16946850','17228909','17418745','18027139','18027140','18027141','19280590','20001444','20368764','21179144','21770261','21830680','22110648','22404676','22493812','22953212','23116809','23331401','23837055','24874631','25415053','25419324','26326542','27198002','27204312','27450401','27882994','28053764','28062326','28355719','28674153','29491335','29843092','29843093','29843094','30069399','30650148','30811117','31480216','31533705','31986289','32335698','32446631','34479659','34767866','34822851','35268888','35514097','38030233','38041941','38053382','39972130','40703223','40844553','41329459','42671152','42956964','43140792','43664495','44026394','44052075','44092305','44097051','44308318','44330099','44586427','44689689','46173680','46173681','46647145','47658965','48068379','48115278','48411997','49808197','51208047','51611042','51987572','52340445','52900001','53855410','53855411','54537490','55326323','56051649','56597273','58371672','59160189','60025884','60406592','60514626','60764582','60764583','62125439','62543394','63184228','63442605','64213018','64382840','64382841','65500516','65810490','66200211','66661679','67284108','67284109','67284110','67284111','67489920','67922703','67949764','68815402','69550260','69811711','69868556','69890968','70391589','70465811','70875956','70950699','71645243','72291079','73915052','73915053','73915054','73915055','74440056','74627017','74983882','75119041','75524093','75622825','75732623','76589547','79387393','81767889','82255873','82324106','82340057','82556059','82994510','83239740','84816245','85243785','85771020','85771021','86801872','86871615','87669905','88923964','89907228','90884404','91512836','93104633','93130022','93224849','93912846','94703022','94973029','97452818','98596597','98875864','18494512','30327675','30327676','30765616','31600514','36629636','40551411','59900656','64583601','70465811','85969518']
alts = ['41356846','86120752','4280259','6150045','14558128','81480460','73580472','23995347','23995348','89631140','89631141','89631142','89631143','89631144','89631145','89631146','31833039','85289966','78193832','91152257','91152258','55878039','82044279','57728571','70095155','10443958','1546124','46986415','46986416','46986417','46986418','46986419','36996508','46986420','46986421','38033122','38033123','38033124','38033125','38033126','43892409','98502114','98502115','16195943','1861630','83965311','84257639','46173681','80193356','94145022','20366275','94977270','95440947','21844577','58932616','89943724','20721929','40044919','31887906','68881650','4376659','40542826','31764354','78661339','81172177','73134081','5043012','5043011','99267151','45231178','15341823','81439174','6368039','69140099','73642297','52038442','59438931','62015409','60643554','36354008','78437365','31122091','18144506','11050417','11050418','11050419','65741787','77585514','38342336','37390590','40640058','40640059','97590748','60764583','90330454','87322378','7852510','68540058','32012842','83764718','83011277','32003339','84013238','90590304','10000001','10000002','16178682','16178683','19230407','14470847','29843092','29843093','29843094','39751093','61307543','42035045','27911550','24433921','27847700','74677423','74677424','74677425','74677426','74677427','64335804','88264979','14878872','83555667','41463182','23401840','73915053','73915054','73915055','63288574','10000021','10000022','47852925','18807108','44508095','41209828','70781053','70781054','70781055','90740330','84080938','10000011','10000012','41462084','49791928','15259704','10802916','35686187','32448766','80604091','56043446','14898067','56993277','77754945','57116034','91998120','91998121']

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
    exceptions = banlist + selectout
    for line in exceptions:
        lineid = line.replace(" ", "")[:-1]
        if str(selectin[0]) == lineid:
            print("duplicate found: "+selectin[1])
            duplicate = 1
    exceptions = exceptions + tokens + alts
    if duplicate == 0:
        newline = str(selectin[0])+" 3"
        banlist.append(newline)
        banlist_file.write("\n"+str(selectin[0])+" 3")
        print("-"+selectin[1]+" ("+str(selectin[0])+")")
        i += 1

banlist_file.flush()
banlist_file.close()

time.sleep(600)