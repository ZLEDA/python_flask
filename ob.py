#!/usr/bin/env python
# encoding=utf-8

import sqlite3
import time
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Text

engine = create_engine('sqlite:///db/luntan.db?check_same_thread=False')

# 创建对象的基类:
Base = declarative_base()

# 定义映射类User，其继承上一步创建的Base
class tiezi(Base):
	# 指定本类映射到tiezis表
	__tablename__ = 'tiezis'

	tieziID = Column(Integer,primary_key=True)
	posterID = Column(String)
	title = Column(String)
	date = Column(String)
	content = Column(Text)
	fenqu = Column(String)

	#获得会话
	@staticmethod
	def get_Session():
		Base.metadata.create_all(engine)
		Session = sessionmaker(bind=engine)
		session = Session()
		return session

	#结束会话
	@staticmethod
	def close_Session(session):
		if session!= None:
			# 关闭session:
			session.close()
			return True

	#增加帖子
	@staticmethod
	def addnew(session,title,posterID,content,fenqu):
		date = time.asctime(time.localtime(time.time()))
		hashdata = str(title)+str(posterID)+str(date)		#帖子的ID是帖子标题和发帖人ID和发帖日期三者拼接的字符串的哈希值
		tieziID = hash(hashdata)
		new_tiezi = tiezi(tieziID=tieziID,posterID=posterID,title=title,date=date,content=content,fenqu=fenqu)
		if session!= None:
			session.add(new_tiezi)
			#提交增加
			session.commit()

	#删除帖子
	@staticmethod
	def delete(session,tieziID):
		if session!= None:
			try:
				del_tiezi = session.query(tiezi).filter(tiezi.tieziID==tieziID).one()
			except Exception as e:
				return False
			session.delete(del_tiezi)
			del_huifu = session.query(huifu).filter(huifu.tieziID==tieziID).all()
			#删除相关帖子的回复
			for i in del_huifu:
				session.delete(i)
			#提交删除
			session.commit()
			return True

	#修改帖子
	@staticmethod
	def modify(session,tieziID,title,posterID,content,fenqu):
		if session!= None:
			modify_tiezi = session.query(tiezi).filter(tiezi.tieziID==tieziID).one()
			modify_tiezi.title = title
			modify_tiezi.content = content
			modify_tiezi.fenqu = fenqu

			#提交修改
			session.commit()

	#浏览帖子的时候,返回所有的帖子
	@staticmethod
	def get_all(session):
		if session!= None:
			result = session.query(tiezi).all()
			result_l=[]
			for i in result:
				result_l.append(i.get_json())
			return result_l

	#搜索帖子，返回符合相关标题的结果
	@staticmethod
	def search(session,title):
		if session!= None:
			result = session.query(tiezi).filter(tiezi.title.like("%"+title+"%")).all()
			result_l=[]
			for i in result:
				result_l.append(i.get_json())
			return result_l

	#查看某个具体的帖子,返回帖子信息和回复信息序列
	@staticmethod
	def get_one(session,tieziID):
		if session!= None:
			try:
				get_tiezi = session.query(tiezi).filter(tiezi.tieziID==tieziID).one()
			except Exception as e:
				return False,None
			result = huifu.get_all(session,tieziID)
			result_tiezi = get_tiezi.get_json()
			return True,{"tiezi":result_tiezi,"huifu":result}


	def get_json(self):
		return {"urlHash":str(self.tieziID),"posterID":self.posterID,"title":self.title,"date":self.date,"content":self.content,"fenqu":self.fenqu,"name":self.posterID[0:3]}

class huifu(Base):
	__tablename__ = 'huifus'

	huifuID = Column(Integer,primary_key=True)
	posterID = Column(String)
	tieziID = Column(Integer)
	date = Column(String)
	content = Column(Text)
	floor = Column(Integer)

	@staticmethod
	def get_Session():
		Base.metadata.create_all(engine)
		Session = sessionmaker(bind=engine)
		session = Session()
		return session

	@staticmethod
	def close_Session(session):
		if session!= None:
			# 关闭session:
			session.close()
			return True

	#增加回复
	@staticmethod
	def addnew(session,tieziID,posterID,content):
		date = time.asctime(time.localtime(time.time()))
		hashdata = str(posterID)+str(date)+str(content)		#回复的ID是回复人ID和回复日期 还有回复内容拼接的字符串的哈希值
		huifuID = hash(hashdata)
		if session!= None:
			#查看这个帖子的回复数，楼层为回复数+1
			huifu_number = session.query(huifu).filter(huifu.tieziID==tieziID).all()
			floor = len(huifu_number)+1
			new_huifu = huifu(huifuID=huifuID,posterID=posterID,tieziID=tieziID,date=date,content=content,floor=floor)
		
			session.add(new_huifu)
			#提交增加
			session.commit()

	#删除回复
	@staticmethod
	def delete(session,huifuID):
		if session!= None:
			del_huifui = session.query(huifu).filter(huifu.huifuID==huifuID).one()
			session.delete(del_huifu)
			#提交删除
			session.commit()

	#修改回复
	@staticmethod
	def modify(session,huifuID,content):
		if session!= None:
			modify_huifu = session.query(huifu).filter(huifu.huifuID==huifuID).one()
			modify_huifu.content = content

			#提交修改
			session.commit()

	#获得某个帖子的所以回复，并按照楼层排序
	@staticmethod
	def get_all(session,tieziID):
		if session!= None:
			result = session.query(huifu).filter(huifu.tieziID==tieziID).all()
			if len(result)!=0:
				result.sort(key=lambda x:x.floor)
			result_l=[]
			for i in result:
				result_l.append(i.get_json())
			return result_l


	def get_json(self):
		return {"posterID":self.posterID,"urlHash":str(self.tieziID),"date":self.date,"content":self.content,"floor":self.floor,"name":self.posterID[0:3]}		









