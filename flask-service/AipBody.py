from aip import AipBodyAnalysis

'''人体检测'''
""" 你的 APPID AK SK """
APP_ID = 'xxxxxx'
API_KEY = 'xxxxxxxx'
SECRET_KEY = 'xxxxxxxx'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def delBody(type,image):
    if(type == 1):
        return __analysis(image)
    if(type == 2):
        return __attr(image)
    if(type == 3):
        return __num(image)
    if(type == 4):
        return __gesture(image)
    if(type == 5):
        return __seg(image)





""" 调用人体关键点识别 """
def __analysis(image):
    return client.bodyAnalysis(image)


""" 调用人体检测与属性识别 """
def __attr(image):
    return client.bodyAttr(image)

""" 调用人流量统计 """
def __num(image):
    return client.bodyNum(image)

""" 调用手势识别 """
def __gesture(image):
    return client.gesture(image)

""" 调用人像分割 """
def __seg(image):
    return client.bodySeg(image)