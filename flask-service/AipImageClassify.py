from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

def get_imgGeneral(type,image):
    if(type==0):
        return __animal(image)
    elif(type==1):
        return __dish(image)
    elif(type==2):
        return __car(image)
    elif(type==3):
        return __plant(image)
    elif(type==4):
        return __ingred(image)
    else:
        return "类型或图片格式错误"

""" 调用动物识别 """
def __animal(image):
    return client.animalDetect(image);

""" 调用菜品识别 """
def __dish(image):
    return client.dishDetect(image);

""" 调用车辆识别 """
def __car(image):
    return client.carDetect(image);

""" 调用植物识别 """
def __plant(image):
    return client.plantDetect(image);

""" 调用食材识别 """
def __ingred(image):
    return client.ingredient(image);
