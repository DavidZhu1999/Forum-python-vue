from . import db
import time

sql = '''CREATE TABLE IF NOT EXISTS userinfo(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT,
            password TEXT)'''
db.execute(sql)

sql = '''CREATE TABLE IF NOT EXISTS emailverify(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            verifycode TEXT,
            addtime TEXT)'''
db.execute(sql)


def exist_user_email(email):
    return len(db.execute(f"SELECT email FROM userinfo WHERE email='{email}'").fetchall()) > 0


def exist_user_username(username):
    return len(db.execute(f"SELECT username FROM userinfo WHERE username='{username}'").fetchall()) > 0


def insert_verifycode(email, verifycode):
    if len(db.execute(f"SELECT email FROM emailverify WHERE email = '{email}'").fetchall()) > 0:
        db.execute(f"DELETE FROM emailverify WHERE email = '{email}'")
    ticks = time.time()
    db.execute(f"INSERT INTO emailverify (email, verifycode, addtime) VALUES('{email}', '{verifycode}', '{ticks}')")
    return 1


def search_verifycode(email):
    return db.execute(f"SELECT verifycode, addtime FROM emailverify WHERE email = '{email}'").fetchall()


def insert_user(username, email, password):
    if len(db.execute(f"SELECT email "
                      f"FROM userinfo "
                      f"WHERE email='{email}'").fetchall()) > 0:
        return -1
    if len(db.execute(f"SELECT username "
                      f"FROM userinfo "
                      f"WHERE username='{username}'").fetchall()) > 0:
        return -2
    db.execute(f"INSERT INTO userinfo (username, email, password) VALUES('{username}', '{email}', '{password}')")
    return 1


def delete_verifycode(email):
    db.execute(f"DELETE FROM emailverify WHERE email = '{email}'")
    return 1


def check_user(email, password):
    if len(db.execute(f"SELECT email "
                      f"FROM userinfo "
                      f"WHERE email='{email}' AND password='{password}'").fetchall()):
        return 1
    return -1


def return_username(email):
    username = db.execute(f"SELECT username FROM userinfo WHERE email = '{email}'").fetchall()
    print(username)
    return username

def return_email(username):
    email =  db.execute(f"SELECT email FROM userinfo WHERE username = '{username}'").fetchall()
    print(email)
    return email

def change_password(email,password):
    db.execute(f"UPDATE userinfo SET password = '{password}' WHERE email = '{email}';")