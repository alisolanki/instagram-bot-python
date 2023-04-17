# importing module
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
#STO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import tkinter as tk
from tkinter import messagebox
import pyttsx3
import customtkinter

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/")


def login():
    try:
        if ent4.get() != str(ent4.get()):
            pass
    except:
        tk.messagebox.showerror(
            title="FAILED",
            message="\t\t Oops! \n You have entered wrong value. Numbers can't be text values!!! \n BYE"
        )
        driver.close

    tk.messagebox.showinfo(
        title="SUCCESS",
        #message=f"\t\tCongratulations!\n\n You are sending {str(ent3.get('1.0', tk.END))} text to {str(ent4.get())}"
        message=f"  Congratulations!"
    )

    print('5')
    #driver.get('https://www.instagram.com/')

    username = str(ent1.get())
    password = str(ent2.get())
    #message = str(ent3.get('1.0', tk.END))
    message = str(ent3.get())
    user = str(ent4.get()).split()

    enter_username = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'username')))
    enter_username.send_keys(username)
    enter_password = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'password')))
    enter_password.send_keys(password)
    enter_password.send_keys(Keys.RETURN)
    time.sleep(30)

        # first pop-up
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    time.sleep(2)

    # 2nd pop-up
    driver.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    time.sleep(2)

    # direct button
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    time.sleep(3)

    # clicks on pencil icon
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
    time.sleep(2)
    for i in user:

        # enter the username
        driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
        time.sleep(2)

        # click on the username
        driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
        time.sleep(2)

        # next button
        driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
        time.sleep(3)

        # click on message area
        send = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

        # types message
        send.send_keys(message)
        time.sleep(1)

        # send message
        send.send_keys(Keys.RETURN)
        time.sleep(2)

        # clicks on direct option or pencl icon
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
        time.sleep(2)

        



engine = pyttsx3.init()
engine.say("Welcome to Instagram Bot")
engine.runAndWait()

#*********************************************************
#<<<<<<<<<<<<<<<<<< ---- NEW UI ----- >>>>>>>>>>>>>>>>>>>>>
#*********************************************************


window = customtkinter.CTk()  # created CTk window like the Tk window
window.geometry("1000x600")
window.minsize(1000,600)
window.maxsize(1000,600)

window.title("Instagram DM Bot")
#window.iconbitmap('c:/bot/insta.ico')
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Grid configure(9x5)
window.grid_rowconfigure((0,2,4,6,8),weight= 3)#widget rows
window.grid_rowconfigure((1,3,5,7,9),weight= 1)#space rows(maybe use padding)
window.grid_columnconfigure((1,2,3,4), weight= 2)


#--0.0-------HEADER-----------
text_var1 = tk.StringVar(value="INSTA DM BOT")

label1 = customtkinter.CTkLabel(master=window,
                               textvariable=text_var1,
                               width=120,
                               height=25,
                               font=("Gilroy",56),
                               text_color="white",
                               fg_color=("transparent"),
                               corner_radius=8).grid(row=0,column=0, columnspan=5)
#label1.pack(padx=40, pady=20)
#label1.place(relx=0.5, rely=0.05, anchor=tk.CENTER)


#--1.0--------YOUR USERNAME------------

frame1=customtkinter.CTkFrame(master=window, width=300, height=80).grid(row=2,column=2,sticky="w")
#frame1.pack(padx=10, pady=10)

#-----Your username Label
#text_var1 = tk.StringVar(value="Your username")

label1 = customtkinter.CTkLabel(master=frame1,
                               text="Your username",
                               width=120,
                               height=25,
                               font=("Calibri",24),
                               text_color="white",
                               fg_color=("gray17"))
#.grid(row=1, column=2)
label1.place(relx=0.12, rely=0.15)  #, anchor=tk.CENTER)

#-----Your username entry box
ent1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Enter your username",
                                height=35,
                                width=200)
ent1.place(relx=0.12, rely=0.21)

#--2.0-------YOUR PASSWORD------------

frame2=customtkinter.CTkFrame(master=window, width=300, height=80).grid(row=2, column=3, sticky="e") 
#-----Your password Label

label2 = customtkinter.CTkLabel(master=frame2,
                               text="Your Password",
                               width=120,
                               height=25,
                               font=("Calibri",24),
                               text_color="white",
                               fg_color=("gray17") )
label2.place(relx=0.7, rely=0.174, anchor=tk.CENTER)

#-----Your password entry box
ent2 = customtkinter.CTkEntry(master=frame2, placeholder_text="Enter your password",
                                height=35,
                                width=200, show="*")
ent2.place(relx=0.62, rely=0.21)


#--3.0-----TYPE TEXT----------
frame3=customtkinter.CTkFrame(master=window, width=800, height=170).grid(row=4, column=1, columnspan=4)
#-----Message Label

label3 = customtkinter.CTkLabel(master=frame3,
                               text="Enter the message",
                               width=120,
                               height=25,
                               font=("Calibri",24),
                               text_color="white",
                               fg_color=("gray17") )
label3.place(relx=0.13, rely=0.325)

#-----Message entry box
ent3 = customtkinter.CTkEntry(master=frame3, 
                                placeholder_text="Enter message to be sent",
                                width=750,
                                height=100,
                                )
ent3.place(relx=0.12, rely=0.38, anchor=tk.NW)


#--4.0-------ENTER  RECIEPENT'S  USERNAME-------------
frame4=customtkinter.CTkFrame(master=window, width=700, height=150).grid(row=6, column=2, columnspan=4, sticky="w")
#-----Reciever username Label

label4 = customtkinter.CTkLabel(master=frame4,
                               text="Reciepent's usernames",
                               width=120,
                               height=25,
                               font=("Calibri",24),
                               text_color="white",
                               fg_color=("gray17") )
#label4= customtkinter.CTkLabel(master=frame4, text="CTkRadioButton Group:")
label4.place(relx=0.24, rely=0.64, anchor=tk.CENTER)

#-----Reciever username entry box
ent4 = customtkinter.CTkEntry(master=frame4, placeholder_text="Enter reciepent's username(s)",
                                height=80,
                                width=500)
ent4.place(relx=0.12, rely=0.68)


#--5.0-------SUBMIT BUTTON----------

button1 = customtkinter.CTkButton(master=window,
                                 fg_color="#125488",
                                 width=160,
                                 height=60,
                                 font=("Gill Sans", 20),
                                 border_width=0,
                                 corner_radius=8,
                                 text=" GO ",
                                 command=login
                                ).grid(row=8, column=0, columnspan=5)


window.mainloop()

# when our program ends it will show "done".
input("DONE")