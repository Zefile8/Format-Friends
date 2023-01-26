import tkinter
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import webbrowser
import json
from urllib.request import urlopen
config_url = urlopen("https://raw.githubusercontent.com/ProjectIgnis/Distribution/master/config/configs.prod.json")
config_data = json.load(config_url)
repos = config_data['repos']
servers = config_data['servers']

#_____________________________________________________________________________________________________________________________________________________

repo_list = [
    {
        "url": "https://github.com/Zefile8/Garbo-lflist",
        "repo_name": "Garbo banlist",
        "repo_path": "./repositories/Garbo-lflist",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    },
    {
        "url": "https://github.com/Ejeffers1239/TrinityList",
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
    },
    {
        "url": "https://github.com/Ejeffers1239/KuchenLists",
        "repo_name": "Kuchen banlists",
        "repo_path": "./repositories/KuchenLISTS",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    },
    {
        "url": "https://github.com/thespideroi/25thLFlist",
        "repo_name": "25th Forbidden & Limited Card banlist",
        "repo_path": "./repositories/25thlflist",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    },
    {
        "url": "https://github.com/diamonddudetcg/format_friends",
        "repo_name": "Common Charity & Disco Inferno banlists",
        "repo_path": "./repositories/CommonDiscoLISTS",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    },
    {
        "url": "https://github.com/Bewilderer/3v3-banlist-ifconfig-file",
        "repo_name": "3v3 Tag Duel banlist",
        "repo_path": "./repositories/3v3-lflist",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    },
    {
        "url": "https://github.com/NoLegs1/everchanging",
        "repo_name": "Everchanging banlist",
        "repo_path": "./repositories/everchanging",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    },
    {
        "url": "https://github.com/ARadGoat/Rogues-Format-Banlist-File",
        "repo_name": "Rogues banlist",
        "repo_path": "./repositories/rogues",
        "lflist_path": ".",
        "should_update": True,
        "should_read": True
    }
]

#_____________________________________________________________________________________________________________________________________________________

ff_server = {
    "name": "EU Central (Format Friends)",
    "address": "13.39.76.61",
    "duelport": 5003,
    "roomaddress": "13.39.76.61",
    "roomlistport": 7081
}

#_____________________________________________________________________________________________________________________________________________________

def callback(url):
    webbrowser.open_new(url)

def select_file():
    filetypes = (
        ('json files', '*.json'),
        ('All files', '*.*')
    )
    
    filename = fd.askopenfilename(
        title='Open your configs.json file',
        initialdir='C:\ProjectIgnis\config',
        filetypes=filetypes)
    
    if filename != "":
        open_button['text'] = filename

def Install(config_path):
    if open_button['text'] != "Select Configs.json path":
        print("installing to: " + open_button['text'])
        with open(config_path, 'w') as config_local:
            count = 0
            for i in range(len(repo_list)):
                if checktab[i].get() == 1:
                    print("installing format: "+repo_list[i]["repo_name"])
                    repos.append(repo_list[i])
                    count = count+1
            if count > 0:
                servers.append(ff_server)
            json.dump(config_data, config_local, indent=4)
        install_button['text'] = "Done!"
        install_button["state"] = "disabled"
        print("Done!")
    else:
        warning = tkinter.Label(window, text = "Choose an installation path!", font=("Arial", 13), fg='#f00')
        warning.pack()

window = tkinter.Tk()
window.geometry('500x450+700+300')
window.title("Format Friends installer for Edopro")

info = tkinter.Label(window, text = "Tick the formats you want to install", font=("Arial", 16))
info.pack()

checktab = []
Button = []
for i in range(len(repo_list)):
    checktab.append(tkinter.IntVar())
    Button.append(tkinter.Checkbutton(window, text = repo_list[i]["repo_name"], cursor="hand2", font=("Arial", 11), variable = checktab[i], onvalue = 1, offvalue = 0))
    Button[i].pack()

server_info = tkinter.Label(window, text = "*Server is installed if you tick any format", font=("Arial", 12), fg='#888')
server_info.pack()

open_button = tkinter.Button(window, text='Select Configs.json path', cursor="hand2", font=("Arial", 13), command=select_file)
open_button.pack()

install_button = tkinter.Button(window, text="Install", cursor="hand2", font=("Arial", 16), command=lambda: Install(open_button['text']))
install_button.pack()

kofi = tkinter.Label(window, text="Support us on Ko-fi <3", cursor="hand2", font=("Arial", 10), fg='#36C')
kofi.pack()
kofi.bind("<Button-1>", lambda e: callback("https://ko-fi.com/zefile"))

window.mainloop()