def if_is_None(data, default=""):
    if data == None:
        data = default
    return data

def webType_to_strType(typeNum):
    dic = {"0": "帖子", "9": "政府公告", "10": "新闻", "11": "博文", "12": "帖子", "13": "网络聊天"}
    return dic[typeNum]