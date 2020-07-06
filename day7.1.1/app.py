from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


@app.route('/',methods=('GET','POST'))
def home():
        name = request.args.get('name','qiqi')
        age = request.args.get('age',12)
        gender = request.args.get('gender','nv')
        
        user=User(name,age,gender)

        menu = [
            'qq',
            'ww',
            'ee',
            'rr'
        ]
        return render_template('home.html',info=user ,menu=menu)

user_data = {
    1:{'name': '郭德纲', 'gender': 'male', 'city': '北京', 'description': '班长', 'birthday': '1997-10-01'},
    2: {'name': '陈乔恩', 'gender': 'female', 'city': '上海', 'description': 'null', 'birthday': '1995-03-02'},
    3: {'name': '赵丽颖', 'gender': 'female', 'city': '兰州', 'description': '班花不骄傲', 'birthday': '1995-04-04'},
    4: {'name': '王宝强', 'gender': 'male', 'city': '重庆', 'description': '超爱吃火锅', 'birthday': '1998-10-05'},
    5: {'name': '赵雅芝', 'gender': 'female', 'city': '重庆', 'description': '全宇宙三好学生', 'birthday': '1996-07-09'},
    6: {'name': '张学友', 'gender': 'male', 'city': '上海', 'description': '奥林匹克总冠军！', 'birthday': '1993-05-02'},
    7: {'name': '陈意涵', 'gender': 'female', 'city': '福州', 'description': 'null', 'birthday': '1994-08-30'},
    8: {'name': '赵本山', 'gender': 'male', 'city': '铁岭', 'description': '副班长', 'birthday': '1995-06-01'},
    9: {'name': '张柏芝', 'gender': 'female', 'city': '上海', 'description': 'null', 'birthday': '1997-02-28'},
    10: {'name': '吴亦凡', 'gender': 'male', 'city': '南京', 'description': '大碗宽面要不要？', 'birthday': '1995-06-01'},
    11: {'name': '鹿晗', 'gender': 'male', 'city': '北京', 'description': 'null', 'birthday': '1993-05-28'},
    12: {'name': '关晓彤', 'gender': 'female', 'city': '北京', 'description': 'null', 'birthday': '1995-07-12'},
    13: {'name': '周杰伦', 'gender': 'male', 'city': '台北', 'description': '小伙人才啊', 'birthday': '1998-03-28'},
    14: {'name': '马云', 'gender': 'male', 'city': '南京', 'description': '一个字：贼有钱', 'birthday': '1990-04-01'},
    15: {'name': '马化腾', 'gender': 'male', 'city': '上海', 'description': '马云死对头', 'birthday': '1990-11-28'},
    17: {'name': '张翔宇', 'gender': 'male', 'city': '北京', 'description': '班长', 'birthday': '1997-10-01'},
    19: {'name': '潘琪琪', 'gender': 'female', 'city': '上海', 'description': 'null', 'birthday': '1995-03-02'},
    20: {'name': '蒋艳鹏', 'gender': 'female', 'city': '北京', 'description': '班花,不骄傲', 'birthday': '1995-04-04'},
    23: {'name': '杨贵祥', 'gender': 'male', 'city': '重庆', 'description': '超爱吃火锅', 'birthday': '1998-10-05'},
    25: {'name': '曹建伟', 'gender': 'male', 'city': '重庆', 'description': '全宇宙三好学生', 'birthday': '1996-07-09'},
    26: {'name': 'hahaha', 'gender': 'male', 'city': '广州', 'description': 'null', 'birthday': '1995-01-01'}
}

@app.route('/info')
def info():
    stu_id = int(request.args.get('id', 1))
    info = user_data.get(stu_id)
    return render_template('info.html',stu=info,stu_id=stu_id)

if __name__ == "__main__":
    app.debug = True
    app.run()