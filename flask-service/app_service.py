from flask import Flask,request
import json,os
from AipImageClassify import get_imgGeneral
from md5random import sjs;
app = Flask(__name__)

@app.route("/file",methods=['POST'])
def upfile():
    params_file = request.files['file'];
    dst = os.path.join(os.path.dirname(__file__),sjs()+params_file.name);
    params_file.save(dst)
    cont = "";
    with open(dst, 'rb') as file:
        cont = file.read()
        print(cont)
    os.remove(dst);
    type=int(request.form['type'])
    print(cont)
    return json.dumps(get_imgGeneral(type,cont));
if __name__=='__main__':
        app.run(host='0.0.0.0',port=8086)
