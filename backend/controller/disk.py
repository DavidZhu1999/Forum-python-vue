from flask import request, Blueprint, jsonify
from flask_cors import CORS

from model.diskmodel import upload_file, download_file

app_disk = Blueprint('app_disk', __name__, url_prefix='/blog')

CORS(app_disk, supports_credentials=True)


@app_disk.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    username = data.get('username')
    filename = data.get('filename')
    file = data.get('file')
    code = upload_file(username, filename, file)
    if code == 1:
        return jsonify({"status": code, "message": "上传成功"})


@app_disk.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    username = data.get('username')
    filename = data.get('filename')
    return jsonify({"status": 1, "datas": download_file(username, filename)})
