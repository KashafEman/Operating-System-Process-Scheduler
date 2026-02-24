from PIL import Image, ImageSequence, ImageTk
import tkinter as tk
import customtkinter as ctk
import subprocess
import sys
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import sqlite3

app=ctk.CTk()
app.geometry("1100x630+45+1")
app.resizable(False, False)
app.configure(fg_color="#002244")
gifImage = "CEP\\runAlgo.gif"
openImage = Image.open(gifImage)
frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(openImage)]

count = 0
showAnimation = None
is_playing = True  # Flag to control animation

# Load an image of equipment----------------------------------------------------------------------------------------------------------
my_image = ctk.CTkImage(
        light_image=Image.open("CEP\icons8-fast-forward-64.png"),
        dark_image=Image.open("CEP\icons8-fast-forward-64.png"),
        size=(12, 24),
    )

# Function to normalize and calculate performance score




def animation():
    global count, showAnimation, is_playing
    if is_playing:
        gif_Label.configure(image=frames[count])
        count += 1
        if count == len(frames)-2:
            is_playing = False

            def on_option_select(choice):
                
                if choice == "FCFS":
                    app.destroy()
                    subprocess.run([sys.executable, 'CEP\fcfs.py'])

                elif choice == "SJF":
                    app.destroy()
                    subprocess.run([sys.executable, 'CEP\sjf2.py'])

                elif choice == "MQS":
                    app.destroy()
                    subprocess.run([sys.executable, 'CEP\MQS2.py'])

                elif choice == "PS":
                    app.destroy()
                    subprocess.run([sys.executable, 'CEP\PS2.py'])

                elif choice == "RR":
                    app.destroy()
                    subprocess.run([sys.executable, 'CEP\RR2.py'])

                elif choice == "Run All (preferred)":
                    app.destroy()
                    subprocess.run([sys.executable, 'CEP\evaluation.py'])

                else:
                    print("wrong option you are crazy so get lost")


            # Add a dropdown menu
            options = ["FCFS", "SJF", "MQS","PS","RR","Run All (preferred)"]
            selected_option = tk.StringVar()
            selected_option.set(options[0])  # Set default option

            dropdown_menu = ctk.CTkOptionMenu(gif_Label,width=250,height=65, variable=selected_option, values=options, fg_color="#F64A8A",bg_color="#ffffff",corner_radius=50, button_color="#662d91",dropdown_fg_color="#F64A8A",button_hover_color="#cb6ce6",dropdown_hover_color="#662d91",command=on_option_select)
            dropdown_menu.place(relx=0.3, rely=0.5, anchor="center")


            def simulate():
                app.destroy()
                subprocess.run([sys.executable, 'CEP\EnterFile.py'])

            simulate_button=ctk.CTkButton(gif_Label,width=12,height=24,image=my_image,text="", corner_radius=50, fg_color="#F64A8A",bg_color="#ffffff", hover_color="#662d91",command=simulate)#cb6ce6
            simulate_button.place(relx=0.93, rely=0.118, anchor="center")

            

            

            
            
        else:
            showAnimation = app.after(50, animation)

    

# Set the size of the label to the size of the first frame
gif_Label = tk.Label(app, image=frames[0])
gif_Label.place(x=0, y=0, width=frames[0].width(), height=frames[0].height())





animation()



app.mainloop()