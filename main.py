'''
                                        Source Code for Database Management software
    
    Purpose  : Managing the database for Students in "Students Quality Council"
               To know more about the council "cqm.annauniv.edu".
    
    Developer: Vaasu devan S
               Email:vaasuceg.96@gmail.com
               www.github.com/VaasuDevanS
    
    Started  : 'Fri Jan 20 15:43:57 2017' 
               (Got using datetime.ctime(datetime.now())) LOL :-)
               
    
    modified:  'Tue Jan 24 17:35:09 2017' 
      (last)
      
    Main TimeLine:
    
    1. 'Sat Jan 21 09:15:55 2017' ------ > The Key bindings and Menu bar was created.
    2. 'Sat Jan 21 16:18:08 2017' ------ > Basic Skeleton was created.
    3. 'Sat Jan 21 23:08:59 2017' ------ > Insert new record window was added.
    4. 'Sun Jan 22 12:28:37 2017' ------ > Database was created and Update existing record window was added.
    5. 'Sun Jan 22 19:50:25 2017' ------ > Overall layout was completed for add and update windows.
    6. 'Mon Jan 23 08:37:02 2017' ------ > Results label was added and fixed some bugs in result Display and Gender column was added.
    7. 'Mon Jan 23 17:01:22 2017' ------ > Search result algorithm was added and fixed some bugs in saving the year data.
    8. 'Tue Jan 24 12:54:16 2017' ------ > Photo algorithms were added and made the source code available in GitHub.
    9. 'Tue Jan 24 17:35:09 2017' ------ > Saving results window was added and the project was ready to be exposed. :-)

    Developed using Python 2.7.12 on Windows 8.1 64-bit os
    IDE Used: Wingware python IDE 101 v.5.1.12-1 (Free version).
    
    Copyrights: No copyrights and nothing. Anybody can modify and use it for their own requirements.
    
    converted to .exe using pyinstaller.
    
    viewed best in any text editing software that understands Python particularly in fullscreen(for comments).
    Eg. Python IDLE,Notepad++,notepad2,wingware IDE,Eclipse.
        Notepad(Worst case because it is non-pythonic).
'''

'''
   First things first..Importing all the things that we need...
   Without Modules you can't achieve something great in python.... :-) :-)
'''

# (Built-in)         No Worries
from Tkinter import Tk,Frame,Label,Button,Entry,Listbox,Menu,Scrollbar,OptionMenu,StringVar,BooleanVar,END,Canvas,Radiobutton,Checkbutton,Text,ACTIVE,Toplevel
import tkMessageBox as msgbox
from tkFileDialog import askopenfile,asksaveasfile,askdirectory,asksaveasfilename
from tkFont import Font
from datetime import datetime
import os,shelve,webbrowser
from urllib import urlopen
import re    # re ------> Regular Expressions
import StringIO

# (Third party modules)
''' 
    Third party modules can be downloaded using pip or from the website 
    "http://www.lfd.uci.edu/~gohlke/pythonlibs/"   
    
    (or)
    
    You can download from the repo itself
    
    (or)
    
    pip install PILLOW xlwt
    
'''
from PIL import Image,ImageTk  # PIL---> Python Imaging Library
from xlwt import Workbook

# Module Uses (Quick Glance)
'''

   * Tkinter,tkMessageBox,tkFileDialog,tkFont -------> GUI packages (In python 3, all belong to the same module 'tkinter')
   * datetime                                 -------> date & time (also Year) management
   * OS                                       -------> for creating files and folders
   * shelve                                   -------> for managing the database file (shelve comes to the rescue) 
   * webbrowser                               -------> for opening the webbrowser and displaying the content
   * urllib                                   -------> for checking the internet connection
   * re                                       -------> for string manipulations
   * PIL  (3.4.2)                             -------> for handling images of students  
   * xlwt (1.2.0)                             -------> for saving the data to excel file
   
'''

# Window

app=Tk()    # Creation of GUI class
current_year=str(datetime.now().year)
title="STUDENTS QUALITY COUNCIL Database-"+current_year   #Setting the window Title
app.title(title)
app.resizable(0,0)               # I Don't want the window to be resized. Also it will disable the maximize button
app.geometry("1000x610+200+40")  # width X height + from-left + from-top

vaasu_results=[]

try:
    os.mkdir("D:\\Database")
    msgbox.showinfo("Message",message="Creating Database for the First Time in D: drive. Either you are creating for the First Time or the database is missing...")
except:
    pass

os.chdir("D:\\Database")
database=shelve.open("Database.sqc")       # Opening the Connection between the database file and the program

#img=Image.open("D:\Program_Files\Python\Database_Management_Software\icon.ico")
#database['icon']=img.tobytes()

#img=Image.open("D:\Program_Files\Python\Database_Management_Software\default_image.png").convert('L').resize((128,128))
#database['default_image']=img.tobytes()

icon=Image.frombytes("RGBA",(256,256),database['icon'])
im=ImageTk.PhotoImage(icon)
app.tk.call('wm','iconphoto',app._w,im)

def clear(): # Control+l or Control+L function
    text_box.delete(0,END)
    list_box.delete(0,END)
    reg_var.set("")
    name_var.set("")
    dept_var.set("")
    con_var.set("")
    mail_var.set("")
    native_var.set("")
    hds_var.set("")
    au_var.set("")
    a_b_var.set("")
    b_c_var.set("")
    c_d_var.set("")
    d_e_var.set("")
    other_info.config(state="normal")
    other_info.delete("1.0",END)
    blood_var.set("")
    dob_var.set("")
    text_box.focus_force()
    found_var.set("Found")
    adv.config(state="disable")
    update.config(state="disable")
    delete.config(state="disable")
    img=Image.frombytes("L",(128,128),database['default_image'])
    avata=ImageTk.PhotoImage(img)
    avatar_label=Label(canvas1,image=avata)
    avatar_label.image=avata
    avatar_label.place(x=340,y=17)    
    
