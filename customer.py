# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 18:43:48 2021

@author: HARSHIT TIWARI
"""

from tkinter import*
from PIL import Image,ImageTk 



class cust_win:
    def __init__(self, root): #constructor
        self.root=root #initialise
        self.root.title("Hotel Management System")
        self.root.geometry("999x620+281+0")
        
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",42,"bold"),bg="black",fg ="cyan",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=999,height=100)
        
        
        
        label_frame=LabelFrame(self.root,relief=RIDGE,bd=2,text="Customer Details",padx=2,font=("times new roman",18,"bold"))
        label_frame.place(x=0,y=101,width=425,height=480)
        
        
        #label ebtry
        cname=Label(label_frame,font=("arial,12,bold"),text="Customer Name",padx=2,pady=3)
        cname.grid(row=0,column=0,sticky=W)
        txtcname=ttk.Entry(label_frame,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=0,column=1)               
        
        
        
        
if __name__== "__main__": #calling object in main fn
    root=Tk()
    obj=cust_win(root)
    root.mainloop() #closing mainloop