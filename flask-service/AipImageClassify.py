from aip import AipImageClassify

APP_ID = '22945433'
API_KEY = 'DNTCcEUiCMyfS2L87LlmZelk'
SECRET_KEY = '4CAHATfysu3dVEGzOSEGAWeIkTDpGWoK'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

# """ 读取图片 """
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()
#
# image = get_file_content('1.jpg')

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



# """ 调用通用物体识别 """
# def get_test():
#     c = client.advancedGeneral(image);
#     return c;
# """ 如果有可选参数 """
# options = {}
# options["baike_num"] = 5
#
# """ 带参数调用通用物体识别 """
# client.advancedGeneral(image, options)