def save_result():
    
    '''
       To save the results to excel file
       
    '''
    
    def names():
        
        book=Workbook()
        sheet1=book.add_sheet("Sheet1")
        
        row=sheet1.row(1)
        row.write(1,"Reg_nos") 
        row.write(2,"Name")
        
        vresults=vaasu_results[1]
        YY=[i for i in database if i.isdigit()]
        
        for j,i in enumerate(vresults,start=4):
            row=sheet1.row(j)
            for k in YY:
                if database[k]["name"]==i:
                    my_no=k   
                    break
            try:
                
                row.write(1,my_no)
                row.write(2,i)
                del my_no
                
            except:row.write(0,i)

        file_name=asksaveasfilename(title="Enter only file name..")
        
        if file_name:
            if not file_name.endswith('.xls'):
                book.save(file_name+".xls")
            else:
                book.save(file_name)
            msgbox.showinfo("Success",message="Saved Successfully..")
            
        else:
            pass
        
        save.focus_force()

    def all_details():
        
        book=Workbook()
        sheet1=book.add_sheet("Sheet1")
        
        row=sheet1.row(1)
        row.write(1,"Reg_nos") 
        row.write(2,"Name")
        row.write(3,"Contact")
        row.write(4,"Email")
        row.write(5,"Department")
        row.write(6,"Native")
        row.write(7,"Hosteller/Days-scholar")
        row.write(8,"Date of Birth")
        row.write(9,"Blood Group")
        row.write(10,"First_year")
        row.write(11,"Second_year")
        row.write(12,"Third_year")
        row.write(13,"Fourth_year")
        row.write(14,"Other")
        
        vresults=vaasu_results[1]
        YY=[i for i in database if i.isdigit()]
        
        for j,i in enumerate(vresults,start=4):
            row=sheet1.row(j)
            for k in YY:
                if database[k]["name"]==i:
                    my_no=k   
                    break
            try:
                
                row.write(1,my_no)
                row.write(2,i)
                row.write(3,database[my_no]['contact'])
                row.write(4,database[my_no]['email'])
                row.write(5,database[my_no]['dept'])
                row.write(6,database[my_no]['native'])
                row.write(7,database[my_no]['hos_days'])
                row.write(8,database[my_no]["dob"])
                row.write(9,database[my_no]["blood"])
                row.write(10,database[my_no]["year"]["1"].values())
                row.write(11,database[my_no]["year"]["2"].values())
                row.write(12,database[my_no]["year"]["3"].values())
                row.write(13,database[my_no]["year"]["4"].values())
                row.write(14,database[my_no]["other"])
                              
                del my_no
                
            except:row.write(0,i)

        file_name=asksaveasfilename(title="Enter only file name..")
        
        if file_name:
            if not file_name.endswith('.xls'):
                book.save(file_name+".xls")
            else:
                book.save(file_name)
            msgbox.showinfo("Success",message="Saved Successfully..")
            
        else:
            pass
        
        save.focus_force()                
    
    def no_email():
        
        book=Workbook()
        sheet1=book.add_sheet("Sheet1")
        
        row=sheet1.row(1)
        row.write(1,"Reg_nos") 
        row.write(2,"Name")
        row.write(3,"Contact")
        row.write(4,"Email")
        
        vresults=vaasu_results[1]
        YY=[i for i in database if i.isdigit()]
        
        for j,i in enumerate(vresults,start=4):
            row=sheet1.row(j)
            for k in YY:
                if database[k]["name"]==i:
                    my_no=k   
                    break
            try:
                
                row.write(1,my_no)
                row.write(2,i)
                row.write(3,database[my_no]['contact'])
                row.write(4,database[my_no]['email'])
                del my_no
                
            except:row.write(0,i)

        file_name=asksaveasfilename(title="Enter only file name..")
        
        if file_name:
            if not file_name.endswith('.xls'):
                book.save(file_name+".xls")
            else:
                book.save(file_name)
            msgbox.showinfo("Success",message="Saved Successfully..")
            
        else:
            pass
        
        save.focus_force()        
    
    save=Toplevel()
    save.resizable(0,0)
    save.title("Default with Reg No..!")
    
    icon=Image.frombytes("RGBA",(256,256),database['icon'])
    im=ImageTk.PhotoImage(icon)    
    save.tk.call('wm','iconphoto',save._w,im)  
    
    save.geometry("300x105+220+470")
    save.focus_force()
    
    all_details=Button(save,text="Save all Results..",command=all_details)
    all_details.place(x=0,y=5,width=300)
    
    no_email=Button(save,text="Save Mob number and email id..",command=no_email)
    no_email.place(x=0,y=40,width=300)
    
    names=Button(save,text="Names..",command=names)
    names.place(x=0,y=75,width=300)
        
    flag=save.bind("<Escape>",lambda *ignore:save.destroy())
    
    save.mainloop()

