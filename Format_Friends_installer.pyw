import tkinter as tk
from tkinter import ttk, PhotoImage, filedialog as fd
from tkinter.messagebox import showinfo
import webbrowser
import json
from urllib.request import urlopen

# Load configuration data from external URLs
config_url = urlopen("https://raw.githubusercontent.com/ProjectIgnis/Distribution/master/config/configs.json")
config_data = json.load(config_url)
repos = config_data['repos']
servers = config_data['servers']

ff_config_url = urlopen("https://raw.githubusercontent.com/Zefile8/Format-Friends/refs/heads/main/Multirole%20server/options.json")
ff_config_data = json.load(ff_config_url)
ff_repos = ff_config_data['repos']
ff_servers = ff_config_data['servers']

# Open a URL in the default web browser
def callback(url):
    webbrowser.open_new(url)

# Function to select the installation folder
def select_folder():
    folder = fd.askdirectory(title='Select your ProjectIgnis folder', initialdir='C:')
    if folder:
        # Ensure the selected folder is the correct one
        if folder.split('/')[-1] != "ProjectIgnis":
            progress_label["text"] = "Please select the 'ProjectIgnis' folder."
        else:
            folder_var.set(folder)
            progress_label["text"] = "Folder selected, waiting for installation."

# Function to install the selected formats and servers
def install(edo_path):
    if edo_path != "Select ProjectIgnis folder":
        # Count the number of checkboxes that are ticked
        total_selected = sum(var.get() for var in check_vars)

        print("Installing to:", edo_path)
        with open(f"{edo_path}/config/configs.json", 'w') as config_local:
            progress = 0  # Initialize progress counter
            progress_bar["value"] = 0  # Reset progress bar

            i = 0
            # Process selected repositories
            for format_name in ff_repos:
                if check_vars[i].get() == 1:
                    for repo in ff_repos[format_name]:
                        print("Installing repo:", repo["repo_name"])
                        repos.append(repo)
                    progress += 1
                    progress_bar["value"] = (progress / total_selected) * 100
                    window.update_idletasks()
                i += 1

            # Process selected servers
            for server_name in ff_servers:
                if check_vars[i].get() == 1:
                    for server in ff_servers[server_name]:
                        print("Installing server:", server["name"])
                        servers.append(server)
                    progress += 1
                    progress_bar["value"] = (progress / total_selected) * 100
                    window.update_idletasks()
                i += 1

            # Save the updated configuration to the local file
            json.dump(config_data, config_local, indent=4)

        install_button["text"] = "Done!"
        install_button["state"] = "disabled"
        progress_label["text"] = "Installation complete!"
        print("Done!")
    else:
        showinfo("Warning", "Please select the installation path!")

# Create the main application window
window = tk.Tk()
window.title("Format Friends Installer for Edopro v2.0.1.4")
window.geometry("800x650")

# Center the window on the screen
window.update_idletasks()  # Ensure geometry is accurate
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 800
window_height = 650
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Load the custom icon
# icon = PhotoImage(file="trans_smoke_ball_download.ico")
# window.iconphoto(True, icon)

# Configure styling for the widgets
style = ttk.Style(window)
style.theme_use("clam")  # Use a modern theme
style.configure("TLabel", font=("Segoe UI", 12), background="#f0f0f0")
style.configure("TButton", font=("Segoe UI", 12), padding=5)
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabelframe", background="#f0f0f0", font=("Segoe UI", 12, "bold"))
style.configure("TLabelframe.Label", background="#f0f0f0")
style.configure("TProgressbar", troughcolor="#d9d9d9", background="#0078d7")
style.configure("TCheckbutton", background="#f0f0f0", font=("Segoe UI", 11))

# Main frame for the content
main_frame = ttk.Frame(window, padding="10")
main_frame.pack(fill="both", expand=True)

