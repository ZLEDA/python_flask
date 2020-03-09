http://127.0.0.1:5000

'/add_tiezi'
功能：发帖
返回数据
{'result':'success'}

'/get_all_tiezi'
功能：获得所有的帖子
返回数据
没有帖子时:
{"result":'fail'}
有帖子时：
{"result":'success',"list":result}
result是数组
每个数组元素格式为：{"tieziID":tieziID,"posterID":posterID,"title":title,"date":date,"content":content,"fenqu":fenqu}

'/search_tiezi'
功能：搜索帖子
返回数据:
没有帖子时:
{"result":'fail'}
有帖子时：
{"result":'success',"list":result}
result是数组
每个数组元素格式为：{"tieziID":tieziID,"posterID":posterID,"title":title,"date":date,"content":content,"fenqu":fenqu}

'/read_tiezi'
功能：查看某个具体的帖子及其回复
返回数据：
发生错误：
{"result":'fail'}
成功获得信息时：
{"result":'success',"tiezi":result_l["tiezi"],"huifu":result_l["huifu"]}
huifu 是 回复数组
每个数组元素格式为：
{"huifuID":huifuID,"posterID":posterID,"tieziID":tieziID,"date":date,"content":content,"floor":floor}

'/add_huifu'
功能：发回复
返回数据
{'result':'success'}