def add_record():
    '''
       This function will make the new records save to the database.
    
    '''
    def clear_func():
        reg_box.delete(0,END)
        name_box.delete(0,END)
        dept_box.delete(0,END)
        contact_box.delete(0,END)
        mail_box.delete(0,END)
        native_box.delete(0,END)
        a_b_box.delete(0,END)
        b_c_box.delete(0,END)
        c_d_box.delete(0,END)
        d_e_box.delete(0,END)
        reg_box.focus_force()
        blood_box.delete(0,END)
        dob_box.delete(0,END)
        other.delete("1.0",END)
        hos_day.set(None)
        m_f.set(None)
        act_unact.set(None)
        im=Image.frombytes("L",(128,128),database['default_image'])
        avata=ImageTk.PhotoImage(im)
        avatar_label=Label(add,image=avata)
        avatar_label.image=avata
        avatar_label.place(x=340,y=10,height=80)         
    
    def save_record():
        
        if len(name_box.get())!=0 and len(dept_box.get())!=0 and len(contact_box.get())!=0 and len(reg_box.get())!=0:
            
            otherrr=re.sub("\n","",other.get("1.0",END))
            data={"name":name_box.get(),"dept":dept_box.get(),"contact":contact_box.get(),"email":mail_box.get(),"native":native_box.get(),"other":otherrr,"image":[str(to_bytes_mode.get()),str(to_bytes.get())],"gender":m_f.get(),"act_unact":act_unact.get(),"hos_days":hos_day.get(),"dob":dob_box.get(),"blood":blood_box.get(),"year":{"1":{a_b_va.get():a_b_box.get()},"2":{b_c_va.get():b_c_box.get()},"3":{c_d_va.get():c_d_box.get()},"4":{d_e_va.get():d_e_box.get()}}}
            
            database[reg_box.get()]=data
            
            msgbox.showinfo("Confirmation..",message="Saved to the Database")
            clear_func()
            
        else:
            msgbox.showerror("Error",message="Fields can't be empty.")
            add.focus_force()
    
    add=Toplevel()
    add.geometry("500x445+645+142")
    add.title("Insert new record")
    
    def Add_Image():
        
        myFormats=[('JPEG / JFIF','*.jpg'),('Portable Network Graphics','*.png'),('Windows Bitmap','*.bmp'),]
        path=askopenfile(title="Open Image",filetypes=myFormats) 
        add.focus_force()

        try:
        
            client=Image.open(path.name).resize((128,128),Image.ANTIALIAS)
            to_bytes_mode.set(str(client.mode))
            to_bytes.set(client.tobytes())
            
            avata=ImageTk.PhotoImage(client)
            avatar_label=Label(add,image=avata)
            avatar_label.image=avata
            avatar_label.place(x=340,y=10,height=80)             
            
        except:
            pass
            
    canvas1=Canvas(add,width=600,height=550)
    
    regno=Label(canvas1,text="Reg No")
    regno.place(x=20,y=15)
    
    reg_box=Entry(canvas1)
    reg_box.place(x=100,y=15)
    
    reg_box.focus_force()
    
    icon=Image.frombytes("RGBA",(256,256),database['icon'])
    im=ImageTk.PhotoImage(icon)    
    add.tk.call('wm','iconphoto',add._w,im)
        
    im=Image.frombytes("L",(128,128),database['default_image'])
    avata=ImageTk.PhotoImage(im)
    avatar_label=Label(add,image=avata)
    avatar_label.image=avata
    avatar_label.place(x=340,y=10,height=80) 
    
    to_bytes=StringVar(canvas1)
    to_bytes_mode=StringVar(canvas1)
    
    to_bytes.set(database['default_image'])
    to_bytes_mode.set("L")

    img_butt=Button(canvas1,text="Add Image",command=Add_Image)
    img_butt.place(x=370,y=100)
        
    name=Label(canvas1,text="Name")
    name.place(x=20,y=50)
    
    name_box=Entry(canvas1)
    name_box.place(x=100,y=50)
        
    dept=Label(canvas1,text="Department")
    dept.place(x=20,y=85)
    
    dept_box=Entry(canvas1)
    dept_box.place(x=100,y=85,width=175)
    
    contact=Label(canvas1,text="Contact")
    contact.place(x=20,y=120)
    
    contact_box=Entry(canvas1)
    contact_box.place(x=100,y=120)
    
    blood=Label(canvas1,text="Blood Group")
    blood.place(x=230,y=120)
    
    blood_box=Entry(canvas1)
    blood_box.place(x=310,y=120,width=30)
    
    mail=Label(canvas1,text="E-Mail Id")
    mail.place(x=20,y=155)
    
    mail_box=Entry(canvas1)
    mail_box.place(x=100,y=155,width=175)
    
    native=Label(canvas1,text="Native")
    native.place(x=20,y=190)
    
    native_box=Entry(canvas1)
    native_box.place(x=100,y=190)  
    
    dob=Label(canvas1,text="Date of Birth")
    dob.place(x=230,y=190)
    
    dob_box=Entry(canvas1)
    dob_box.place(x=310,y=190)
    
    hos_day=StringVar(canvas1)
    hos_day.set(None)
    
    hos=Radiobutton(canvas1,variable=hos_day,text="Hosteller",value="Hosteller")
    hos.place(x=10,y=225)
    
    days=Radiobutton(canvas1,variable=hos_day,text="Days Scholar",value="Days Scholar")
    days.place(x=80,y=225)
        
    _=Label(canvas1,text="|")
    _.place(x=170,y=225)
    _.configure(foreground="red")
        
    act_unact=StringVar(canvas1)
    act_unact.set(None)
    
    act=Radiobutton(canvas1,variable=act_unact,text="Active",value="Active")
    act.place(x=175,y=225)
    
    unact=Radiobutton(canvas1,variable=act_unact,text="Not Active",value="Not Active")
    unact.place(x=232,y=225)
    
    __=Label(canvas1,text="|")
    __.place(x=312,y=225)
    __.configure(foreground="red")
    
    m_f=StringVar(canvas1)
    m_f.set(None)
    
    m=Radiobutton(canvas1,variable=m_f,text="Male",value="Male")
    m.place(x=320,y=225)
    
    f=Radiobutton(canvas1,variable=m_f,text="Female",value="Female")
    f.place(x=370,y=225)
    
    other_label=Label(canvas1,text="Other")
    other_label.place(x=440,y=240)
    
    other=Text(canvas1,width=20,height=8)
    other.place(x=310,y=255)
    
    a_b_box=Entry(canvas1)
    b_c_box=Entry(canvas1)
    c_d_box=Entry(canvas1)
    d_e_box=Entry(canvas1)
    
    save=Button(canvas1,text="Save",command=save_record)
    save.place(x=250,y=400,width=70)    
    
    clear_butt=Button(canvas1,text="Clear",command=clear_func)
    clear_butt.place(x=350,y=400,width=70)
    
    a_b_va=StringVar(canvas1)
    b_c_va=StringVar(canvas1)
    c_d_va=StringVar(canvas1)
    d_e_va=StringVar(canvas1)
    
    def click():
        '''
           Registration number needs to be verified.
        
        '''
        
        no=reg_box.get()
                
        if no.isdigit() and len(no)!=0 and len(no)>=4:
            his_year=int(no[:4])
            a,b,c,d,e=range(his_year,his_year+5)
            
            a_b_va.set(str(a)+"-"+str(b))
            a_b=Label(canvas1,textvariable=a_b_va)
            a_b.place(x=20,y=260)
            
            a_b_box.place(x=100,y=260,width=200)  
                    
            b_c_va.set(str(b)+"-"+str(c))
            b_c=Label(canvas1,textvariable=b_c_va)
            b_c.place(x=20,y=295)
                        
            b_c_box.place(x=100,y=295,width=200)   
                        
            c_d_va.set(str(c)+"-"+str(d))
            c_d=Label(canvas1,textvariable=c_d_va)
            c_d.place(x=20,y=330)
                        
            c_d_box.place(x=100,y=330,width=200)
                        
            d_e_va.set(str(d)+"-"+str(e))
            d_e=Label(canvas1,textvariable=d_e_va)
            d_e.place(x=20,y=365)
                        
            d_e_box.place(x=100,y=365,width=200)  
            
            a_b_box.config(state="normal")
            b_c_box.config(state="normal")
            c_d_box.config(state="normal")
            d_e_box.config(state="normal")            
            
        else:
            
            a_b_box.config(state="disable")
            b_c_box.config(state="disable")
            c_d_box.config(state="disable")
            d_e_box.config(state="disable")
            
        if no in database:
            msgbox.showerror("Error",message="Register number already exists in the database.")   
            canvas1.focus_force()
            reg_box.delete(0,END)
            reg_box.focus_force()
            a_b_box.config(state="disable")
            b_c_box.config(state="disable")
            c_d_box.config(state="disable")
            d_e_box.config(state="disable")            
            
    canvas1.grid()
    
    add.resizable(0,0)
    add.focus_force()
    
    flag=add.bind("<Escape>",lambda *ignore:add.destroy())
    flag=canvas1.bind("<Button-1>",lambda *ignore:click())
    flag=name_box.bind("<Button-1>",lambda *ignore:click())
    flag=reg_box.bind("<Tab>",lambda *ignore:click())
    flag=add.bind("<Control l>",lambda *ignore:clear_func())
    flag=add.bind("<Control L>",lambda *ignore:clear_func())
    
    add.mainloop()

