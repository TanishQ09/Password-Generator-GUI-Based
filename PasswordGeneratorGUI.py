import datetime
import time
import webbrowser
import PasswordMethods
import random
import pyperclip
from tkinter import *
import tkinter.messagebox as msg

'''For fetching current date'''
current_year = datetime.date.today()

'''Function for Processing input and generate password'''
def user_ip():
    username = namevalue.get()
    username1 = username.split(" ")
    username = username.replace(" ","")
    userdate = int(datevalue.get())
    usermonth = int(monthvalue.get())
    useryear = int(yearvalue.get())
    usercontact = contactvalue.get()
    usergender = var.get()
    age = current_year.year-useryear-((current_year.month,current_year.day)<(usermonth,userdate))
    if not username:
        msg.showerror("Blank Field","Name field is empty")
    if (userdate <1  or userdate > 31):
        msg.showerror("Invalid Date", "Date entered is either greater than 31 or less than 1")
    if (usermonth < 1 or usermonth > 12):
        msg.showerror("Invalid Month", "Month entered is either greater than 12 or less than 1")
    if (useryear < 1950 or useryear > current_year.year):
        msg.showerror("Invalid Year", "Input year is Invalid")
    if not usercontact:
        msg.showerror("Blank Field","Contact field is empty")
    if usercontact:
        usercontact = str(usercontact)
        if (len(usercontact) <  10) :
            msg.showerror("Invalid Contact", "Input contact No. is Invalid")
        if (len(usercontact) > 10):
            msg.showerror("Invalid Contact", "Input Contact No. is Invalid")
    if (username != "" and usercontact != "" and usermonth<=12 and usermonth>1 and userdate<=31 and userdate>1 and useryear<=current_year.year and useryear>1950):
        usercontact = int(usercontact)
        rand_choice = random.randint(0,4)
        if(rand_choice == 0):
            r_c2 = random.randint(0,3)
            if(r_c2 == 0):
                num = userdate
            elif(r_c2 == 1):
                num = usermonth
            elif (r_c2 == 2):
                num = useryear
            elif(r_c2 == 3):
                num = age
            passcode = PasswordMethods.name_begin_num(username,num)
            pass_str.set(passcode)
        elif(rand_choice == 1):
            r_c3 = random.randint(0,3)
            if(r_c3 == 0):
                num = userdate
            elif(r_c3 == 1):
                num = usermonth
            elif (r_c3 == 2):
                num = useryear
            elif(r_c3 == 3):
                num = age
            passcode = PasswordMethods.name_mid_num(username, num)
            pass_str.set(passcode)
        elif(rand_choice == 2):
            r_c3 = random.randint(0,3)
            if(r_c3 == 0):
                num = userdate
            elif(r_c3 == 1):
                num = usermonth
            elif (r_c3 == 2):
                num = useryear
            elif(r_c3 == 3):
                num = age
            passcode = PasswordMethods.name_end_num(username, num)
            pass_str.set(passcode)
        elif(rand_choice==3):
            passcode = PasswordMethods.rand_pass_all(name = username,contact = usercontact,age=age,date = userdate,month = usermonth,year = useryear)
            pass_str.set(passcode)
        elif(rand_choice == 4):
            passcode = PasswordMethods.rand_name_symbol(username,userdate)
            pass_str.set(passcode)
        elif(rand_choice == 5):
            r_c4 = random.randint(0,2)
            if(r_c4 == 0):
                n = userdate
            elif(r_c4 == 1):
                n = usermonth
            elif(r_c4 == 2):
                n = age
            passcode = PasswordMethods.Ldig_name_Fdig(username,num)
            pass_str.set(passcode)
        elif(rand_choice == 6):
            r_c5 = random.randint(0,5)
            if(r_c5 == 0):
                num = userdate
                num2 = usermonth
            elif(r_c5 == 1):
                num = userdate
                num2 = age
            elif(r_c5 == 2):
                num = usermonth
                num2 = userdate
            elif(r_c5 == 3):
                num = usermonth
                num2 = age
            elif(r_c5 == 4):
                num = age
                num2 = userdate
            elif(r_c5 == 5):
                num = age
                num2 = usermonth
            passcode = PasswordMethods.Fdig_name_Ldig(username,num,num2)
            pass_str.set(passcode)

'''Instagram Linker'''
def insta():
    url = "https://www.instagram.com/tanishq._11/"
    webbrowser.open_new(url)

'''Linkedin Linker'''
def linkedin():
    url = "https://www.linkedin.com/in/tanish-gupta-85a440211/"
    webbrowser.open_new(url)

'''Copy Function to copy password in clipboard'''
def copy():
    status.set("Copying to clipboard..")
    sbar.update()
    time.sleep(1)
    status.set(" ")
    pyperclip.copy(pass_str.get())

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

def hom(root):
    root.destroy()
    import main

'''Driver Code'''
root = Tk()
root.geometry("1265x670")
root.title(" Password Generator ")
root.wm_iconbitmap("icons/user-lock-solid.ico")
root.config(background="white")

