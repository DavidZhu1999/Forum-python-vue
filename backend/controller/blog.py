import os
import time

from flask import request, Blueprint, jsonify
from flask_cors import CORS

from model.blogmodel import *

app_blog = Blueprint('app_blog', __name__, url_prefix='/blog')

CORS(app_blog, supports_credentials=True)


@app_blog.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    introduction = data.get('introduction')
    content = data.get('content')
    email = data.get('email')
    type = data.get('type')
    code = insert_blog(title, author, introduction, content, email, type)
    if code == 1:
        return jsonify({"status": code, "message": "发布成功"})


@app_blog.route('/query')
def query():
    keyword = ""
    data = query_blog(keyword)
    return jsonify({"status": 1, "datas": data})


@app_blog.route('/detail', methods=['POST'])
def detail():
    data = request.get_json()
    id = int(data.get('id'))
    return jsonify({"status": 1, "datas": query_detail(id)})


@app_blog.route('/comment_blog', methods=['POST'])
def comment_blog():
    data = request.get_json()
    id = int(data.get('id'))
    author = data.get('author')
    content = data.get('content')
    print(data)
    code = insert_comment_blog(id, author, content)

    if code == -1:
        return jsonify({"status": code, "message": "博客已被删除"})
    if code == 1:
        return jsonify({"status": code})


@app_blog.route('/comment_review', methods=['POST'])
def comment_review():
    data = request.get_json()
    id = int(data.get('id'))
    author = data.get('author')
    content = data.get('content')
    code = insert_comment_review(id, author, content)
    if code == -1:
        return jsonify({"status": code, "message": "评论已被删除"})
    if code == 1:
        return jsonify({"status": code})


@app_blog.route('/comment_blog_delete', methods=['POST'])
def comment_blog_delete():
    data = request.get_json()
    id = int(data.get('id'))
    print(id)
    code = delete_comment_blog(id)
    if code == 1:
        return jsonify({"status": code})


@app_blog.route('/comment_review_delete', methods=['POST'])
def comment_review_delete():
    data = request.get_json()
    id = int(data.get('id'))
    code = delete_comment_review(id)
    if code == 1:
        return jsonify({"status": code})


@app_blog.route('/blog_delete', methods=['POST'])
def blog_delete():
    data = request.get_json()
    id = int(data.get('id'))
    print(id)
    code = delete_blog(id)
    if code == 1:
        return jsonify({"status": code})


@app_blog.route('/blog_author', methods=['POST'])
def blog_author():
    data = request.get_json()
    author = data.get('username')
    returndatas = query_blog_author(author)
    return jsonify({"status": 1, "datas": returndatas})


# 上传图片
@app_blog.route('/upload_image', methods=['POST'])
def upload_image():
    file = request.files.get('image')
    filename = str(time.time()) + "." + file.filename.split('.')[-1]
    file.save("images" + os.path.sep + filename)
    return f"http://localhost:8900/{filename}"

