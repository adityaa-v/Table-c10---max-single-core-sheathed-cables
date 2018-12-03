from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class c10(Frame):
    def __init__(self, master):
        master.title("c10")
        master.geometry('600x500+500+500')
        master.configure(background = '#e1d8b9')

        self.style = ttk.Style()

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, text = 'Thanks for Exploring!', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("We're glad you chose Explore California for your recent adventure.  "
                          "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row = 1, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Button(self.frame_content, text = 'Submit',
                   command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear',
                   command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')
        

    def main():            
    
        root = Tk()
        feedback = Feedback(root)
        root.mainloop()

root.mainloop()


