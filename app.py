import time

from flask import Flask, jsonify, send_file

import main
from log import add_log, get_logs
from scripts.func import move_and_click
from key import get_key, update_key, add_key, RUN_ING, RUN_OVER
app = Flask(__name__)

@app.route('/')
def hello():
    return ("<h1>"
            "<a href='/open'>开启</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href='/close'>关闭</a><br/>"
            "<a href='/now'>当前截图</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href='/log'>日志</a><br/>"
            "<a href='/activity'>待办任务</a>"
            "</h1>")

@app.route('/open')
def open():
    run_boo = get_key("run")
    if run_boo.value == RUN_ING:
        return "执行中"
    update_key("run", RUN_ING)
    main.run()
    return "开启"

@app.route('/close')
def close():
    update_key("run", RUN_OVER)
    return "关闭中"



@app.route('/now')
def now():
    from scripts.func import capture_screen
    from log import get_uuid
    img = capture_screen()
    img_name = get_uuid()
    img.save(f"img/{img_name}.png")
    return send_file(f"img/{img_name}.png", mimetype='image/png')

@app.route('/activity')
def acti():
    from activity import get_todo_activities
    activities = get_todo_activities()
    content = ""
    for each in activities:
        content += f"待办任务: {each.name}, 开始时间: {each.start_time}, 脚本名称: {each.script_name}<br/>---------------------------------<br/>"
    if not content:
        content = "当前没有待办任务"
    return content



@app.route('/img/<filename>')
def img(filename):
    return send_file(f"img/{filename}.png", mimetype='image/png')

@app.route('/log')
def see_log():
    logs = get_logs()
    content = ""
    for each in logs:
        content += f"{each.text},关联图片地址<a href='/img/{each.pic_add}'>{each.pic_add}</a>,记录时间{each.create_time}<br/>---------------------------------<br/>"
    return content


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

