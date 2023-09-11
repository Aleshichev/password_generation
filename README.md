# Password Generator (Tkinter - graphical project)
The programme is able to save, generate and search for passwords.
User can enter site, email and password or generate password automatically.
All data is saved in a json file. The user can also enter the site name and search for a previously saved password.
## Resources, modules and libraries used:  
- tkinter, 
- random, 
- json,
- pyperclip, 
- messagebox
## Graphical display
![logo](https://github.com/Aleshichev/password_generation/blob/main/photo/1.png)
## Project structure
3 data constants, 3 functions, Ui structure and programme display logic are created for easy data management.
## Process 
1.	A window is opened to the user, which displays 3 lines for entering information **Website**, **Email**, **Password** and three function buttons **Search**, **Generate Password**, **Add**.
2.	If the user fills in all lines and presses **Add** button, the programme calls **def save()** function, which saves the received information into **json** file (if there is no file - creates a file, if there is a file - updates it).
3. If the user cannot think of a password, he can click on the **Generate Password** button. The programme will call **def generate_password()** and display a random complex password consisting of letters, numbers and symbols.
4 The programme also helps to easily find the necessary password from the database of saved passwords. You need to specify the site name and press **Search**. The programme will execute the **def find_password()** function and the required data will appear in the pop-up window.
## Functional features
+ When generating or searching for a password, the programme (for convenience) automatically saves the password to the clipboard, which can be immediately entered into the required registration field by pressing Ctrl+V.
+ Pop-up windows: 
  - Data saving confirmation request.
  - Error message: if the user has not entered all information, if this site does not exist.
  
![logo](https://github.com/Aleshichev/password_generation/blob/main/photo/4.png)![logo](https://github.com/Aleshichev/password_generation/blob/main/photo/3.png)