def show_result(*ignore):
    
    '''
           Function for Displaying result
    '''
    
    try:
        
        update.config(state="normal")
        delete.config(state="normal")        
        name=list_box.get(ACTIVE)
        
        for i in database:
            if database[i]["name"]==name:
                my_no=i   
                break
                         
        stu_year=int(my_no[:4])
        a,b,c,d,e=range(stu_year,stu_year+5)
        
        a_b=Label(canvas1,text=str(a)+"-"+str(b)+" (I Year)")
        a_b.place(x=20,y=295)
        a_b.configure(foreground="blue")
                
        a_b_label=Label(canvas1,textvariable=a_b_var)
        a_b_label.place(x=200,y=295) 
        
        b_c=Label(canvas1,text=str(b)+"-"+str(c)+" (II Year)")
        b_c.place(x=20,y=330)
        b_c.configure(foreground="blue")         
        
        b_c_label=Label(canvas1,textvariable=b_c_var)
        b_c_label.place(x=200,y=330)   
        
        c_d=Label(canvas1,text=str(c)+"-"+str(d)+" (III Year)")
        c_d.place(x=20,y=365)
        c_d.configure(foreground="blue")
        
        c_d_label=Label(canvas1,textvariable=c_d_var)            
        c_d_label.place(x=200,y=365)
        
        d_e=Label(canvas1,text=str(d)+"-"+str(e)+" (IV Year)")
        d_e.place(x=20,y=400)
        d_e.configure(foreground="blue")
        
        d_e_label=Label(canvas1,textvariable=d_e_var)            
        d_e_label.place(x=200,y=400)
               
        reg_var.set(my_no)
        name_var.set(database[my_no]['name'])
        dept_var.set(database[my_no]['dept'])
        con_var.set(database[my_no]['contact'])
        mail_var.set(database[my_no]['email'])
        native_var.set(database[my_no]['native'])
        hds_var.set(database[my_no]["hos_days"])
        au_var.set(database[my_no]["act_unact"])
        a_b_var.set(database[my_no]['year']["1"].values()[0])
        b_c_var.set(database[my_no]['year']["2"].values()[0])
        c_d_var.set(database[my_no]['year']["3"].values()[0])
        d_e_var.set(database[my_no]['year']["4"].values()[0])
        other_info.config(state="normal")
        other_info.delete("1.0",END)
        other_info.insert(END,database[my_no]['other'])
        other_info.config(state="disable")
        blood_var.set(database[my_no]['blood'])
        dob_var.set(database[my_no]['dob'])      
        
        try:
            img=Image.frombytes(database[my_no]['image'][0],(128,128),database[my_no]['image'][1])
            avata=ImageTk.PhotoImage(img)
            avatar_label=Label(canvas1,image=avata)
            avatar_label.image=avata 
            avatar_label.place(x=340,y=17)
            
        except:
            pass
        
    except:
        
        msgbox.showerror("Error",message="Select valid record..")
        
def search_result():
    
    adv.grid(row=2,column=0)
    
    flag=app.bind("<Alt r>",lambda *ignore:save_result()) 
    flag=app.bind("<Alt R>",lambda *ignore:save_result())               # Save the results      
    
    list_box.delete(0,END)
    reg_var.set("")
    name_var.set("")
    dept_var.set("")
    con_var.set("")
    mail_var.set("")
    native_var.set("")
    hds_var.set("")
    au_var.set("")
    a_b_var.set("")
    b_c_var.set("")
    c_d_var.set("")
    d_e_var.set("")
    other_info.config(state="normal")
    other_info.delete("1.0",END)
    blood_var.set("")
    dob_var.set("")
    text_box.focus_force()
    found_var.set("Found")
    adv.config(state="disable")
    update.config(state="disable")
    delete.config(state="disable")    
    img=Image.frombytes("L",(128,128),database['default_image'])
    avata=ImageTk.PhotoImage(img)
    avatar_label=Label(canvas1,image=avata)
    avatar_label.image=avata
    avatar_label.place(x=340,y=17)    
    
    key_word=text_box.get().split()
    key_word=[i.lower() for i in key_word]
    bresults,results=[],[]
    YY={'I Year':[],'II Year':[],'III Year':[],'IV Year':[]}
    
    given_year=variable.get()
        
    my_keys=[i for i in database.keys() if i.isdigit()]
    total=len(my_keys)
        
    for i in my_keys:
        
        total_data=re.sub("\s","",database[i]['name']+database[i]['hos_days']+database[i]['gender']+database[i]['act_unact']+database[i]['dept']+database[i]['contact']+database[i]['blood']+database[i]['native']+database[i]['email']+i).lower()
        
        yyears=sum([database[i]['year'].values()[k].keys() for k in (0,1,2,3)],[])
        
        if Allvar.get():
            if given_year==database[i]['year']['1'].keys()[0]:
                if len(key_word)!=0:
                    for j in key_word:    
                        if j in total_data:
                            YY['I Year'].append(i)
                else:
                    YY['I Year'].append(i)                        

            if given_year==database[i]['year']['2'].keys()[0]:
                if len(key_word)!=0:
                    for j in key_word:    
                        if j in total_data:
                            YY['II Year'].append(i)
                else:               
                    YY['II Year'].append(i)                      
                    
            if given_year==database[i]['year']['3'].keys()[0]:
                if len(key_word)!=0:
                    for j in key_word:    
                        if j in total_data:
                            YY['III Year'].append(i)
                else:
                    YY['III Year'].append(i)
                    
            if given_year==database[i]['year']['4'].keys()[0]:
                if len(key_word)!=0:
                    for j in key_word:    
                        if j in total_data:
                            YY['IV Year'].append(i)
                else:
                    YY['IV Year'].append(i)                    
                                        
        else:
            
            if first.get()==True:
                if given_year==database[i]['year']['1'].keys()[0]:
                    if len(key_word)!=0:
                        for j in key_word:    
                            if j in total_data:
                                YY['I Year'].append(i)
                    else:
                        YY['I Year'].append(i)
            
            if second.get()==True:
                if given_year==database[i]['year']['2'].keys()[0]:
                    if len(key_word)!=0:
                        for j in key_word:    
                            if j in total_data:
                                YY['II Year'].append(i)
                    else:               
                        YY['II Year'].append(i)
                        
            if third.get()==True:
                if given_year==database[i]['year']['3'].keys()[0]:
                    if len(key_word)!=0:
                        for j in key_word:    
                            if j in total_data:
                                YY['III Year'].append(i)
                    else:
                        YY['III Year'].append(i)
            
            if fourth.get()==True:
                if given_year==database[i]['year']['4'].keys()[0]:
                    if len(key_word)!=0:
                        for j in key_word:    
                            if j in total_data:
                                YY['IV Year'].append(i)
                    else:
                        YY['IV Year'].append(i)
        
    bresults=list(set(bresults))

    YY['I Year']=list(set(YY['I Year']))
    YY['II Year']=list(set(YY['II Year']))
    YY['III Year']=list(set(YY['III Year']))
    YY['IV Year']=list(set(YY['IV Year']))
        
    if len(YY['I Year'])!=0:
        bresults.append("  First Year")
        for i in YY['I Year']:
            bresults.append(database[i]['name'])
     
    if len(YY['II Year'])!=0:
        bresults.append("  Second Year")
        for i in YY['II Year']:
            bresults.append(database[i]['name'])    
            
    if len(YY['III Year'])!=0:
        bresults.append("   Third Year")
        for i in YY['III Year']:
            bresults.append(database[i]['name'])
            
    if len(YY['IV Year'])!=0:
        bresults.append("  Fourth Year")
        for i in YY['IV Year']:
            bresults.append(database[i]['name'])    
            
    list_box.delete(0,END)
    
    list_box.insert(END,*bresults)    
    
    try:
        i1=bresults.index("  First Year")
        list_box.itemconfig(i1,{'fg':'blue'})
    except:pass
    try:
        i2=bresults.index("  Second Year")
        list_box.itemconfig(i2,{'fg':'blue'})
    except:pass
    try:
        i3=bresults.index("   Third Year")
        list_box.itemconfig(i3,{'fg':'blue'})
    except:pass
    try:
        i4=bresults.index("  Fourth Year")
        list_box.itemconfig(i4,{'fg':'blue'})
    except:pass
    
    results=[]+bresults
    try:results.remove("  First Year")
    except:pass
    
    try:results.remove("  Second Year")
    except:pass
    
    try:results.remove("   Third Year")
    except:pass
    
    try:results.remove("  Fourth Year")
    except:pass    
            
    found_var.set("Found "+str(len(results))+" / "+str(total))
    
    if len(bresults)==0:
        adv.config(state="disable")
        delete.config(state="disable")
        update.config(state="disable")   
    else:
        adv.config(state="normal")
        
    vaasu_results.append(YY)
    vaasu_results.append(bresults)
        
    list_box.bind('<Double Button-1>',show_result)  

