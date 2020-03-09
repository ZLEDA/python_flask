#!/usr/bin/env python
# encoding=utf-8

from flask import Flask,jsonify,redirect
from flask import request
from flask_cors import CORS
import requests
import json

from ob import tiezi,huifu

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

appid = 'wx2194c221a5ffe26a'
secret = 'e11a3c683770e3db59c4c74c47049ef0'

@app.route('/get_oppenid',methods=['GET','POST'])
def get_openid():
	data = request.args
	jscode = data.get("code")
	url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (appid,secret,jscode)

	r = requests.get(url)
	print(r.text)
	openid = r.json()['openid']


	return jsonify({"openid":openid})

@app.route('/add_tiezi',methods=['GET'])
def add_tiezi():
	data = request.args
	posterID = data.get('openid')
	title = data.get('theme')
	content = data.get('content')
	fenqu = data.get('kind')

	session = tiezi.get_Session()
	tiezi.addnew(session,title,posterID,content,fenqu)
	tiezi.close_Session(session)
	return jsonify({'result':'success'})

@app.route('/get_all_tiezi',methods=['GET'])
def get_all_tiezi():
	session = tiezi.get_Session()
	result = tiezi.get_all(session)
	tiezi.close_Session(session)
	if len(result)==0:
		return jsonify({"result":'fail'})
	else:
		return jsonify({"result":'success',"list":result})

@app.route('/search_tiezi',methods=['GET'])
def search_tiezi():
	data = request.args
	title = data.get('theme')
	session = tiezi.get_Session()
	result = tiezi.search(session,title)
	tiezi.close_Session(session)

	if len(result)==0:
		return jsonify({"result":'fail'})
	else:
		return jsonify({"result":'success',"list":result})
	
@app.route('/read_tiezi',methods=['GET'])
def read_tiezi():
	data = request.args
	tieziID = int(data.get('urlHash'))
	print(tieziID)
	session = tiezi.get_Session()
	result,result_l = tiezi.get_one(session,tieziID)
	tiezi.close_Session(session)
	if result == False:
		return jsonify({"result":'fail'})
	else:
		return jsonify({"result":'success',"tiezi":result_l["tiezi"],"huifu":result_l["huifu"]})

@app.route('/add_huifu',methods=['GET'])
def add_huifu():
	data = request.args
	posterID = data.get('openid')
	content = data.get('content')
	tieziID = data.get('urlHash')

	session = huifu.get_Session()
	huifu.addnew(session,tieziID,posterID,content)
	huifu.close_Session(session)
	return jsonify({'result':'success'})













if __name__ == '__main__':
	app.run()
