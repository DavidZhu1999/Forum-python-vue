from . import db
import time
from datetime import datetime
import pytz
sql = '''CREATE TABLE IF NOT EXISTS bloginfo(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            introduction TEXT,
            content TEXT,
            email TEXT,
            type TEXT,
            date TEXT)'''
db.execute(sql)
sql = '''CREATE TABLE IF NOT EXISTS blogcommentinfo(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            blog_id INTEGER,
            author TEXT,
            content TEXT)'''
db.execute(sql)
sql = '''CREATE TABLE IF NOT EXISTS commentcommentinfo(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            comment_id INTEGER,
            author TEXT,
            content TEXT)'''
db.execute(sql)


def insert_blog(title, author, introduction, content, email, type):
    print(content)
    tz = pytz.timezone('Asia/Shanghai')  # 东八区
    t = datetime.fromtimestamp(int(time.time()),
                               pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d')
    print(t)
    title=title.replace("'","''")
    author = author.replace("'", "''")
    introduction = introduction.replace("'", "''")
    content = content.replace("'", "''")
    print(content)
    db.execute(f"INSERT INTO bloginfo(title, author, introduction, content, email, type, date) "
               f"VALUES('{title}', '{author}', '{introduction}', '{content}', '{email}', '{type}', '{t}')")
    return 1


def query_blog(keyword):
    if keyword == '':
        datas = db.execute(f"SELECT id, title, author, introduction, content, type, date "
                           f"FROM bloginfo").fetchall()
    else:
        datas = db.execute(f"SELECT id, title, author, introduction, content "
                           f"FROM bloginfo "
                           f"WHERE title LIKE '%{keyword}%' OR introduction LIKE '%{keyword}%' "
                           f"OR content LIKE '%{keyword}%'").fetchall()
    return datas

def query_blog_author(author):
    datas = db.execute(f"SELECT id, title, author, introduction, content,type, date "
                       f"FROM bloginfo "
                       f"WHERE author = '{author}'").fetchall()
    return datas

def query_detail(id):
    datas = {}
    datas['blog'] = db.execute(f"SELECT id, title, author, introduction, content, email "
                               f"FROM bloginfo "
                               f"WHERE id={id}").fetchone()
    blogcomments = db.execute(f"SELECT id, author, content "
                              f"FROM blogcommentinfo "
                              f"WHERE blog_id={datas['blog'][0]}").fetchall()
    datas['comment'] = []
    for blogcomment in blogcomments:
        datas['comment'].append(
            {"comment_id": blogcomment[0], "author": blogcomment[1], "content": blogcomment[2], "review": []})
        commentcomments = db.execute(f"SELECT id, author, content "
                                     f"FROM commentcommentinfo "
                                     f"WHERE comment_id={blogcomment[0]}").fetchall()
        for commentcomment in commentcomments:
            datas['comment'][-1]['review'].append(
                {"review_id": commentcomment[0], "author": commentcomment[1], "content": commentcomment[2]})
    return datas


def insert_comment_blog(id, author, content):
    content = content.replace("'","''")
    if len(db.execute(f"SELECT id "
                      f"FROM bloginfo "
                      f"WHERE id={id}").fetchall()) > 0:
        db.execute(f"INSERT INTO blogcommentinfo(blog_id, author, content) "
                   f"VALUES('{id}', '{author}', '{content}')")
        return 1
    return -1


def delete_comment_blog(id):
    if len(db.execute(f"SELECT id "
                      f"FROM blogcommentinfo "
                      f"WHERE id={id}").fetchall()) > 0:
        db.execute(f"DELETE FROM blogcommentinfo WHERE ID = {id}")
        return 1
    return -1


def insert_comment_review(id, author, content):
    if len(db.execute(f"SELECT id "
                      f"FROM blogcommentinfo "
                      f"WHERE id={id}").fetchall()) > 0:
        db.execute(f"INSERT INTO commentcommentinfo(comment_id, author, content) "
                   f"VALUES('{id}', '{author}', '{content}')")
        return 1
    return -1

def delete_comment_review(id):
    if len(db.execute(f"SELECT id "
                      f"FROM commentcommentinfo "
                      f"WHERE id={id}").fetchall()) > 0:
        db.execute(f"DELETE FROM commentcommentinfo WHERE ID = {id}")
        return 1
    return -1

def delete_blog(id):
    if len(db.execute(f"SELECT id "
                      f"FROM bloginfo "
                      f"WHERE id={id}").fetchall()) > 0:
        db.execute(f"DELETE FROM bloginfo WHERE ID = {id}")
        return 1
    return -1

