from flask import Flask
import pymysql
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    count = request.args.get('count')
    cursor.execute("select * from image where imageNam like '%{}%'".format(keyword))
    data = cursor.fetchmany(int(count))
    return render_template('/index.html', images=data)

if __name__ == '__main__':
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='root',
        db='test',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )

    cursor = conn.cursor()

    app.run()