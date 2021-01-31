from flask import Flask,request,send_file,make_response
import json,os,jsonify,threading,base64,requests
from AipImageClassify import get_imgGeneral
from md5random import sjs;
from AipBody import delBody
from  AipSpeech import voice
app = Flask(__name__)

token = ""
'''字节小程序需要内容以及图片检测是否违规，此处获取检测所需x-token'''
def __getToken():
    url = 'https://developer.toutiao.com/api/apps/token?appid=xxxxxx&secret=xxxxxxxxx&grant_type=client_credential'
    res = requests.get(url)
    dd = res.json()
    datas = json.loads(json.dumps(dd))
    global token
    token = datas['access_token']
    t = threading.Timer(7100,__getToken)
    t.start()

__getToken()

'''获取内容检测token'''
@app.route("/getToken",methods=["GET"])
def getT():
    return token

'''图像识别'''
@app.route("/file",methods=['POST'])
def upfile():
    '''接收文件'''
    params_file = request.files['file'];
    '''随机文件名'''
    dst = os.path.join(os.path.dirname(__file__),sjs()+params_file.name);
    '''保存文件'''
    params_file.save(dst)
    '''文件流变量'''
    cont = "";
    '''读取文件'''
    with open(dst, 'rb') as file:
        cont = file.read()
    '''删除文件'''
    os.remove(dst);
    '''获取表单数据type'''
    type=int(request.form['type'])
    '''返回识别结果'''
    return json.dumps(get_imgGeneral(type,cont));

'''语音合成'''
@app.route("/voi",methods=['GET'])
def voi():
    '''获取前端传参result的值'''
    conts = request.args['result']
    '''获取前端传参type的值'''
    type = request.args['type']
    '''获取合成结果'''
    result = voice(conts,int(type))
    '''随机文件名'''
    sj = sjs()
    '''生成mp3文件'''
    with open("{}.mp3".format(sj), 'wb') as f:
        f.write(result)
        f.close()
    '''将向前端返回语音合成文件加入返回参数'''
    response = make_response(
        send_file("{}.mp3".format(sj)))
    '''定时任务函数，发送完数据后删除mp3文件'''
    def sc():
        os.remove("{}.mp3".format(sj))

    '''定时任务，任务开启3秒后调用定时任务函数删除mp3文件'''
    timer = threading.Timer(3, sc)
    '''开启任务'''
    timer.start()
    '''返回数据'''
    return response

'''人体检测'''
@app.route("/body",methods=['POST'])
def delBodys():
    '''接收文件'''
    params_file = request.files['file'];
    '''随机文件名'''
    dst = os.path.join(os.path.dirname(__file__),sjs()+params_file.name);
    '''保存文件'''
    params_file.save(dst)
    '''文件流变量'''
    cont = "";
    '''读取文件'''
    with open(dst, 'rb') as file:
        cont = file.read()
    '''删除文件'''
    os.remove(dst);
    '''获取前端传参type的值'''
    type=int(request.form['type'])
    '''判断是否为图像分割，图像分割需要返回图片'''
    if(type==5):
        '''获取图像分割结果'''
        ss = json.loads(json.dumps(delBody(type, cont)))
        '''得到人物抠图'''
        ssr = ss['foreground']
        '''处理得到的数据'''
        imgdata = base64.b64decode(ssr)
        '''随机文件名'''
        send_s = sjs()
        '''保存文件'''
        with open('{}.png'.format(send_s), 'wb') as filess:
            filess.write(imgdata)
            filess.close()
        '''定时任务函数，发送完数据后删除mp3文件'''
        def sc():
            os.remove("{}.png".format(send_s))

        '''定时任务，任务开启20秒后调用定时任务函数删除mp3文件'''
        timer = threading.Timer(20, sc)
        '''任务开启'''
        timer.start()
        '''返回分割得到的图片的文件名'''
        return send_s
    '''返回分析数据'''
    return json.dumps(delBody(type,cont));

'''获取图片'''
@app.route("/getImg",methods=['GET'])
def getImg():
    '''接收name参数'''
    ss = request.args['name']
    '''返回对应图片'''
    response = make_response(
        send_file("{}.png".format(ss)))
    '''定时任务函数，发送完数据后删除mp3文件'''
    def sc():
        os.remove("{}.png".format(ss))

    '''定时任务，任务开启2秒后调用定时任务函数删除mp3文件'''
    timer = threading.Timer(2, sc)
    '''任务开启'''
    timer.start()
    '''返回数据'''
    return response

'''图片转base64 不再详细说明'''
@app.route("/toBe64",methods=['POST'])
def getB64():
    params_file = request.files['file'];
    dst = os.path.join(os.path.dirname(__file__), sjs() + params_file.name);
    params_file.save(dst)
    cont = "";
    with open(dst, 'rb') as file:
        cont = file.read()
    bas64D = base64.b64encode(cont)
    os.remove(dst);
    return bas64D

if __name__=='__main__':
        app.run(host='0.0.0.0',port=8086)
