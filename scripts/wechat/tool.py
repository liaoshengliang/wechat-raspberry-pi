import requests as re
import json


class Tools:
    def __init__(self):
        self.url_for_token='https://api.weixin.qq.com/cgi-bin/token?'#url for getting access_token
        self.url_for_media_id='https://api.weixin.qq.com/cgi-bin/media/upload?'#url for getting mmedia_id

        

    def get_access_token(self):#get acess_token
        params ={
        'grant_type':'client_credential',
        'appid':'wx5ae1f28b0cf15253',
        'secret':'a88c1032236fc5dda69c63109504e3b6'}
        get = re.get(self.url_for_token,params=params)
        result = get.json()
        access_token = result['access_token']
        return access_token

    
    def get_media_id(self,file_path):#get media_id
     
        image = {'file':open(file_path,'rb')}
        params={
          'access_token':self.get_access_token(),
          'type':'image'}
        media = re.post(self.url_for_media_id,params,files =image).json()
        return media['media_id']
if __name__=='__main__':
    tool=Tools()
    print(tool.get_access_token(),'\n')
    print(tool.get_media_id('d:/dst.jpg'))
