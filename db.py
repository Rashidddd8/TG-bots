import mysql.connector
import smtplib
from config import *


def send_data(data):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()

    smtpObj.login(mail, mail_pass)
    smtpObj.sendmail(mail, catchers_mail, data.encode('utf-8'))

    smtpObj.quit()

def create_user(idtg, usernametg, firstname, lastname):
    if not firstname:
        firstname = 'Null'
    if not lastname:
        lastname = 'Null'
    data = [idtg, usernametg, firstname, lastname]
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=password_python, database=database_name)
    mycursor = mydb.cursor()
    sql = "INSERT IGNORE INTO Users (IDTG, UsernameTG, FirstNameTG, LastNameTG) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql, data)
    mydb.commit()
    mycursor.close()
    mydb.close()

def create_application(idtg, fio, home, birth, number, comment, name1="ФИО : ", name3="Прописка : ", name2="Дата рождения : ", name4="Номер телефона : ", name5="Комментарий : "):
    data = [idtg, fio, home, birth, number, comment]
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=password_python, database=database_name)
    mycursor = mydb.cursor()
    sql = "INSERT INTO Applications (IDTG, FIO, Home, Birth, PhoneNumber, Comment) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, data)
    mydb.commit()
    mycursor.close()
    mydb.close()
    data_string = f"\n{name1}\n{fio}\n{name2}\n{home}\n{name3}\n{birth}\n{name4}\n{number}\n{name5}\n{comment}"
    send_data(data_string)

def create_record_btns_table(buttonName, userTGID, datetime):
    data = [buttonName, userTGID, datetime]
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=password_python, database=database_name)
    mycursor = mydb.cursor()
    sql = "INSERT INTO Buttons (ButtonName, UserTGID, DateTime) VALUES (%s, %s, %s)"
    mycursor.execute(sql, data)
    mydb.commit()
    mycursor.close()
    mydb.close()


# Эта функция пока не пригодилась
#def get_last_application():
#    #SELECT * FROM Applications ORDER BY UniqID DESC LIMIT 1;
#    mydb = mysql.connector.connect(host=host_name, user=user_name, password=password_python, database=database_name)
#    mycursor = mydb.cursor()
#    mycursor.execute("SELECT * FROM Applications ORDER BY UniqID DESC LIMIT 1")
#    myresult = mycursor.fetchall()
#    print(myresult)
#    print(type(myresult))
#    for el in myresult:
#        print(el)


if __name__ == '__main__':
    pass
