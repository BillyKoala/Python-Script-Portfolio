"""
Author: Billy Knight - February 2022.

This is a small learning project to create a form,
type into a textbox and have it read back to you.
"""
from tkinter import *
import pyttsx3

def talk(): 

    engine = pyttsx3.init()
    engine.say(speech_text.get())
    engine.runAndWait()
    speech_text.delete(0, END) 

try: 
    # Define a GUI for the user to key text into.
    root = Tk()
    root.title('Text To Speech')
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.resizable(False, False)
    # root.iconbitmap("images/favicon.ico")

    # Define variables for the window and screen sizes.
    window_width = 433
    window_height = 180
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    """ 
    Calculate the x and y coordinates for placing 
    this parent window in the centre of the screen. 
    """
    x_coord = (screen_width / 2) - (window_width / 2)
    y_coord = (screen_height / 2) - (window_height / 2)
    # Place the window in the centre of the screen.
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord)) 

    # Define the look of the game window.
    root.title = "Speech To Text"
    root.configure(width=window_width, height=window_height, bg="blue")
    speech_label = Label(root, text="Type In Text To Be Read", relief="raised", bg="orange", font=("Arial Black", 12))
    speech_label.pack(pady=20, padx=20)
    speech_text = Entry(root, relief="ridge", font=("Arial Black", 12), fg="red")
    speech_text.pack(pady=10, padx=50)
    speech_text.focus_set()
    talk_btn = Button(root, text="Talk", relief="groove", fg="green", font=("Arial Black", 14), command=talk)
    talk_btn.pack(pady=20)

    root.mainloop() 

except Exception as e: 

    print(e) 

finally: 

    pass 