def update_record():
    '''
          This function will update the existing records save to the database.
       
    '''
    def save_record():
        
        if len(name_box.get())!=0 and len(dept_box.get())!=0 and len(contact_box.get())!=0 and len(reg_box.get())!=0:
            
            otherrr=re.sub("\n","",otherr.get("1.0",END))
            data={"name":name_box.get(),"dept":dept_box.get(),"contact":contact_box.get(),"email":mail_box.get(),"native":native_box.get(),"other":otherrr,"image":[str(to_bytes_mode.get()),str(to_bytes.get())],"gender":m_f.get(),"act_unact":act_unact.get(),"hos_days":hos_day.get(),"dob":dob_box.get(),"blood":blood_box.get(),"year":{"1":{a_b_va.get():a_b_box.get()},"2":{b_c_va.get():b_c_box.get()},"3":{c_d_va.get():c_d_box.get()},"4":{d_e_va.get():d_e_box.get()}}}
                       
            del database[reg_var.get()]
            database[reg_box.get()]=data
            
            msgbox.showinfo("Confirmation..",message="Updated Successfully..")
            add.destroy()        
            clear()          
                                       
        else:
            
            msgbox.showerror("Error",message="Fields can't be empty.")
            add.focus_force()    
            reg_box.focus_set()
                  
    def Add_Image():
        
        myFormats=[('JPEG / JFIF','*.jpg'),('Portable Network Graphics','*.png'),('Windows Bitmap','*.bmp'),]
        path=askopenfile(title="Open Image",filetypes=myFormats) 
        add.focus_force()

        try:
        
            client=Image.open(path.name).resize((128,128),Image.ANTIALIAS)
            to_bytes_mode.set(client.mode)
            to_bytes.set(client.tobytes())
            
        except:pass    
        
    def clear_func():
        reg_box.delete(0,END)
        name_box.delete(0,END)
        dept_box.delete(0,END)
        contact_box.delete(0,END)
        mail_box.delete(0,END)
        native_box.delete(0,END)
        a_b_box.delete(0,END)
        b_c_box.delete(0,END)
        c_d_box.delete(0,END)
        d_e_box.delete(0,END)
        reg_box.focus_force()
        otherr.delete("1.0",END)
        hos_day.set(None)
        act_unact.set(None)
        m_f.set(None)
        blood_box.delete(0,END)
        dob_box.delete(0,END)
        
        im=Image.frombytes("L",(128,128),database['default_image'])
        avata=ImageTk.PhotoImage(im)
        avatar_label=Label(add,image=avata)
        avatar_label.image=avata
        avatar_label.place(x=340,y=10,height=80)         
    
    add=Toplevel()
    add.geometry("500x445+645+143")
    add.title("Update record")
    
    icon=Image.frombytes("RGBA",(256,256),database['icon'])
    im=ImageTk.PhotoImage(icon)    
    add.tk.call('wm','iconphoto',add._w,im)    
    
    canvas1=Canvas(add,width=600,height=550)
    
    im=Image.frombytes(database[reg_var.get()]['image'][0],(128,128),database[reg_var.get()]['image'][1])
    avata=ImageTk.PhotoImage(im)
    avatar_label=Label(add,image=avata)
    avatar_label.image=avata
    avatar_label.place(x=340,y=10,height=80) 
    
    to_bytes_mode=StringVar(canvas1)
    to_bytes=StringVar(canvas1)
    
    to_bytes_mode.set(database[reg_var.get()]['image'][0])
    to_bytes.set(database[reg_var.get()]['image'][1])

    img_butt=Button(canvas1,text="Add Image",command=Add_Image)
    img_butt.place(x=370,y=100)    
        
    regno=Label(canvas1,text="Reg No")
    regno.place(x=20,y=15)
    
    reg_box=Entry(canvas1)
    reg_box.place(x=100,y=15)
    reg_box.insert(0,reg_var.get())
    
    name=Label(canvas1,text="Name")
    name.place(x=20,y=50)
    
    name_box=Entry(canvas1)
    name_box.insert(0,name_var.get())
    name_box.place(x=100,y=50)
    
    dept=Label(canvas1,text="Department")
    dept.place(x=20,y=85)
    
    dept_box=Entry(canvas1)
    dept_box.place(x=100,y=85,width=175)
    dept_box.insert(0,dept_var.get())
    
    contact=Label(canvas1,text="Contact")
    contact.place(x=20,y=120)
    
    contact_box=Entry(canvas1)
    contact_box.place(x=100,y=120)
    contact_box.insert(0,con_var.get())
    
    blood=Label(canvas1,text="Blood Group")
    blood.place(x=230,y=120)
    
    blood_box=Entry(canvas1)
    blood_box.place(x=310,y=120,width=30)
    blood_box.insert(0,blood_var.get())
    
    mail=Label(canvas1,text="E-Mail Id")
    mail.place(x=20,y=155)
    
    mail_box=Entry(canvas1)
    mail_box.place(x=100,y=155,width=175)
    mail_box.insert(0,mail_var.get())
    
    native=Label(canvas1,text="Native")
    native.place(x=20,y=190)
    
    native_box=Entry(canvas1)
    native_box.place(x=100,y=190)  
    native_box.insert(0,native_var.get())
    
    dob=Label(canvas1,text="Date of Birth")
    dob.place(x=230,y=190)
    
    dob_box=Entry(canvas1)
    dob_box.place(x=310,y=190)
    dob_box.insert(0,dob_var.get())
    
    hos_day=StringVar(canvas1)
    hos_day.set(None)
    
    hos=Radiobutton(canvas1,variable=hos_day,text="Hosteller",value="Hosteller")
    hos.place(x=10,y=225)
    
    days=Radiobutton(canvas1,variable=hos_day,text="Days Scholar",value="Days Scholar")
    days.place(x=80,y=225)
       
    _=Label(canvas1,text="|")
    _.place(x=170,y=225)
    _.configure(foreground="red")
        
    act_unact=StringVar(canvas1)
    act_unact.set(None)
    
    act=Radiobutton(canvas1,variable=act_unact,text="Active",value="Active")
    act.place(x=175,y=225)
    
    unact=Radiobutton(canvas1,variable=act_unact,text="Not Active",value="Not Active")
    unact.place(x=232,y=225)
    
    __=Label(canvas1,text="|")
    __.place(x=312,y=225)
    __.configure(foreground="red")
    
    m_f=StringVar(canvas1)
    
    m=Radiobutton(canvas1,variable=m_f,text="Male",value="Male")
    m.place(x=320,y=225)
    
    f=Radiobutton(canvas1,variable=m_f,text="Female",value="Female")
    f.place(x=370,y=225)
    
    no=reg_box.get()
    
    m_f.set(database[no]['gender'])
    
    hos_day.set(hds_var.get())
    
    act_unact.set(au_var.get())
     
    other_label=Label(canvas1,text="Other")
    other_label.place(x=440,y=240)
    
    otherr=Text(canvas1,width=20,height=8)
    otherr.place(x=310,y=255)
    otherr.insert(END,other_info.get("1.0",END))
    
    a_b_box=Entry(canvas1)
    b_c_box=Entry(canvas1)
    c_d_box=Entry(canvas1)
    d_e_box=Entry(canvas1)
    
    a_b_va=StringVar(canvas1)
    b_c_va=StringVar(canvas1)
    c_d_va=StringVar(canvas1)
    d_e_va=StringVar(canvas1)
    
    save=Button(canvas1,text="Update",command=save_record)
    save.place(x=250,y=400,width=70)    
    
    clear_butt=Button(canvas1,text="Clear",command=clear_func)
    clear_butt.place(x=350,y=400,width=70)
              
    state=StringVar(canvas1)
    state.set(" ")

    status=Label(canvas1,textvariable=state)
    status.place(x=225,y=15)  
    
    try:
        
        his_year=int(no[:4])
        a,b,c,d,e=range(his_year,his_year+5)
        
        a_b_va.set(str(a)+"-"+str(b))
        a_b=Label(canvas1,textvariable=a_b_va)
        a_b.place(x=20,y=260)
        
        a_b_box.place(x=100,y=260,width=200)  
        a_b_box.insert(0,a_b_var.get())
        
        b_c_va.set(str(b)+"-"+str(c))
        b_c=Label(canvas1,textvariable=b_c_va)
        b_c.place(x=20,y=295)
                    
        b_c_box.place(x=100,y=295,width=200)   
        b_c_box.insert(0,b_c_var.get())
        
        c_d_va.set(str(c)+"-"+str(d))
        c_d=Label(canvas1,textvariable=c_d_va)
        c_d.place(x=20,y=330)
                    
        c_d_box.place(x=100,y=330,width=200)
        c_d_box.insert(0,c_d_var.get())
        
        d_e_va.set(str(d)+"-"+str(e))
        d_e=Label(canvas1,textvariable=d_e_va)
        d_e.place(x=20,y=365)
                    
        d_e_box.place(x=100,y=365,width=200)  
        d_e_box.insert(0,d_e_var.get())  
        
    except:
        pass

    canvas1.grid()
    
    add.resizable(0,0)
    add.focus_force()
    
    flag=add.bind("<Escape>",lambda *ignore:add.destroy())
    flag=add.bind("<Control l>",lambda *ignore:clear_func())
    
    add.mainloop()

