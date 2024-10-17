import tkinter
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import webbrowser
import json
from urllib.request import urlopen
config_url = urlopen("https://raw.githubusercontent.com/ProjectIgnis/Distribution/master/config/configs.json")
config_data = json.load(config_url)
repos = config_data['repos']
servers = config_data['servers']

#_____________________________________________________________________________________________________________________________________________________


garbo = [
    {
        "url": "https://github.com/Zefile8/Garbo-lflist",
        "repo_name": "Garbo banlist",
        "repo_path": "./repositories/Garbo-lflist",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    }
]
trinity = [
    {
        "url": "https://github.com/Quakedrop/Trinity-Banlists",
        "repo_name": "Trinity banlist",
        "repo_path": "./repositories/TrinityLIST",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    },
    {
        "url": "https://github.com/Ejeffers1239/TrinityExtension",
        "repo_name": "Trinity Expansion",
        "repo_path": "./repositories/TrinityEXP",
        "data_path": "expansions",
        "script_path": "script",
        "should_update": True,
        "should_read": True
    }
]
_25th = [
    {
        "url": "https://github.com/thespideroi/25thLFlist",
        "repo_name": "25th Forbidden & Limited Card banlist",
        "repo_path": "./repositories/25thlflist",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    }
]
_3v3 = [
    {
        "url": "https://github.com/Bewilderer/3v3-banlist-ifconfig-file",
        "repo_name": "3v3 Tag Duel banlist",
        "repo_path": "./repositories/3v3-lflist",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    }
]
everchanging = [
    {
        "url": "https://github.com/NoLegs1/everchanging",
        "repo_name": "Everchanging banlist",
        "repo_path": "./repositories/everchanging",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    }
]
rogues = [
    {
        "url": "https://github.com/ARadGoat/Rogues-Format-Banlist-File",
        "repo_name": "Rogues banlist",
        "repo_path": "./repositories/rogues",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    }
]
sleipnir = [
    {
        "url": "https://github.com/eej4105/Sleipnir-Yugioh",
        "repo_name": "Sleipnir banlist",
        "repo_path": "./repositories/sleipnir",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    }
]
acg = [
    {
        "url": "https://github.com/Contrax111/ACG-Banlist",
        "repo_name": "ACG banlist",
        "repo_path": "./repositories/ACG",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    }
]
repo_list = [garbo,trinity,_25th,_3v3,everchanging,rogues,sleipnir,acg]

#_____________________________________________________________________________________________________________________________________________________

ff_server = {
    "name": "EU Central (Format Friends v4)",
    "address": "89.168.36.10",
    "duelport": 5003,
    "roomaddress": "89.168.36.10",
    "roomlistport": 7081
}

#_____________________________________________________________________________________________________________________________________________________

def callback(url):
    webbrowser.open_new(url)

def select_folder():    
    folder = fd.askdirectory(
        title='Select your ProjectIgnis folder',
        initialdir='C:')
    
    if folder != "":
        open_button['text'] = folder

def Install(edo_path):
    if edo_path != "Select ProjectIgnis folder":
        print("installing to: " + edo_path)
        with open(edo_path+"/config/configs.json", 'w') as config_local:
            for i in range(len(repo_list)):
                if checktab[i].get() == 1:
                    for j in range(len(repo_list[i])):
                        print("installing repo: "+repo_list[i][j]["repo_name"])
                        repos.append(repo_list[i][j])
            if checktab[i+1].get() == 1:
                print("installing Format Friends server")
                servers.append(ff_server)
            json.dump(config_data, config_local, indent=4)
        install_button['text'] = "Done!"
        install_button["state"] = "disabled"
        print("Done!")
    else:
        warning = tkinter.Label(window, text = "Choose an installation path!", font=("Arial", 13), fg='#f00')
        warning.pack()

#_____________________________________________________________________________________________________________________________________________________

window = tkinter.Tk()
window.geometry('500x450+700+300')
window.title("Format Friends installer for Edopro")

info = tkinter.Label(window, text = "Thank you for using the Format Friends installer!", font=("Arial", 16))
info.pack()

info = tkinter.Label(window, text = "Tick the features you want applied", font=("Arial", 14))
info.pack()

checktab = []
Button = []
for i in range(len(repo_list)):
    checktab.append(tkinter.IntVar())
    Button.append(tkinter.Checkbutton(window, text = repo_list[i][0]["repo_name"], cursor="hand2", font=("Arial", 12), variable = checktab[i], onvalue = 1, offvalue = 0))
    Button[i].pack()

checktab.append(tkinter.IntVar())
Button.append(tkinter.Checkbutton(window, text = "Format Friends online server", cursor="hand2", font=("Arial", 14), variable = checktab[i+1], onvalue = 1, offvalue = 0))
Button[i+1].pack()

open_button = tkinter.Button(window, text='Select ProjectIgnis folder', cursor="hand2", font=("Arial", 13), command=select_folder)
open_button.pack()

install_button = tkinter.Button(window, text="Install", cursor="hand2", font=("Arial", 16), command=lambda: Install(open_button['text']))
install_button.pack()

kofi = tkinter.Label(window, text="Support us on Ko-fi <3", cursor="hand2", font=("Arial", 10), fg='#36C')
kofi.pack()
kofi.bind("<Button-1>", lambda e: callback("https://ko-fi.com/zefile"))

window.mainloop()