# Header labels
info_label = ttk.Label(main_frame, text="Format Friends Installer", font=("Segoe UI", 16, "bold"), foreground="#0078d7", background="#f0f0f0")
info_label.pack(pady=(0, 10))
sub_label = ttk.Label(main_frame, text="Select formats and server to install:", font=("Segoe UI", 14), background="#f0f0f0")
sub_label.pack()
sub_label_info = ttk.Label(main_frame, text="(Unticked formats will be uninstalled. Running Install with no formats ticked will remove all formats.)", font=("Segoe UI", 10), foreground="#555", background="#f0f0f0")
sub_label_info.pack()

# Labelframe for format options
format_frame = ttk.Labelframe(main_frame, text="Available Formats:", padding="10")
format_frame.pack(fill="both", expand=True, pady=(10, 0))

# Scrollable frame for format options
format_canvas = tk.Canvas(format_frame, background="#f0f0f0")
format_scrollbar = ttk.Scrollbar(format_frame, orient="vertical", command=format_canvas.yview)
format_scrollable_frame = ttk.Frame(format_canvas)

# Update scroll region dynamically
format_scrollable_frame.bind(
    "<Configure>", lambda e: format_canvas.configure(scrollregion=format_canvas.bbox("all"))
)

format_canvas.create_window((0, 0), window=format_scrollable_frame, anchor="nw")
format_canvas.configure(yscrollcommand=format_scrollbar.set)
format_canvas.pack(side="left", fill="both", expand=True)
format_scrollbar.pack(side="right", fill="y")

# Create checkboxes for each format
check_vars = []
for format_name in ff_repos:
    var = tk.IntVar()
    check_vars.append(var)
    ttk.Checkbutton(format_scrollable_frame, text=ff_repos[format_name][0]["repo_name"], variable=var).pack(anchor="w")

# Create server checkboxes directly below format section
server_label = ttk.Label(main_frame, text="Server:", font=("Segoe UI", 10), background="#f0f0f0")
server_label.pack(pady=(0, 0), anchor="w")

for server_name in ff_servers:
    var = tk.IntVar()
    check_vars.append(var)
    ttk.Checkbutton(main_frame, text=f"{ff_servers[server_name][0]['name']} online server", variable=var).pack(anchor="w", padx=(20, 0))

# Separator between sections
separator = ttk.Separator(main_frame, orient="horizontal")
separator.pack(fill="x", pady=(10, 10))

# Folder selection widgets
folder_var = tk.StringVar(value="Select ProjectIgnis folder")
folder_frame = ttk.Frame(main_frame)
folder_frame.pack(fill="x", pady=(10, 0))

folder_label = ttk.Label(folder_frame, textvariable=folder_var, relief="sunken", background="#f0f0f0")
folder_label.pack(side="left", fill="x", expand=True, padx=(0, 5))
select_button = ttk.Button(folder_frame, text="Browse...", command=select_folder)
select_button.pack(side="right")

# Progress bar and label for installation
progress_bar = ttk.Progressbar(main_frame, orient="horizontal", mode="determinate", length=400)
progress_bar.pack(pady=(10, 5))
progress_label = ttk.Label(main_frame, text="Waiting for folder selection.", font=("Segoe UI", 10), foreground="#555", background="#f0f0f0")
progress_label.pack()

# Buttons for actions
bottom_frame = ttk.Frame(main_frame)
bottom_frame.pack(fill="x", pady=(10, 0))

install_button = ttk.Button(bottom_frame, text="Install", command=lambda: install(folder_var.get()))
install_button.pack(side="right", padx=(5, 0))

close_button = ttk.Button(bottom_frame, text="Exit", command=window.destroy)
close_button.pack(side="right", padx=(5, 5))

# Ko-fi support link
kofi_label = ttk.Label(main_frame, text="Support us on Ko-fi <3", foreground="#0078d7", cursor="hand2", background="#f0f0f0")
kofi_label.pack(pady=(10, 0))
kofi_label.bind("<Button-1>", lambda e: callback("https://ko-fi.com/zefile"))

# Finalize scroll region after packing
window.update_idletasks()
format_canvas.configure(scrollregion=format_canvas.bbox("all"))

# Start the main application loop
window.mainloop()
