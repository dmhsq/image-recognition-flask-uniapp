from aip import AipSpeech
from md5random import sjs
import os

'''语音合成'''
""" 你的 APPID AK SK """
APP_ID = 'xxxxxx'
API_KEY = 'xxxxxx'
SECRET_KEY = 'xxxxxxx'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def voice(conts,type):
    result = client.synthesis(conts, 'zh', 1, {
        'vol': 5,
        'per': type
    })
    if not isinstance(result, dict):
        return result
