import tkinter as tk
import customtkinter

#root_tk =customtkinter.CTk()

window = customtkinter.CTk()  # create CTk window like you do with the Tk window
window.geometry("900x500")
#window = tk.Tk()
window.title("Instagram Messenger Bot")
#window.configure(bg="#494949")
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#--0.0-------WELCOME-----------
tk.Label(window, text="Welcome", font=(
    "Gill Sans", 36), bg="#6f6f6f").pack(pady=10)


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
entry1 = customtkinter.CTkEntry(master=window, placeholder_text="Enter your username")
#entry1.pack(padx=20, pady=10)
entry1.place(relx=0.12, rely=0.25)


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
entry2 = customtkinter.CTkEntry(master=window, placeholder_text="Enter your password")
#entry2.pack(padx=20, pady=10)
entry2.place(relx=0.52, rely=0.25)


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
label3.place(relx=0.1, rely=0.35, anchor=tk.NW)

#---Message entry box
entry3 = customtkinter.CTkEntry(master=window, placeholder_text="Enter message to be sent")
#entry3.pack(padx=200, pady=100)
entry3.place(relx=0.12, rely=0.425)


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
label4.place(relx=0.24, rely=0.525, anchor=tk.CENTER)

#---Reciever username entry box
entry4 = customtkinter.CTkEntry(master=window, placeholder_text="Enter reciepent's username")
#entry4.pack(padx=40, pady=20)
entry4.place(relx=0.12, rely=0.575)


#--5.0-------SUBMIT BUTTON----------

button1 = customtkinter.CTkButton(master=window,
                                 fg_color="#125488",
                                 width=160,
                                 height=60,
                                 font=("Gill Sans", 20),
                                 border_width=0,
                                 corner_radius=8,
                                 text=" GO ",
                                #command=button_event
                                )
button1.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


window.mainloop()

#check padding of labels and entry boxes