import datetime

def if_is_None(data, default=""):
    if data == None:
        data = default
    return data

def webType_to_strType(typeNum):
    dic = {"0": "未知", "9": "政府公告", "10": "新闻", "11": "博文", "12": "帖子", "13": "网络聊天"}
    return dic[typeNum]

def changeWebsite(id):
    list = [{'websitename': '网易博客', 'websitetypeid': '11'},
            {'websitename': '教育部', 'websitetypeid': '9'},
            {'websitename': '未知', 'websitetypeid': '0'},
            {'websitename': '中华网社区', 'websitetypeid': '12'},
            {'websitename': '猫扑社区', 'websitetypeid': '12'},
            {'websitename': '新华网', 'websitetypeid': '10'},
            {'websitename': '凯迪社区', 'websitetypeid': '12'},
            {'websitename': '人民网', 'websitetypeid': '10'},
            {'websitename': '西祠社区', 'websitetypeid': '12'},
            {'websitename': '天涯BBS', 'websitetypeid': '12'},
            {'websitename': '人民网BBS', 'websitetypeid': '12'},
            {'websitename': '新华网BBS', 'websitetypeid': '12'},
            {'websitename': '三秦网', 'websitetypeid': '10'},
            {'websitename': '豆瓣小组', 'websitetypeid': '13'},
            {'websitename': '搜狐BBS', 'websitetypeid': '12'},
            {'websitename': '中国社会新闻网', 'websitetypeid': '10'},
            {'websitename': '新浪新闻', 'websitetypeid': '10'},
            {'websitename': '网易新闻', 'websitetypeid': '10'},
            {'websitename': '博客中国', 'websitetypeid': '11'},
            {'websitename': '新浪博客', 'websitetypeid': '11'},
            {'websitename': '人民新闻', 'websitetypeid': '10'},
            {'websitename': '网易博客', 'websitetypeid': '11'},
            ]
    return list[id]['websitename'], webType_to_strType(list[id]['websitetypeid'])

def countAge(birth):
    birthday = datetime.datetime.strptime(birth, "%Y-%m-%d")
    now = datetime.datetime.now()
    if (now - birthday).days < 0:
        return "数据出错"
    else:
        if now.month > birthday.month:
            return now.year - birthday.year
        elif now.month < birthday.month:
            return now.year - birthday.year - 1
        elif now.month == birthday.month:
            if now.day >= birthday.day:
                return now.year - birthday.year
            else:
                return now.year - birthday.year - 1
