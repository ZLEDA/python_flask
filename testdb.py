#!/usr/bin/env python
# encoding=utf-8

from ob import tiezi,huifu
import time

session = tiezi.get_Session()


#l = [-6084764008844179393,4858743306983920654,9021363558139671850]


#tiezi.addnew(session,title="关注中美贸易战",posterID="123141341",content="中美贸易战继续谈判，仍未出现好转局势",fenqu="日常生活")
#tiezi.addnew(session,title="小伙穿越无人区背后隐情",posterID="123661841",content="有报道说，那个小伙子被队友抛下了才不得不自己荒野求生",fenqu="日常生活")
#tiezi.addnew(session,title="5月8日，铭记历史上的今天",posterID="123761841",content="5月8日，南斯拉夫大使馆被炸，这是新中国不能忘记的一天",fenqu="日常生活")
#r=tiezi.get_one(session,'王子豪')
#tiezi.delete(session,4566439719426382920)
#for j in range(0,2):
#for i in l:
#huifu.addnew(session,7153867448066541951,"46533","我听说好像是他女朋友把他抛弃了，这哥们也太惨了")
#r = tiezi.delete(session,21312321)
#r=tiezi.get_one(session,9021363558139671850)
#for i in r:
#	print(i.get_json())

#print(r)

tiezi.close_Session(session)

