import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bys
from threading import Thread
from os import path
import shutil

ua = UserAgent()
headers = {"User-Agent": ua.random}

def DownImg(imgUrl, imgPath):
    response = requests.get(imgUrl, stream=True)  # 开通便可以下载
    if response.status_code == 200:  # 代表服务器正常返回内容
        with open(imgPath, "wb") as f: # 以二进制格式写入
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)  # 必须使用response.raw 原始返回数据进行开发




class GetImg(Thread):
    def run(self):
        response = requests.get(url, headers).text
        soup = bys(response, "lxml")
        for img in soup.find_all("a", class_="thumbnail"):
            for item in img.find_all("img"):
                img_url = item.get("src")
                save_dic = path.abspath("../Pictures")  # 将相对路经解析为绝对路径
                img_name = path.basename(img_url)  # 最后斜杠的名字
                img_path = path.join(save_dic, img_name)  # 合并，这就是完整的路径名字
                print("开始下载 %s" %(img_url))
                DownImg(img_url, img_path)


for i in range(1, 6, 1):
    url = "http://www.cnu.cc/discoveryPage/hot-人像?page=" + str(i)
    print(url)
    run = GetImg()
    run.start()
    print("第 %s 页:" %i)
#    run.join()  # 判断各自线程结束

