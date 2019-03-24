import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import sys
from threading import Thread
from multiprocessing import Process
import time

# <div class="panel-body" id="htmlContent" style="font-size: 24px;"> 正文
# 正文下有一个 p; 下一页在 div#content>p.readPager>a
# div_id="list-chapterAll">dl>dd>a  # 列表


class downloader(Thread):
    def __init__(self):
        self.target = "http://www.biqukan.net/book/71080/"
        self.titles = []
        self.urls = []
        self.headers = {"User-Agent": UserAgent().random}
        self.str_content = ""
        self.amount = 0

    def get_download_urls(self):
        res = requests.get(url=self.target, headers=self.headers)
        res.encoding = "gb2312"
        soup = bs(res.text, features="html.parser")
        box = soup.find_all("div", id="list-chapterAll")
        link = box[0].find_all("a")
        self.amount = len(link)
        for item in link:
            self.titles.append(item.string)
            self.urls.append(self.target + item.get("href"))

    def get_content(self, target):
        res = requests.get(url=target, headers=self.headers)
        res.encoding = "gb2312"
        soup = bs(res.text, features="html.parser")
        content = soup.find_all("div", id="htmlContent")
        new_content = content[0].text.replace('\xa0' * 8, '\n\n')
        self.str_content += new_content
        if content[0].find_all("p"):
            nextpage = soup.find_all("p", class_="readPager")
            nextLink = nextpage[0].find_all("a", id="linkNext")
            nextLink = nextLink[0].get("href")
            self.amount += 1
            self.get_content(nextLink)
        else:
            return

        content = self.str_content
        self.str_content = ""
        return content

    def writer(self, title, path, content):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(title + '\n')
            f.writelines(content)
            f.write('\n\n')


class myThread(Thread):
    def __init__(self, title, path, content):
        Thread.__init__(self)
        self.title = title
        self.path = path
        self.content = content

    def run(self):
        self.writer(self.title, self.path, self.content)


if __name__ == "__main__":
    dl = downloader()
    dl.get_download_urls()
    start = time.time()
    print('<<神祇>> 开始下载： ')
    for item in range(dl.amount):
        # mythread = myThread(dl.titles[item], '神祇.txt', dl.get_content(dl.urls[item]))
        # mythread.start()  # 多线程
        # dl.writer(dl.titles[item], '神祇.txt', dl.get_content(dl.urls[item]))  # 单线程
        Process(target=dl.writer, args=(dl.titles[item], '神祇.txt', dl.get_content(dl.urls[item]),)).start()  # 多进程
        sys.stdout.write(" 已下载：%.3f%%" % float(item / dl.amount * 100) + '\r')
        sys.stdout.flush()

    end = time.time()
    print("<<神祇>> 下载完成")
    print("用时： %.1f s" %(end -start))
