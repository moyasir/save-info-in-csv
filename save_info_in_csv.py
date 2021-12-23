# python tkinter tutorial
# tee-kinter, tk-inter, kinter

# starting code
# import tkinter
# from tkinter import *
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
window = tk.Tk()
window.title('Python GUI App')

# create labels
name_label = tk.Label(window, text='Enter your name: ')
name_label.grid(row=0,column=0,sticky=tk.W)

email_label = tk.Label(window, text='Enter your email: ')
email_label.grid(row=1,column=0,sticky=tk.W)

age_label = tk.Label(window, text='Enter your age: ')
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label = tk.Label(window, text='Select your gender')
gender_label.grid(row=3,column=0,sticky=tk.W)


# create entry box
#pack(), grid() ---> widgets
name_var = tk.StringVar()
name_entry_box = ttk.Entry(window, width=16, textvariable = name_var)
name_entry_box.grid(row=0,column=1)
name_entry_box.focus()

email_var = tk.StringVar()
email_entry_box = ttk.Entry(window, width=16, textvariable = email_var)
email_entry_box.grid(row=1,column=1)

age_var = tk.StringVar()
age_entry_box = ttk.Entry(window, width=16, textvariable = age_var)
age_entry_box.grid(row=2,column=1)

# create combo box
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(window, width=14, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.grid(row=3,column=1)
gender_combobox.current(0)

# radio button
#student, techer
usertype = tk.StringVar()
radiobtn_student = ttk.Radiobutton(window, text='Student', value='Student',variable=usertype)
radiobtn_student.grid(row=4,column=0)

radiobtn_teacher = ttk.Radiobutton(window, text='Teacher', value='Teacher',variable=usertype)
radiobtn_teacher.grid(row=4,column=1)

#check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(window, text='Agree with our privacy policy.', variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3)

# button
# def action():
#     user_name = name_var.get()
#     user_email = email_var.get()
#     user_age = age_var.get()
#     # print(f'{user_name} is {user_age} years old, {user_email}.')
#     user_gender = gender_var.get()
#     user_type = usertype.get()
#     if checkbtn_var.get() == 0:
#         agreed = 'No'
#     else:
#         agreed = 'Yes'
#     # print(user_gender, user_type, subscribed)

#     with open('file.txt', 'a') as f:
#         f.write(f'Name: {user_name}\n')
#         f.write(f'Email: {user_email}\n')
#         f.write(f'Age: {user_age}\n')
#         f.write(f'Gender: {user_gender}\n')
#         f.write(f'Type: {user_type}\n')
#         f.write(f'Agreed: {agreed}\n')
#         f.write('-------------\n')


# for write to csv file
def action():
    user_name = name_var.get()
    user_email = email_var.get()
    user_age = age_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        agreed = 'No'
    else:
        agreed = 'Yes'
        
    # for csv
    with open('file.csv', 'a',newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['User Name','User Email','User Age','User Gender','User Type','Agreed'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'User Name' : user_name,
            'User Email' : user_email,
            'User Age' : user_age,
            'User Gender' : user_gender,
            'User Type' : user_type,
            'Agreed' : agreed
        })

    name_entry_box.delete(0, tk.END)
    email_entry_box.delete(0, tk.END)
    age_entry_box.delete(0, tk.END)
    name_label.configure(foreground='blue')
    email_label.configure(foreground='blue')
    age_label.configure(foreground='blue')
submit_button = ttk.Button(window, text='Submit', command=action)
submit_button.grid(row=6,column=0)

window.mainloop()