'''Menu of the Interface'''
menubar = Menu(root)
help = Menu(menubar,tearoff=0)
help.add_command(label="Check for Updates...", command=checkup)
help.add_separator( )
help.add_command(label="About",command=about)
menubar.add_cascade(label="Help",menu=help)
menubar.add_cascade(label="Exit",command=quit)
root.config(menu = menubar)

back_btn = PhotoImage(file='images/back.png')
my_btn3 = Button(root, image=back_btn,border=0,background="white",cursor="hand2", command=lambda:hom(root))
my_btn3.place(x = 40, y = 35)

'''System's Main Interface'''
Label(text="Welcome To Password Generator", background="white",fg="black", font="Castellar 35 bold").place(x = 180,y=20)

username = Label(root, text = "Name", background="white",fg="black",font="Forte 16").place(x=460, y = 126)

userdate = Label(root, text= "Date",background="white",fg="black",font="Forte 16").place(x=460, y = 166)

usermonth = Label(root, text = "Month",background="white",fg="black",font="Forte 16").place(x=460, y = 206)

useryear = Label(root, text="Year",background="white",fg="black",font="Forte 16").place(x=460, y = 246)

usercontact = Label(root, text="Contact No. ",background="white",fg="black",font="Forte 16").place(x=460, y = 286)

usergender = Label(root, text = "Gender",background="white",fg="black",font="Forte 16").place(x=460, y = 326)

userpassword = Label(root, text="Your Password is :",background="white",fg="black",font="Forte 16").place(x=460, y = 426)

'''variable declaration for different user inputs'''
var = StringVar()
var.set("Radio")
pass_str = StringVar()
namevalue = StringVar()
datevalue = IntVar()
datevalue.set(current_year.day)
monthvalue = IntVar()
monthvalue.set(current_year.month)
yearvalue = IntVar()
yearvalue.set(current_year.year)
contactvalue = StringVar()

'''Entries to take input from user'''
nameentry = Entry(root, textvariable=namevalue,border=0,background="#F6F4F4",fg="black",font="comicsans 16",insertbackground="grey",insertwidth=3).place(x = 680,y=126)

dateentry = Spinbox(root, from_ = 1, to_ =31, textvariable = datevalue,insertbackground="grey",border=0,buttonbackground="white",fg="black",background="#F6F4F4" ,width =18,font="comicsans 16").place(x=680,y=166)

monthentry = Spinbox(root, from_ = 1, to_ =12, textvariable = monthvalue, insertbackground="grey",border=0,buttonbackground="white",fg="black",width =18,background="#F6F4F4",font="comicsans 16").place(x=680,y=206)

yearentry = Spinbox(root, from_ = 1950, to_ =2022, textvariable = yearvalue,insertbackground="grey",border=0,buttonbackground="white",fg="black", background="#F6F4F4",width =18,font="comicsans 16").place(x=680,y=246)

contactentry = Entry(root, textvariable=contactvalue,background="#F6F4F4",insertbackground="grey",fg="black",border=0,font="comicsans 16").place(x=680,y=286)

genderentry = Radiobutton(root, text="Male",background="white",cursor="hand2", fg="black",variable=var, value="M",font="Modern 18 bold",pady=2).place(x =675,y=326)
genderentry = Radiobutton(root, text="Female",background="white",cursor="hand2", fg="black",variable=var, value="F",font="Modern 18 bold",pady=2).place(x= 835, y =326)

'''Password Generating Button'''
Button(text="Generate Password",background="black",cursor="hand2",fg="white",command=user_ip,font="Forte 16").place(x=710,y=376)

'''Refresh Button For Regenerating password from same details'''
ref_btn = PhotoImage(file='images/refresh.png')
my_btn = Button(root, image=ref_btn,background="white",borderwidth=0,cursor="exchange", command=user_ip)
my_btn.place(x = 945, y = 421)

'''Output after generating password'''
Entry(root, textvariable= pass_str,background="#F6F4F4",border=0,fg="grey",font="comicsans 16").place(x=680,y=426)

'''Copy To Clipboard button'''
Button(text="Copy To Clipboard",background="black",cursor="hand2",fg="white",command=copy,font="Forte 14").place(x=720,y=466)

'''Instagram Button'''
insta_btn = PhotoImage(file='images/instagram.png')
my_btn2 = Button(root, image=insta_btn,borderwidth=0,background="white",cursor="hand2", command=insta)
my_btn2.place(x = 1175, y = 635)

'''Linkedin Button'''
linkedin_btn = PhotoImage(file='images/linkedin.png')
my_btn3 = Button(root, image=linkedin_btn,borderwidth=0,background="white",cursor="hand2", command=linkedin)
my_btn3.place(x = 1225, y = 635)

'''Status Bar'''
status = StringVar()
status.set("")
sbar = Label(root,textvariable=status,width=165,background="white",fg="grey",font="comicsans 9")
sbar.pack(side=BOTTOM,anchor=NW)

root.resizable(False,False)
root.mainloop()
