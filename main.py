from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10)) ]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for let in range(randint(2, 4)) ]
    # for let in range(nr_letters):
    #     password_lst += random.choice(letters)
    # for symb in range(nr_symbols):
    #     password_lst += random.choice(symbols)
    # for num in range(nr_numbers):
    #     password_lst += random.choice(numbers)
    password_lst = password_letters + password_numbers + password_symbols
    shuffle(password_lst)
    password = "".join(password_lst)
    # password = ''
    # for char in password_lst:
    #     password += char
    entry_password.insert(0, password)
    pyperclip.copy(password)      # автоматически сохраняет в буфер обмена пароль
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = entry_web.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ошибка", message="Введите данные")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"Детали ввода: \nEmail: {email}"
                               f"\nPassword: {password} \nСохранять?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # data_file.write(f"{website} | {email} | {password}\n")
                    # Reading
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                    # Updating
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving
                    json.dump(data, data_file, indent=4)

            finally:
                entry_web.delete(0, END)
                entry_password.delete(0, END)

# ---------------------------- Find Password ------------------------------- #
def find_password():
    website = entry_web.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Ошибка!!!", message="Нет данных!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Ошибка!!!", message=f"Нет данных {website}")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_web = Label(text="Website: ")
label_web.grid(column=0, row=1)

label_email = Label(text="Email/Username: ")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

#buttons
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

button_password = Button(text="Generate Password ", command=generate_password)
button_password.grid(column=2, row=3)

button_add = Button(text="Add", width=44, command=save)
button_add.grid(column=1, row=4, columnspan=2)

entry_web = Entry(width=33)
entry_web.grid(column=1, row=1)
entry_web.focus()

entry_email = Entry(width=52)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "igor@gmail.com")

entry_password = Entry(width=33)
entry_password.grid(column=1, row=3)




window.mainloop()