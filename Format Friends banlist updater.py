import tkinter
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import webbrowser
import json
import time
from urllib.request import urlopen
import string
import re

#_____________________________________________________________________________________________________________________________________________________

def callback(url):
    webbrowser.open_new(url)

def select_file():
    filetypes = (
        ('lflist files', '*.lflist.conf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Select your banlist file',
        filetypes=filetypes)

    if filename != "":
        list_button['text'] = filename

def select_folder():    
    folder = fd.askdirectory(
        title='Select your ProjectIgnis folder',
        initialdir='C:')
    
    if folder != "":
        open_button['text'] = folder

def update_banlist(edo_path,list_path):
    if (open_button['text'] != "Select Edopro folder" and list_button['text'] != "Select .lflist.conf file"):
        if True:#if all files found
            print("\nupdating from: " + open_button['text'])
            #get banlist to edit
            with open(list_path, 'r') as list:
                list_data = list.read()
            #info vars
            mod_amount = {
                -1: 0,
                0: 0,
                1: 0,
                2: 0,
                3: 0
            }
            
            #comment
            comments = {
                0: "#forbidden",
                1: "#limited",
                2: "#semi-limited",
                3: "#unlimited"
            }
            #decklists
            decklists = {
                -1: edo_path + "/deck/¤Banlist - removed.ydk",
                0: edo_path + "/deck/¤Banlist - to 0.ydk",
                1: edo_path + "/deck/¤Banlist - to 1.ydk",
                2: edo_path + "/deck/¤Banlist - to 2.ydk",
                3: edo_path + "/deck/¤Banlist - to 3.ydk"
            }
            
            #modify to 0-3
            for i in range(4):
                f = open(decklists[i])
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
                        list_data = list_data.replace(comments[i], comments[i]+"\n"+id[0]+" "+str(i), 1)
                        mod_amount[i] = mod_amount[i]+1
            
            #modify remove
            f = open(decklists[-1])
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
                    mod_amount[-1] = mod_amount[-1]+1
            
            #export modified
            with open(list_path, 'w') as list:
                list.write(list_data)
            
            #report changes
            print("\n")
            print("nb removed: "+str(mod_amount[-1]))
            print("nb banned: "+str(mod_amount[0]))
            print("nb limited: "+str(mod_amount[1]))
            print("nb semi: "+str(mod_amount[2]))
            print("nb unlimited: "+str(mod_amount[3]))
            print("\n")
            print("Done!")
            update_button['text'] = "Done!"
            update_button["state"] = "disabled"
        else:
            warning = tkinter.Label(window, text = "Files missing!", font=("Arial", 13), fg='#f00')
            warning.pack()
    else:
        warning = tkinter.Label(window, text = "Select Edopro path and lflist file!", font=("Arial", 13), fg='#f00')
        warning.pack()

def update_mappings(edo_path,list_path):
    if (open_button['text'] != "Select Edopro folder" and list_button['text'] != "Select .lflist.conf file"):
        if True:#if all files found
            print("\nupdating from: " + open_button['text'])
            map_name = edo_path + "/repositories/delta-bagooska/mappings.json"
            edits = 0
            with open(map_name) as map_file:
                map_data = json.load(map_file)
                mappings = map_data['mappings']
                for old, new in mappings:
                    oldstr = str(old)
                    newstr = str(new)
                    with open(list_path, 'r') as list:
                            list_data = list.read()
                    list_data_new = list_data.replace(oldstr, newstr)
                    if list_data != list_data_new:
                        edits=edits+1
                        with open(list_path, 'w') as list:
                            list.write(list_data_new)

            print("\nid updates: " + str(edits)+"\n")
            print("Done!")
            mappings_button['text'] = "Done!"
            mappings_button["state"] = "disabled"
        else:
            warning = tkinter.Label(window, text = "Files missing!", font=("Arial", 13), fg='#f00')
            warning.pack()
    else:
        warning = tkinter.Label(window, text = "Select Edopro path and lflist file!", font=("Arial", 13), fg='#f00')
        warning.pack()
#_____________________________________________________________________________________________________________________________________________________

window = tkinter.Tk()
window.geometry('500x200+700+300')
window.title("Format Friends banlist updater for Edopro")

list_button = tkinter.Button(window, text='Select .lflist.conf file', cursor="hand2", font=("Arial", 13), command=select_file)
list_button.pack()

open_button = tkinter.Button(window, text='Select ProjectIgnis folder', cursor="hand2", font=("Arial", 13), command=select_folder)
open_button.pack()

update_button = tkinter.Button(window, text="Update banlist", cursor="hand2", font=("Arial", 16), command=lambda: update_banlist(open_button['text'],list_button['text']))
update_button.pack(pady=10)

mappings_button = tkinter.Button(window, text="Update mappings", cursor="hand2", font=("Arial", 16), command=lambda: update_mappings(open_button['text'],list_button['text']))
mappings_button.pack()

kofi = tkinter.Label(window, text="Support us on Ko-fi <3", cursor="hand2", font=("Arial", 10), fg='#36C')
kofi.pack()
kofi.bind("<Button-1>", lambda e: callback("https://ko-fi.com/zefile"))

window.mainloop()