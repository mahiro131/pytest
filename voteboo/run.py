# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import psycopg2
import psycopg2.extras

connection = psycopg2.connect("host=192.168.99.100 port=5432 user=dev password=password")
dict_cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)


# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

# ここからウェブアプリケーション用のルーティングを記述

# indexにアクセスした時の処理
@app.route('/')
def index():
    title = "ようこそ"
    message = "こんにちは"
    # index.html をレンダリングする
    return render_template('index.html',
                           message=message, title=title)

# /post にアクセスしたときの処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "こんにちは"
    if request.method == 'POST':
        # リクエストフォームから「名前」を取得して
        vote_id = request.form['vote_id']
        

        query = " select " + " id,title,candnum,cand1,cand2 " + " from m_vote " + " where id ="+ vote_id

        dict_cur.execute(query)

        for row in dict_cur:
            a=row
            print(row)

        # index.html をレンダリングする
        return render_template('index.html',
                               a=a)
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に