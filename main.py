from tkinter import *
import time
import webbrowser
import tkinter.messagebox as msg

'''driver code for home page'''
root = Tk()
root.geometry("1265x670")
root.title(" Password Generator | Home ")
root.wm_iconbitmap("icons/home.ico")
bg = PhotoImage(file="images/bg.png")
bg_label = Label(root, image=bg)
bg_label.pack()
# root.config(background="#0f111a")

'''Instagram Linker'''
def insta():
    url = "https://www.instagram.com/tanishq._11/"
    webbrowser.open_new(url)

'''Linkedin Linker'''
def linkedin():
    url = "https://www.linkedin.com/in/tanish-gupta-85a440211/"
    webbrowser.open_new(url)

'''Check For update function'''
def checkup():
    status.set("Checking For Updates...")
    sbar.update()
    time.sleep(2)
    status.set("")
    msg.showinfo("Password Generator","There are currently no updates available")

'''About Function'''
def about():
    msg.showinfo("About","password generator : \n\n\n\nLanguage : Python\n\nDeveloped at : ITM GOI\n\nDevelopment year : 2022\n\nInstructed By : Dr. Jitendra Singh Kushwah\n\nDeveloped By : Tanish Gupta")


Label(text="Welcome To Password Generator",background="#010e1f",fg="#5e8598", font="Algerian 45").place(x = 140,y=10)
# Modern
# Consolas
# Constantia
# Castellar
# Forte
# Algerian
# Chiller
# Harrington

'''Menu of the Interface'''
menubar = Menu(root)
help = Menu(menubar,tearoff=0)
help.add_command(label="Check for Updates...", command=checkup)
help.add_separator( )
help.add_command(label="About",command=about)
menubar.add_cascade(label="Help",menu=help)
menubar.add_cascade(label="Exit",command=quit)
root.config(menu = menubar)

'''Button for starting password generating process'''
start_btn = PhotoImage(file='images/start_button.png')
my_btn3 = Button(root, image=start_btn,border=0,background="#107ba6",cursor="hand2", command=lambda:gen(root))
my_btn3.place(x = 610, y = 320)

'''Function to link with main gui'''
def gen(root):
    root.destroy()
    import guipassgen

'''Instagram Button'''
insta_btn = PhotoImage(file='images/instagram.png')
my_btn2 = Button(root, image=insta_btn,borderwidth=0,background="#013464",cursor="hand2", command=insta)
my_btn2.place(x = 1175, y = 635)

'''Linkedin Button'''
linkedin_btn = PhotoImage(file='images/linkedin.png')
my_btn3 = Button(root, image=linkedin_btn,borderwidth=0,background="#013464",cursor="hand2", command=linkedin)
my_btn3.place(x = 1225, y = 635)

'''status bar'''
status = StringVar()
status.set("")
sbar = Label(root,textvariable=status,width=120,background="#0f111a",fg="grey",font="comicsans 9")
sbar.pack(side=BOTTOM,anchor=NW)

root.resizable(False,False)
root.mainloop()