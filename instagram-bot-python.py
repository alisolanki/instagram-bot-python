# importing module
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import tkinter as tk
from tkinter import messagebox
import pyttsx3
import customtkinter

driver = webdriver.Chrome(ChromeDriverManager().install())


def login():
    try:
        if ent2.get() != str(ent2.get()):
            pass
    except:
        tk.messagebox.showerror(
            title="FAILED",
            message="\t\t Oops! \n You have entered wrong value. Numbers can't be text values!!! \n BYE"
        )
        driver.close

    tk.messagebox.showinfo(
        title="SUCCESS",
        message=f"\t\tCongratulations!\n\n You are sending {str(ent1.get('1.0', tk.END))} text to {str(ent2.get())}"
    )

    print('5')
    driver.get('https://www.instagram.com/')

    username = str(ent3.get())
    password = str(ent4.get())
    message = str(ent1.get('1.0', tk.END))
    user = str(ent2.get()).split()

    enter_username = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'username')))
    enter_username.send_keys(username)
    enter_password = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'password')))
    enter_password.send_keys(password)
    enter_password.send_keys(Keys.RETURN)
    time.sleep(5)

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
#<<<<<<<<<<<<<<<<<<---- NEW UI ----- >>>>>>>>>>>>>>>>>>>>>
#*********************************************************


window = customtkinter.CTk()  # create CTk window like you do with the Tk window
window.geometry("1000x600")
window.title("Instagram Messenger Bot")
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#--0.0-------WELCOME-----------
text_var1 = tk.StringVar(value="WELCOME")

label1 = customtkinter.CTkLabel(master=window,
                               textvariable=text_var1,
                               width=120,
                               height=25,
                               font=("Harrington",56),
                               text_color="white",
                               fg_color=("transparent"),
                               corner_radius=8)
#label1.pack(padx=40, pady=20)
label1.place(relx=0.5, rely=0.05, anchor=tk.CENTER)


#--1.0--------YOUR USERNAME------------
#---Your username Label
text_var1 = tk.StringVar(value="Your username")

label1 = customtkinter.CTkLabel(master=window,
                               textvariable=text_var1,
                               width=120,
                               height=25,
                               font=("Calibri",24),
                               text_color="white",
                               fg_color=("transparent"),
                               corner_radius=8)
#label1.pack(padx=40, pady=20)
label1.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

#---Your username entry box
ent1 = customtkinter.CTkEntry(master=window, placeholder_text="Enter your username",
                                height=35,
                                width=200)
#entry1.pack(padx=20, pady=10)
ent1.place(relx=0.12, rely=0.25)


#--2.0-------YOUR PASSWORD------------
#---Your password Label
text_var2 = tk.StringVar(value="Your Password")

label2 = customtkinter.CTkLabel(master=window,
                               textvariable=text_var2,
                               width=120,
                               height=25,
                               font=("Calibri",24),
                               text_color="white",
                               fg_color=("transparent"),
                               corner_radius=8)
#label2.pack(padx=40, pady=20)
label2.place(relx=0.6, rely=0.2, anchor=tk.CENTER)

#---Your password entry box
ent2 = customtkinter.CTkEntry(master=window, placeholder_text="Enter your password",
                                height=35,
                                width=200)
#entry2.pack(padx=20, pady=10)
ent2.place(relx=0.52, rely=0.25)


#--3.0-----TYPE TEXT----------
#---Message Label

text_var3 = tk.StringVar(value="Enter the message")

label3 = customtkinter.CTkLabel(master=window,
                               textvariable=text_var3,
                               width=120,
                               height=25,
                               font=("Calibri",24),
                               text_color="white",
                               fg_color=("transparent"),
                               corner_radius=8)
#label3.pack(padx=400, pady=200)
label3.place(relx=0.1, rely=0.325)

#---Message entry box
ent3 = customtkinter.CTkEntry(master=window, 
                                placeholder_text="Enter message to be sent",
                                width=750,
                                height=100,
                                )
#entry3.pack(padx=200, pady=100)
ent3.place(relx=0.12, rely=0.4, anchor=tk.NW)


#--4.0-------ENTER  RECIEPENT'S  USERNAME-------------
#---Reciever username Label
text_var4 = tk.StringVar(value="Reciepent's usernames")

label4 = customtkinter.CTkLabel(master=window,
                               textvariable=text_var4,
                               width=120,
                               height=25,
                               font=("Calibri",24),
                               text_color="white",
                               fg_color=("transparent"),
                               corner_radius=8)
#label4.pack(padx=40, pady=20)
label4.place(relx=0.24, rely=0.62, anchor=tk.CENTER)

#---Reciever username entry box
ent4 = customtkinter.CTkEntry(master=window, placeholder_text="Enter reciepent's username(s)",
                                height=60,
                                width=400)
#entry4.pack(padx=40, pady=20)
ent4.place(relx=0.12, rely=0.675)


#--5.0-------SUBMIT BUTTON----------

button1 = customtkinter.CTkButton(master=window,
                                 fg_color="#125488",
                                 width=160,
                                 height=60,
                                 font=("Gill Sans", 20),
                                 border_width=0,
                                 corner_radius=8,
                                 text=" GO ",
                                command=button_event
                                )
button1.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

window.mainloop()

# when our program ends it will show "done".
input("DONE")