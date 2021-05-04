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
engine.say("Welcome to Ali's Instagram Bot")
engine.runAndWait()

window = tk.Tk()
window.title("Instagram Bot by Ali")
window.geometry("800x400")
window.configure(bg="#494949")

tk.Label(window, text="Welcome", font=(
    "Gill Sans", 36), bg="#F0FF00").pack(pady=10)
tk.Label(window, text="Type the text :- ",
         font=("Gill Sans", 20), bg="#00FAFA").pack(pady=10)
ent1 = tk.Text(window)
ent1.place(x=10, y=120, height=100, width=750)

tk.Label(window, text="Enter usernames:- ",
         font=("Gill Sans", 20), bg="#00FAFA").place(x=20, y=240)
ent2 = tk.Entry(window)
ent2.place(x=350, y=240, width=300)

tk.Label(window, text="Your username:-",
         font=("Gill Sans", 20), bg="#00FAFA").place(x=20, y=280)
ent3 = tk.Entry(window)
ent3.place(x=20, y=320)

tk.Label(window, text="Your password:-",
         font=("Gill Sans", 20), bg="#00FAFA").place(x=350, y=280)
ent4 = tk.Entry(window, show="*")
ent4.place(x=350, y=320)

button1 = tk.Button(window, text="SUBMIT",
                    font=("Gill Sans", 20), bg="#18D848",
                    command=login)
button1.place(x=350, y=360)  # pack issue
window.mainloop()

# when our program ends it will show "done".
input("DONE")
