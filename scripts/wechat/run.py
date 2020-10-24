#!/bin/python3
from flask import Flask,request
import hashlib
import xmltodict
import time
from gdutnew_help import download
from tool import Tools
from get_pic import get_pic
app = Flask(__name__)
tool = Tools()
@app.route('/wx', methods=["GET", "POST"])
def getinput():
    if (request.method == "GET"):       
        signature=request.args.get('signature')
        timestamp=request.args.get('timestamp')
        nonce=request.args.get('nonce')
        token = "slleo2020"
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        sha1.update(list[0].encode('utf-8'))
        sha1.update(list[1].encode('utf-8'))
        sha1.update(list[2].encode('utf-8'))
        hashcode = sha1.hexdigest()
        echostr = request.args.get("echostr")
        if hashcode == signature:
            return echostr
        else:
            return ""
    elif request.method == "POST":
       
        xml_str = request.data
        if not xml_str:
            return""
       
        xml_dict = xmltodict.parse(xml_str)
        xml_dict = xml_dict.get("xml")


        msg_type = xml_dict.get("MsgType")      
        content_fromuser =  xml_dict.get("Content")
        content_touser = ''
        if msg_type=='text':
            if '通知' in  content_fromuser:
                data = download()
                for each in data:
                    content_touser = content_touser+each+'\n'
                resp_dict = {
                "xml": {
                    "ToUserName": xml_dict.get("FromUserName"),
                    "FromUserName": xml_dict.get("ToUserName"),
                    "CreateTime": int(time.time()),
                    "MsgType": "text",
                    "Content": "通知:\n" +content_touser
                }
            }
            elif 'pz' in content_fromuser:
                get_pic()
                #content_touser = open(r'/home/pi/scripts/roboot/result.jpg', 'rb')
                url_mediaid='https://api.weixin.qq.com/cgi-bin/media/upload?'
                media_id = tool.get_media_id('/home/pi/scripts/wechat/result.jpg')
                resp_dict = {
                "xml": {
                    "ToUserName": xml_dict.get("FromUserName"),
                    "FromUserName": xml_dict.get("ToUserName"),
                    "CreateTime": int(time.time()),
                    "MsgType": "image",
                    'Image':{
                            "MediaId": media_id}
                    
                }
            }           
            resp_xml_str = xmltodict.unparse(resp_dict)

            #print(resp_xml_str)
            return resp_xml_str
        else:
            resp_dict = {
                "xml": {
                    "ToUserName": xml_dict.get("FromUserName"),
                    "FromUserName": xml_dict.get("ToUserName"),
                    "CreateTime": int(time.time()),
                    "MsgType": "text",
                    "Content": "Dear I Love you so much"
                }
            }
            resp_xml_str = xmltodict.unparse(resp_dict)

            return resp_xml_str
if __name__ == '__main__':
    app.run('127.0.0.1',port='5000')
