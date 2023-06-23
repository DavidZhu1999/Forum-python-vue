import sqlite3

conn = sqlite3.connect('model/datas.db', check_same_thread=False, isolation_level=None)
db = conn.cursor()