def delete_record():
    if len(reg_var.get())!=0:
        if msgbox.askyesno("Deletion",message="Are you sure you want to delete the record. This can't be undone.."):
            del database[reg_var.get()]
            clear()
    
# SearchBar Frame

search=Frame(app)         # Creation of Frame that can have tkinter objects like text box, buttons etc.
search.grid(ipadx=200)

text_box=Entry(search,width=100)    # Creation of text box
text_box.grid(padx=30,pady=10,row=0,column=0)
text_box.focus_set()                # Function explains

var=StringVar(search)
var.set("Category")
Type=OptionMenu(search,variable=var,value="Category")
Type.place(x=690,y=4)
first=BooleanVar(search)
second=BooleanVar(search)
third=BooleanVar(search)
fourth=BooleanVar(search)
all_=BooleanVar()
all_.set(True)
Allvar=BooleanVar(search)

def All_search(): 
    
    if Allvar.get():
        Type.config(state="disable")
    else:
        Type.config(state="normal")
        
All=Checkbutton(search,text="All",variable=Allvar,onvalue=True,offvalue=False,command=All_search)
All.select()
Type.config(state="disable")

All.place(x=644,y=11)
Type['menu'].add_checkbutton(label="I Year",onvalue=True,offvalue=False,variable=first)
Type['menu'].add_checkbutton(label="II Year",onvalue=True,offvalue=False,variable=second)
Type['menu'].add_checkbutton(label="III Year",onvalue=True,offvalue=False,variable=third)
Type['menu'].add_checkbutton(label="IV Year",onvalue=True,offvalue=False,variable=fourth)

variable=StringVar(search)
yy=set(sorted([int(i[:4]) for i in database.keys() if i.isdigit()]))
current_month=datetime.now().month
years=[]
try:
    strt=min(yy)
    for i in range(strt,int(current_year)+1):
        years.append(str(i)+"-"+str(i+1))
except:
    years.append(str(current_year)+"-"+str(int(current_year)+1))
variable=StringVar(search)
j=[]
for i in years:
    if current_year in i:
        j.append(i)
if current_month<=4:my_year=j[0]
else:my_year=j[1]
variable.set(my_year)

year=OptionMenu(search,variable,*years)
year.place(x=785,y=4)

search_button=Button(search,text="Search",command=search_result,underline=0)
search_button.place(x=888,y=5,width=70,height=28)

# Results Frame

result=Frame(app,width=1000,height=1000)       
result.grid(sticky="nw",row=1,column=0)

found_var=StringVar()
found_var.set("Found : ")
Found=Label(result,textvariable=found_var)
Found.place(x=27,y=0)
Found.config(foreground="red")

scroll=Scrollbar(result,orient="vertical")  # Scroll bar for scrolling the results 
scroll.grid(row=1,column=1,sticky="n"+"s"+"w",pady=16)

list_box=Listbox(result,height=20,width=25,cursor="hand2",font=Font(size=15))   # Creation of List Box for displaying the results
list_box.grid(row=1,column=0,padx=29,pady=16)

scroll.configure(command=list_box.yview)
list_box.configure(yscrollcommand=scroll.set)

adv=Button(result,text="Save Results",command=save_result,underline=5)

# Canvas                 

canvas=Canvas(result,width=2,height=501)     # The Line between the scrollBar and the Result box
canvas.grid(row=1,column=1,padx=65)
canvas.config(background="red")

# Display Frame

display=Frame(app,width=1000,height=1000)
display.place(x=450,y=45)

canvas1=Canvas(display,width=502,height=526)
canvas1.place(x=0,y=0)
canvas1.create_rectangle(5,5,500,490,outline="blue")              # The Outer box covering the Display Section

regno=Label(canvas1,text="Reg No")
regno.place(x=20,y=15)
regno.configure(foreground="blue")

reg_var=StringVar(canvas1)
reg_box=Label(canvas1,textvariable=reg_var)
reg_box.place(x=200,y=15)

img=Image.frombytes("L",(128,128),database['default_image'])
avata=ImageTk.PhotoImage(img)
avatar_label=Label(canvas1,image=avata)
avatar_label.image=avata
avatar_label.place(x=340,y=17)

name=Label(canvas1,text="Name")
name.place(x=20,y=50)
name.configure(foreground="blue")

name_var=StringVar(canvas1)
name_box=Label(canvas1,textvariable=name_var)
name_box.place(x=200,y=50)

dept=Label(canvas1,text="Department")
dept.place(x=20,y=85)
dept.configure(foreground="blue")

dept_var=StringVar(canvas1)
dept_box=Label(canvas1,textvariable=dept_var)
dept_box.place(x=200,y=85)

contact=Label(canvas1,text="Contact")
contact.place(x=20,y=120)
contact.configure(foreground="blue")

