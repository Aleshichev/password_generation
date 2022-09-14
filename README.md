# Генератор паролей  (Tkinter – графический проект)
Программа умеет сохранять, генерировать и искать пароли.
Пользователь может ввести сайт, почту и свой пароль или сгенерировать пароль автоматически.
Все данные сохраняються в json файл. Также пользователь может ввести имя сайта и найти нужную информацию о сохранённом ранее пароле.
## Используемые ресурсы,  модули и библиотеки:  
-	tkinter, 
-	random, 
-	json,
-	pyperclip, 
-	messagebox
## Графическое отображение 
![logo](https://github.com/Aleshichev/password_generation/blob/main/photo/1.png)
## Структура проекта
Для удобства управления данными создано 3 константы данных, 3 функции, Ui структура и логика отображения программы.
## Процесс 
1.	Пользователю открывается окно, в котором отображено 3 строки для ввода информации **Website**, **Email**, **Password** и три функциональные кнопки **Search**, **Generate Password**, **Add**.
2.	Если пользователь заполняет все строки и нажимает кнопку **Add** - то программа обращаеться к функции **def  save()**, которая сохраняет полученную информацию в **json** файл (если файла нет – создаёт файл, если файл есть – обновляет его).
3.	Если пользователь не может придумать пароль, он может нажать на кнопку **Generate Password**. Программа обратиться к функции **def  generate_password()**  и отобразит рандомный сложный пароль,  состоящий из букв, цифр и символов.
4.	Также программа помогает легко найти из базы сохранённых паролей необходимый. Нужно указать имя сайта и нажать **Search**. Программа выполнит функцию **def find_password()** и в всплывающем окне появятся нужные данные.
## Функциональные особенности
+ При генерации или поиске пароля программа (для удобства) автоматически сохраняет пароль в буфер обмена, который сразу можно вводить в нужное поле регистрации нажав Ctrl+V.
+ Всплывающие окна: 
  - Запрос о подтверждении сохранения данных.
  - Сообщение об ошибке: если пользователь ввёл не всю информацию, если данного сайта нет.
  
![logo](https://github.com/Aleshichev/password_generation/blob/main/photo/4.png)![logo](https://github.com/Aleshichev/password_generation/blob/main/photo/3.png)



