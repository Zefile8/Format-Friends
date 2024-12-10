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

ff_config_url = urlopen("https://raw.githubusercontent.com/Zefile8/Format-Friends/refs/heads/main/Multirole%20server/options.json")
ff_config_data = json.load(ff_config_url)
ff_repos = ff_config_data['repos']
ff_servers = ff_config_data['servers']

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
            i = 0
            for format in ff_repos:
                if checktab[i].get() == 1:
                    for j in range(len(ff_repos[format])):
                        print("installing repo: "+ff_repos[format][j]["repo_name"])
                        repos.append(ff_repos[format][j])
                i += 1
            for server in ff_servers:
                if checktab[i].get() == 1:
                    for j in range(len(ff_servers[server])):
                        print("installing repo: "+ff_servers[server][j]["name"])
                        servers.append(ff_servers[server][j])
                    i += 1
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
window.title("Format Friends installer for Edopro v1.3.2.0")

info = tkinter.Label(window, text = "Thank you for using the Format Friends installer!", font=("Arial", 16))
info.pack()

info = tkinter.Label(window, text = "Tick what you want, untick to uninstall", font=("Arial", 14))
info.pack()

i = 0
checktab = []
Button = []
for format in ff_repos:
    checktab.append(tkinter.IntVar())
    Button.append(tkinter.Checkbutton(window, text = ff_repos[format][0]["repo_name"], cursor="hand2", font=("Arial", 12), variable = checktab[i], onvalue = 1, offvalue = 0))
    Button[i].pack()
    i += 1

for server in ff_servers:
    checktab.append(tkinter.IntVar())
    Button.append(tkinter.Checkbutton(window, text = ff_servers[server][0]["name"]+" online server", cursor="hand2", font=("Arial", 14), variable = checktab[i], onvalue = 1, offvalue = 0))
    Button[i].pack()
    i += 1

open_button = tkinter.Button(window, text='Select ProjectIgnis folder', cursor="hand2", font=("Arial", 13), command=select_folder)
open_button.pack()

install_button = tkinter.Button(window, text="Install", cursor="hand2", font=("Arial", 16), command=lambda: Install(open_button['text']))
install_button.pack()

kofi = tkinter.Label(window, text="Support us on Ko-fi <3", cursor="hand2", font=("Arial", 10), fg='#36C')
kofi.pack()
kofi.bind("<Button-1>", lambda e: callback("https://ko-fi.com/zefile"))

window.mainloop()