con_var=StringVar(canvas1)
contact_box=Label(canvas1,textvariable=con_var)
contact_box.place(x=200,y=120)

blood=Label(canvas1,text="Blood Group")
blood.place(x=300,y=225)
blood.configure(foreground="blue")

blood_var=StringVar(canvas1)
blood_box=Label(canvas1,textvariable=blood_var)
blood_box.place(x=380,y=225,width=30)

mail=Label(canvas1,text="E-Mail Id")
mail.place(x=20,y=155)
mail.configure(foreground="blue")

mail_var=StringVar(canvas1)
mail_box=Label(canvas1,textvariable=mail_var)
mail_box.place(x=200,y=155)

native=Label(canvas1,text="Native")
native.place(x=20,y=190)
native.configure(foreground="blue")

native_var=StringVar(canvas1)
native_box=Label(canvas1,textvariable=native_var)
native_box.place(x=200,y=190)

dob=Label(canvas1,text="Date of Birth")
dob.place(x=300,y=260)
dob.configure(foreground="blue")

dob_var=StringVar(canvas1)
dob_box=Label(canvas1,textvariable=dob_var)
dob_box.place(x=380,y=260)

hos_days=Label(canvas1,text="Hosteller / Day Scholar")
hos_days.place(x=20,y=225)
hos_days.configure(foreground="blue")

hds_var=StringVar(canvas1)
hds_box=Label(canvas1,textvariable=hds_var)
hds_box.place(x=200,y=225)

act_unact=Label(canvas1,text="Active / Not Active")
act_unact.place(x=20,y=260)
act_unact.configure(foreground="blue")

au_var=StringVar(canvas1)
au_label=Label(canvas1,textvariable=au_var)
au_label.place(x=200,y=260)

a_b_var=StringVar(canvas1)
b_c_var=StringVar(canvas1)
c_d_var=StringVar(canvas1)
d_e_var=StringVar(canvas1)

other_label=Label(canvas1,text="Other")
other_label.place(x=20,y=435)
other_label.configure(foreground="blue")

other_info=Text(canvas1)
other_info.place(x=200,y=435,width=280,height=40)

  # Buttons for Updation and Deletion

add=Button(canvas1,text="New",command=add_record,underline=0)
add.place(x=150,y=500,width=50)

update=Button(canvas1,text="Update",command=update_record,underline=0)
update.place(x=250,y=500)

delete=Button(canvas1,text="Delete",command=delete_record,underline=0)
delete.place(x=350,y=500)

if len(reg_var.get())==0:
    update.config(state="disable")
    delete.config(state="disable")

def key_bindings():  # Control+k or Control +K function
    
    '''
      Creation of a small window that shows information about the keyboard shortcuts available.
      
    '''   
    key=Toplevel()
    key.title("KeyBoard Shortcuts")
    key.geometry("350x300+300+200")
    key.resizable(0,0)
    
    icon=Image.frombytes("RGBA",(256,256),database['icon'])
    im=ImageTk.PhotoImage(icon)    
    key.tk.call('wm','iconphoto',key._w,im)    
    
    shortcut=Label(key,text="")
    shortcut.pack()
    
    shortcut0=Label(key,text="To view the Keyboard shortcuts........ ctrl+k or ctrl+K")
    shortcut0.pack()
    
    shortcut1=Label(key,text="To insert a new record to the database........ alt+n or alt+N")
    shortcut1.pack()    
    
    shortcut2=Label(key,text="To Update the existing record... alt+u or alt+U")
    shortcut2.pack()  
    
    shortcut3=Label(key,text="To delete the existing record... alt+d or alt+D")
    shortcut3.pack()    
    
    shortcut4=Label(key,text="Save the results from the ListBox... alt+r or alt+R")
    shortcut4.pack()    
         
    shortcut5=Label(key,text="Clear the result box........ctrl+l or ctrl+L")
    shortcut5.pack()      
    
    shortcut7=Label(key,text="Search... alt+s or alt+S")
    shortcut7.pack()
    
    shortcut8=Label(key,text="Close the sub window(if exists and active).... esc")
    shortcut8.pack()
    
    shortcut9=Label(key,text="Minimize the database..... esc")
    shortcut9.pack()
    
    shortcut10=Label(key,text="Close the database........ ctrl+q or ctrl+Q")
    shortcut10.pack()      
    
    shortcut11=Label(key,text="About the software........ alt+a or alt+A")
    shortcut11.pack()
    
    shortcut12=Label(key,text="About the Developer.... ctrl+alt+shift+d")
    shortcut12.pack()
       
    key.focus_force()
    flag=key.bind("<Escape>",lambda *ignore:key.destroy())
    key.mainloop()

def about():  # Alt+a or Alt+A function
    '''
     Creation of a small window that shows information about the keyboard shortcuts available.
     
    '''    
    def get_source_code():
        # Ask for the directory and save the Source code in the file
        try:
            stri="https://www.google.co.in"
            data=urlopen(stri)            
            save_file=asksaveasfile(title="Enter only the file name..",mode='w', defaultextension=".py")
            files=urlopen("https://raw.githubusercontent.com/VaasuDevanS/Database_SQC/master/main.py")
            if save_file:
                for line in files:
                    save_file.write(line)
                save_file.close()
            msgbox.showinfo("Success",message="Saved Successfully..")
            files.close()
            about.destroy()
            app.focus_force()
        except:
            msgbox.showerror("Error",message="Requires internet connection")
            about.focus_force()
    
    about=Toplevel()
    about.title("About")
    about.geometry("600x115+300+300")
    about.resizable(0,0)
    
    icon=Image.frombytes("RGBA",(256,256),database['icon'])
    im=ImageTk.PhotoImage(icon)    
    about.tk.call('wm','iconphoto',about._w,im)    
    
    desc0=Label(about,text="This Software is used to manage the students database for the Students Quality Council.")
    desc0.pack()
    
    desc1=Label(about,text="This software is developed using Python 2.7.12 on windows 8.1 64-bit")
    desc1.pack() 
    
    desc2=Label(about,text="mainly using Tkinter and Shelve Modules.")
    desc2.pack()
    
    save=Button(about,text="Save and View the Source Code..!",command=get_source_code)
    save.pack()
    save.configure(foreground="red")
    
    desc3=Label(about,text="Press esc to close this window..")
    desc3.pack()
    
    about.focus_force()
    flag=about.bind("<Escape>",lambda *ignore:about.destroy())
    about.mainloop()

def insert(): # Alt+n or Alt+N function
    add_record()

def enter():  # Enter key function
    search_result()

