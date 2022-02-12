#Bank ACCOUNT (Last ver.)
import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime

def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def check_acc_nmb(num):
	try:
		pin=open(num+".txt",'r')
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Numbers\nTry Again!")
		return 
	pin.close()
	return 

def home_return(ID):
	ID.destroy()
	Main_Menu()

def write(ID,name,oc,pin):
    if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""):
            messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
            ID.destroy()
            return 

    file=open("Accnt_Record.txt",'r')
    accnt_no=int(file.readline())
    accnt_no+=1
    file.close()

    file=open("Accnt_Record.txt",'w')
    file.write(str(accnt_no))
    file.close()

    Account=open(str(accnt_no)+".txt","w")
    Account.write(pin+"\n")
    Account.write(oc+"\n")
    Account.write(str(accnt_no)+"\n")
    Account.write(name+"\n")
    Account.close()
	
    messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
    ID.destroy()
    return

def M_write(ID,amt,accnt,name):
    if(is_number(amt)==0):
        messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
        master.destroy()
        return 

    Account=open(accnt+".txt",'r')
    pin=Account.readline()
    camt=int(Account.readline())
    Account.close()
    
    amti=int(amt)
    cb=amti+camt
    Account=open(accnt+".txt",'w')
    Account.write(pin)
    Account.write(str(cb)+"\n")
    Account.write(accnt+"\n")
    Account.write(name+"\n")
    Account.close()
    
    messagebox.showinfo("Operation Successfull","Amount Credited Successfully")
    ID.destroy()
    return

def M_Amt(accnt,name):
    credit=tk.Tk()
    credit.geometry("500x250")
    credit.title("Credit Amount")

    bt_title=tk.Message(credit,text="Credit Payment",width=2000,padx=600,pady=0,anchor="center")
    bt_title.config(font=("Tahoma","40","bold"))
    bt_title.pack(side="top")
	
    bt=tk.Label(credit,text="Enter Amount of Payment: ")
    bt.pack(side="top")
	
    entry=tk.Entry(credit)
    entry.pack(side="top")
	
    b=tk.Button(credit,text="Enter",command=lambda:M_write(credit,entry.get(),accnt,name))
    b.pack(side="top")
    credit.bind("<Return>",lambda x:M_write(credit,entry.get(),accnt,name))

def disp_bal(accnt):
    read=open(accnt+".txt",'r')
    read.readline()
    show=read.readline()
    read.close()
    messagebox.showinfo("Balance",show)

def logged_in_menu(accnt,name):
    logged=tk.Tk()
    logged.geometry("1000x500")
    logged.title("Bank Accountant")

    bt_title=tk.Message(text="Bank Account",width=2000,padx=600,pady=0,anchor="center")
    bt_title.config(font=("Tahoma","50","bold"))
    bt_title.pack(side="top")
    
    label=tk.Label(text="Logged in as: "+name,anchor="center")
    label.pack(side="top")
    
    bt_credit=tk.Button(logged,text='CREDIT PAYMENT',command=lambda: M_Amt(accnt,name))
    bt_credit.config(font=("Tahoma","20","bold"))
    bt_credit.place(x=150,y=150)

    bt_balance=tk.Button(logged,text='BALANCE',command=lambda: disp_bal(accnt))
    bt_balance.config(font=("Tahoma","20","bold"))
    bt_balance.place(x=600,y=150)
 
    bt_logout=tk.Button(logged,text='LOGOUT',command=lambda: logout(logged))
    bt_logout.config(font=("Tahoma","20","bold"))
    bt_logout.place(x=400,y=400)

def logout(ID):
	messagebox.showinfo("Logged Out","You Have Been Logged Out")
	ID.destroy()
	Main_Menu()

def check_log_in(ID,name,acc_num,pin):
	if(check_acc_nmb(acc_num)==0):
		ID.destroy()
		Main_Menu()
		return

	elif( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Error","Invalid Login\nPlease try again.")
		ID.destroy()
		Main_Menu()
	else:
		ID.destroy()
		logged_in_menu(acc_num,name)


def log_in(ID):
    ID.destroy()
    login=tk.Tk()
    login.geometry("500x250")
    login.title("Create Account")
    
    bt_title=tk.Message(login,text="LOGIN",width=2000,padx=600,pady=0,anchor="center")
    bt_title.config(font=("Tahoma","40","bold"))
    bt_title.pack(side="top")
    
    bt_name=tk.Label(login,text="Enter Name:")
    bt_name.pack(side="top")
    
    entry=tk.Entry(login)
    entry.pack(side="top")
    
    bt_credit=tk.Label(login,text="Enter opening credit:")
    bt_credit.pack(side="top")
    
    entry2=tk.Entry(login)
    entry2.pack(side="top")
    
    bt_pin=tk.Label(login,text="Enter desired PIN:")
    bt_pin.pack(side="top")
    
    entry3=tk.Entry(login,show="*")
    entry3.pack(side="top")
    
    bt_submit=tk.Button(login,text="Submit",command=lambda: check_log_in(login,entry.get().strip(),entry2.get().strip(),entry3.get().strip()))
    bt_submit.pack(side="top")

    bt_home=tk.Button(text="HOME",command=lambda: home_return(login))
    bt_home.pack(side="top")
    
    login.bind("<Return>",lambda x:check_log_in(login,entry.get().strip(),entry2.get().strip(),entry3.get().strip()))
    return

def Create():
    create=tk.Tk()
    create.geometry("500x250")
    create.title("Create Account")
    
    bt_title=tk.Message(create,text="Create Account",width=2000,padx=600,pady=0,anchor="center")
    bt_title.config(font=("Tahoma","40","bold"))
    bt_title.pack(side="top")
    
    bt_name=tk.Label(create,text="Enter Name:")
    bt_name.pack(side="top")
    
    entry=tk.Entry(create)
    entry.pack(side="top")
    
    bt_credit=tk.Label(create,text="Enter opening credit:")
    bt_credit.pack(side="top")
    
    entry2=tk.Entry(create)
    entry2.pack(side="top")
    
    bt_pin=tk.Label(create,text="Enter desired PIN:")
    bt_pin.pack(side="top")
    
    entry3=tk.Entry(create,show="*")
    entry3.pack(side="top")
    
    bt_submit=tk.Button(create,text="Submit",command=lambda: write(create,entry.get().strip(),entry2.get().strip(),entry3.get().strip()))
    bt_submit.pack(side="top")
    
    create.bind("<Return>",lambda x:write(create,entry.get().strip(),entry2.get().strip(),entry3.get().strip()))
    return


def Main_Menu():
    main=tk.Tk()
    main.geometry("1000x500")
    main.title("Bank Accountant")

    bt_title=tk.Message(text="Bank Account",width=2000,padx=600,pady=0,anchor="center")
    bt_title.config(font=("Tahoma","50","bold"))
    bt_title.pack(side="top")
    
    bt_create=tk.Button(main,text='CREATE NEW ACCOUNT',command=Create)
    bt_create.config(font=("Tahoma","20","bold"))
    bt_create.place(x=340,y=250)

    bt_login=tk.Button(main,text='LOGIN',command=lambda: log_in(main))
    bt_login.config(font=("Tahoma","20","bold"))
    bt_login.place(x=450,y=150)

    bt_close=tk.Button(main,text='Close',command=main.destroy)
    bt_close.config(font=("Tahoma","20","bold"))
    bt_close.place(x=450,y=400)
    
    main.mainloop()

Main_Menu()
