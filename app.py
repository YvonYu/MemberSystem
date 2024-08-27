# 初始化資料庫連線
import pymongo
uri = "mongodb+srv://root:root123@cluster0.q14hq9k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
try:
    client = pymongo.MongoClient(uri)
    db = client.member_system

    print('successful connections')

except Exception as e:
    print(e)


# 初始化 Flask 伺服器
from flask import *
app = Flask(__name__,)
app.secret_key = 'any string but secret'

# 處理路由
@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/member')
def memberPage():
    if 'username' in session:
        Username = session.get('username')
        return render_template('member.html', username = Username)
    else:
        return redirect('/')

@app.route('/error')
def errorPage():
    error_message = request.args.get('msg', '發生錯誤，請聯繫客服')
    return render_template('error.html', message = error_message)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signupReady', methods=['POST'])
def signupReady():
    # 從前端接收資料
    user_email = request.form['email']
    user_password = request.form['password']
    # 根據接收到的資料，與資料庫互動
    collection = db.user
    result = collection.find_one({
        'email':user_email
    })
    if result != None:
        return redirect('/error?msg=此信箱已被註冊')
    else:
        # 把資料放進資料庫，完成註冊
        collection.insert_one({
            'email':user_email,
            'password':user_password
        })
        return redirect('/')
    
@app.route('/signin', methods=['POST'])
def signin():
    # 從前端取得使用者的輸入
    user_email = request.form['email']
    user_password = request.form['password']
    # 和資料庫互動
    collection = db.user
    result = collection.find_one({
        '$and':[
            {'email':user_email},
            {'password':user_password}
        ]
    })
    if result == None:
        return redirect('/error?msg=帳號或密碼輸入錯誤')
    # 登入成功，在session中紀錄會員資訊，並導向到會員頁面
    username = get_username_from_email(result['email'])
    session['username'] = username
    return redirect('/member')

@app.route('/signout')
def signout():
    # 從session中删除 'username' 鍵，若'username'不存在，則返回 None 而不會引發異常
    session.pop('username', None)
    return redirect('/')


def get_username_from_email(user_email):
    # 使用 split 方法將email拆分為兩部分
    username = user_email.split('@')[0]
    return username


# 啟動伺服器
if __name__ == '__main__':
    app.run(debug=True, port=3000)
# app.run(port=3000)