def developer():   #Control+Alt+D function
    
    '''
       Creation of a small window that shows small information about the developer (Yep.. that's me...!!)
       And also a link to view the developer's information in the Students database.
    
    '''
    
    def vaasu_view():
        
        my_no='2014107051'
                         
        stu_year=int(my_no[:4])
        a,b,c,d,e=range(stu_year,stu_year+5)
        
        a_b=Label(canvas1,text=str(a)+"-"+str(b)+" (I Year)")
        a_b.place(x=20,y=295)
        a_b.configure(foreground="blue")
                
        a_b_label=Label(canvas1,textvariable=a_b_var)
        a_b_label.place(x=200,y=295) 
        
        b_c=Label(canvas1,text=str(b)+"-"+str(c)+" (II Year)")
        b_c.place(x=20,y=330)
        b_c.configure(foreground="blue")         
        
        b_c_label=Label(canvas1,textvariable=b_c_var)
        b_c_label.place(x=200,y=330)   
        
        c_d=Label(canvas1,text=str(c)+"-"+str(d)+" (III Year)")
        c_d.place(x=20,y=365)
        c_d.configure(foreground="blue")
        
        c_d_label=Label(canvas1,textvariable=c_d_var)            
        c_d_label.place(x=200,y=365)
        
        d_e=Label(canvas1,text=str(d)+"-"+str(e)+" (IV Year)")
        d_e.place(x=20,y=400)
        d_e.configure(foreground="blue")
        
        d_e_label=Label(canvas1,textvariable=d_e_var)            
        d_e_label.place(x=200,y=400)
        
        other_info.place(x=200,y=435,width=280,height=40)
        reg_var.set(my_no)
        name_var.set(database[my_no]['name'])
        dept_var.set(database[my_no]['dept'])
        con_var.set(database[my_no]['contact'])
        mail_var.set(database[my_no]['email'])
        native_var.set(database[my_no]['native'])
        hds_var.set(database[my_no]["hos_days"])
        au_var.set(database[my_no]["act_unact"])
        a_b_var.set(database[my_no]['year']["1"].values()[0])
        b_c_var.set(database[my_no]['year']["2"].values()[0])
        c_d_var.set(database[my_no]['year']["3"].values()[0])
        d_e_var.set(database[my_no]['year']["4"].values()[0])
        other_info.insert(END,database[my_no]['other'])
        other_info.config(state="disable")
        blood_var.set(database[my_no]['blood'])
        dob_var.set(database[my_no]['dob'])      
        
        try:
            
            img=Image.frombytes(database[my_no]['image'][0],(128,128),database[my_no]['image'][1])
            avata=ImageTk.PhotoImage(img)
            avatar_label=Label(canvas1,image=avata)
            avatar_label.image=avata 
            avatar_label.place(x=340,y=17)
            
        except:pass     
        
    def profile_view():
        try:
            stri="https://www.google.co.in"
            data=urlopen(stri)            
            webbrowser.open("https://www.github.com/VaasuDevanS")
        except:
            msgbox.showerror("Error",message="Requires Internet Conection")
            dev.focus_force()
    
    dev=Toplevel()
    dev.geometry("300x87+300+300")
    dev.resizable(0,0)
    dev.title("Developer")
    
    icon=Image.frombytes("RGBA",(256,256),database['icon'])
    im=ImageTk.PhotoImage(icon)    
    dev.tk.call('wm','iconphoto',dev._w,im)    
    
    name=Label(dev,text="Name:  Vaasu Devan S")
    name.pack()
    name.configure(foreground="red")
    
    profile=Label(dev,text="Click here to view his GitHub Profile",cursor="hand2")
    profile.pack()
    ufont=Font(profile,profile.cget("font"))
    ufont.configure(underline=True)
    
    profile.configure(font=ufont,foreground="blue")
    
    profile.bind("<Button-1>",lambda*ignore:profile_view())
    
    view=Button(dev,text="view in the database",command=vaasu_view)
    view.pack()
    
    text=Label(dev,text="Press the Escape key to close this window...")
    text.pack(side="bottom")
    text.configure(foreground="red")
    
    dev.focus_force()
    flag=dev.bind("<Escape>",lambda *ignore:dev.destroy())
    dev.mainloop()    

def Easter_Egg():
    
    a=dir_path=askdirectory()
    os.chdir(a)
    os.mkdir("Easter_Egg_Result...")
    os.chdir(a+"\\"+"Easter_Egg_Result...")
    my_nos=[i for i in database if i.isdigit()]
    for i in my_nos:
        im=Image.frombytes(database[i]['image'][0],(128,128),database[i]['image'][1])
        file_name=database[i]['gender'][0]+"_"+database[i]['name']+"_"+database[i]['contact']+"_"+database[i]['native']+"_"+database[i]['hos_days']+"_"+database[i]['dob']+"_"+database[i]['blood']+"_"+i+database[i]['dept']
        im.save(str(file_name)+".jpg")
        
    msgbox.showerror("")
    
# Keyboard Shortcut Bindings
# flag variable is used to get the return values of the bind function

flag=app.bind("<Control k>",lambda *ignore:key_bindings())
flag=app.bind("<Control K>",lambda *ignore:key_bindings())          # To show the Keyboard shortcuts in a new window

flag=app.bind("<Alt n>",lambda *ignore:insert())
flag=app.bind("<Alt N>",lambda *ignore:insert())                    # To insert a new Record to the Database

flag=app.bind("<Alt a>",lambda *ignore:about())
flag=app.bind("<Alt A>",lambda *ignore:about())                     # To show the about window

flag=app.bind("<Control l>",lambda *ignore:clear())  
flag=app.bind("<Control L>",lambda *ignore:clear())                 # To clear everything and go to its default view

flag=app.bind("<Control q>",lambda *ignore:app.destroy()) 
flag=app.bind("<Control Q>",lambda *ignore:app.destroy())           # Close the window (Quit from the database)

flag=app.bind("<Alt s>",lambda *ignore:search_result()) 
flag=app.bind("<Alt S>",lambda *ignore:search_result())             # Search

flag=app.bind("<Alt u>",lambda *ignore:update_record()) 
flag=app.bind("<Alt U>",lambda *ignore:update_record())             # Update

flag=app.bind("<Alt d>",lambda *ignore:delete_record()) 
flag=app.bind("<Alt D>",lambda *ignore:delete_record())             # Delete

flag=app.bind("<Control Alt G>",lambda *ignore:Easter_Egg())        # Easter Egg... !
flag=app.bind("<Control Alt D>",lambda *ignore:developer())         # To show info about the developer
flag=app.bind("<Escape>",lambda *ignore:app.iconify())              # Minimizes the window by pressing the Escape button
flag=app.bind("<Return>",lambda *ignore:enter())                    # For Search command

# MenuBar Frame

menubar=Menu(app)
app.config(menu=menubar)

filemenu1=Menu(menubar,tearoff=0)
filemenu1.add_command(label="Insert a new record...",command=insert)
filemenu1.add_command(label="Clear All...",command=clear)
filemenu1.add_command(label="KeyBoard Shortcuts...",command=key_bindings)
filemenu1.add_command(label="Minimize...",command=lambda *ignore:app.iconify())
filemenu1.add_command(label="Quit...",command=lambda *ignore:app.destroy())

filemenu2=Menu(menubar,tearoff=0)
filemenu2.add_command(label="About the App...",command=about)
filemenu2.add_command(label="About the developer...",command=developer)

menubar.add_cascade(label="Tools",menu=filemenu1,underline=0)
menubar.add_cascade(label="About",menu=filemenu2,underline=1)

app.focus_force()                # Making the application window active
app.mainloop()   # To make window Running until close button is pressed

database.close()                 # Closing the Connection between the database file and the program

'''

    Hope you understood this code. Feedbacks are welcome.
    Enjoy Python Coding... :-)

'''
