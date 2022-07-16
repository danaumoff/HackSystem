import sqlite3
import hashlib
from tkinter import *
from tkinter import messagebox as mb
import requests
from bs4 import BeautifulSoup

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(32),
    name VARCHAR(32),
    password VARCHAR(64)
    )""")

def insert_user_sql(login, name, password ):
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    md5_password = hashlib.md5(password.encode())
    cursor.execute("""INSERT INTO users (login, name, password) VALUES (?, ?, ?)""", [login, name, md5_password.hexdigest()])
    connect.commit()
    connect.close()


def TK_autorize():
    def menu():
        autorize.destroy()
        menu = Tk()
        menu.iconbitmap("icon.ico")
        menu.geometry("800x600")
        menu.resizable(0, 0)
        menu.title("HackerSystem")

        def get_weather():
            city_id = 578072
            appid = "75b6b6bf8c7775c44dc00cb28f622ea8"
            try:
                res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                        params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
                data = res.json()
                mb.showinfo("HackerSystem", "Погода в Белгороде:\n" + str(data['weather'][0]['description'].title()) + "\n" + str(data['main']['temp']) + "C°")
                
            except Exception as e:
                mb.showerror("Ошибка", "Проверьте подключение к интернету!")
         

            
        
        
        def currency():
            menu.destroy()
            currency = Tk()
            currency.title("HackerSystem")
            currency.iconbitmap("icon.ico")
            currency.geometry("800x600")
            currency.resizable(0, 0)

            def usd_currency():
                URL = 'https://ru.investing.com/currencies/usd-rub'
                HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.61'}
                page = requests.get(URL, headers = HEADERS)
                soup = BeautifulSoup(page.content, 'html.parser')
                currency = soup.find(id = 'last_last')
                dollar = currency.text[0:4] + " Руб"
                mb.showinfo("HackerSystem", "Курс доллара " + dollar)
            
            def eur_currency():
                URL = 'https://ru.investing.com/currencies/eur-rub'
                HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.61'}
                page = requests.get(URL, headers = HEADERS)
                soup = BeautifulSoup(page.content, 'html.parser')
                currency = soup.find(id = 'last_last')
                eur = currency.text[0:4] + " Руб"
                mb.showinfo("HackerSystem", "Курс евро " + eur)
            
            def kzt_currency():
                URL = 'https://ru.investing.com/currencies/kzt-rub'
                HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.61'}
                page = requests.get(URL, headers = HEADERS)
                soup = BeautifulSoup(page.content, 'html.parser')
                currency = soup.find(id = 'last_last')
                kzt = currency.text[0:4] + " Руб"
                mb.showinfo("HackerSystem", "Курс тенге " + kzt)
            
            def cny_currency():
                URL = 'https://ru.investing.com/currencies/cny-rub'
                HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.61'}
                page = requests.get(URL, headers = HEADERS)
                soup = BeautifulSoup(page.content, 'html.parser')
                currency = soup.find(id = 'last_last')
                cny = currency.text[0:4] + " Руб"
                mb.showinfo("HackerSystem", "Курс юань " + cny)
            
            def uah_currency():
                URL = 'https://ru.investing.com/currencies/uah-rub'
                HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.61'}
                page = requests.get(URL, headers = HEADERS)
                soup = BeautifulSoup(page.content, 'html.parser')
                currency = soup.find(id = 'last_last')
                uah = currency.text[0:4] + " Руб"
                mb.showinfo("HackerSystem", "Курс гривны " + uah)

           

            
            
            lblmain = Label(text = "Курсы валют", font = "Calibri 25")
            lblmain.place(x = 300, y = 15)

            btneur = Button(text = "Курс евро", font = "Calibri 18", bg = "black", fg = "white", command =  eur_currency)
            btneur.place(x = 70, y = 105)

            btnusd = Button(text = "Курс доллара", font = "Calibri 18", bg = "black", fg = "white", command = usd_currency)
            btnusd.place(x = 70, y = 185)

            btnkzt = Button(text = "Курс тенге", font = "Calibri 18", bg = "black", fg = "white", command = kzt_currency)
            btnkzt.place(x = 70, y = 265)

            btncny = Button(text = "Курс юань", font = "Calibri 18", bg = "black", fg = "white", command = cny_currency)
            btncny.place(x = 70, y = 345)

            btnuah = Button(text = "Курс гривны", font = "Calibri 18", bg = "black", fg = "white", command = uah_currency)
            btnuah.place(x = 70, y = 425)
            
        lblmenu = Label(text =  "Добро пожаловать в HackerSystem!", font = "Calibri 25")
        lblmenu.place(x = 150, y = 15)

        weatherbtn = Button(text = "Погода", font =  "Calibri 18", bg = "black", fg = "white", command = get_weather)
        weatherbtn.place(x = 70, y = 105)

        currencybtn = Button(text = "Курсы валют", font = "Calibri 18", bg = "black", fg = "white", command = currency)
        currencybtn.place(x = 70, y = 170)

        btndonttouchit = Button(text = "Не нажимай!", font = "Calibri 10", bg = "black", fg = "white", command = dont_touch_it)
        btndonttouchit.place(x = 70, y = 500)
        
    def enter_sql():
        login = entlogin1.get().strip()
        password = entpassword1.get().strip()
        connect = sqlite3.connect("users.db")
        cursor = connect.cursor()
        md5_password = hashlib.md5(password.encode())
        user_sql = cursor.execute("""SELECT * FROM users WHERE login = (?) AND password = (?)""", [login, md5_password.hexdigest()])
        acc = user_sql.fetchall()
        if len(acc) == 1:
            name = acc[0][2]
            mb.showinfo("Вход", "Здраствуйте, " + name)
            connect.commit()
            connect.close()
            menu()
        else:
            mb.showerror("Ошибка", "Проверьте правильность ввода данных")
        
    
    root.destroy()
    
    autorize = Tk()
    autorize.iconbitmap("icon.ico")
    autorize.geometry("800x600")
    autorize.resizable(0, 0)
    autorize.title("Авторизация")
    
    lblmain = Label(text =  "Авторизация", font = "Calibri 25")
    lblmain.place(x = 300, y = 15)

    lbllogin1 = Label(text = "Логин:", font = "Calibri 18")
    lbllogin1.place(x = 200, y = 75)
    entlogin1 = Entry(width = 20, font = "Calibri 18", bg = "gray")
    entlogin1.place(x = 280, y = 75)

    lblpassword1 = Label(text = "Пароль:", font = "Calibri 18")
    lblpassword1.place(x = 185, y = 120)
    entpassword1 = Entry(width = 20, font = "Calibri 18", bg = "gray")
    entpassword1.place(x = 280, y = 120)

    btnok = Button(text = "Войти", font = "Calibri 18", command = enter_sql)
    btnok.place(x = 360, y = 160)
    
    autorize.mainloop()
    

def reg():
    login = entlogin.get().strip()
    name = entname.get().strip()
    password = entpassword.get().strip()
    password1 = entpassword1.get().strip()
    if login == "" or name == "" or password == "" or password1 == "":
        mb.showerror("Ошибка", "Данные заполнены не полностью")
    if login == password:
        mb.showerror("Ошибка", "Логин не может быть идентичен с паролем")
    elif password != password1:
        mb.showerror("Ошибка", "Пароли не идентичны")
    else:
        insert_user_sql(login, name, password)
        mb.showinfo("Успешно", "Вы успешно зарегистрировались")
    


root = Tk()
root.iconbitmap("icon.ico") 
root.geometry("800x600")
root.resizable(0, 0)
root.title("Регистрация")

lblmain = Label(text = "Регистрация", font = "Calibri 25")
lblmain.place(x = 300, y = 15)

lbllogin = Label(text = "Логин:", font = "Calibri 18")
lbllogin.place(x = 200, y = 75)
entlogin = Entry(width = 20, font = "Calibri 18", bg = "gray")
entlogin.place(x = 280, y = 75)

lblname = Label(text = "Имя:", font = "Calibri 18")
lblname.place(x = 220, y = 120)
entname = Entry(width = 20, font = "Calibri 18", bg = 'gray')
entname.place(x = 280, y = 120)

lblpassword = Label(text = "Пароль:", font = "Calibri 18")
lblpassword.place(x = 185, y = 165)
entpassword = Entry(width = 20, font = "Calibri 18", bg = "gray")
entpassword.place(x = 280, y = 165)

lblpassword1 = Label(text = "Повторите пароль:", font = "Calibri 18")
lblpassword1.place(x = 75, y = 210)
entpassword1 = Entry(width = 20, font = "Calibri 18", bg = "gray")
entpassword1.place(x = 280, y = 210)

lblhaveacc = Label(text = "Уже есть аккаунт?", font = "Calibri 12")
lblhaveacc.place(x = 250, y = 360)
btnhaveacc = Button(text = "Авторизация", font = "Calibri 9", command = TK_autorize)
btnhaveacc.place(x = 380, y = 360)



btnok = Button(text = "Отправить", font = "Calibri 18", command = reg)
btnok.place(x = 330, y = 260 )


root.mainloop()


