# -*-coding:utf-8-*-
import os

import requests
from multiprocessing import Process,Pool
from tianyan.config.header import RequestHeader
from lxml import etree


class IpProxyCrawl(object):
    '''西刺代理爬取'''

    def __init__(self):
        self.url = 'http://www.xicidaili.com/nn/'
        self.header = RequestHeader().headerInfo

    def get_html(self):
        res = requests.get(self.url, headers=self.header)
        print(type(res.text))
        return res.text

    def get_parse(self):
        ip_list = []
        html = etree.HTML(self.get_html())
        for i in range(len(html.xpath("//tr/td[2]/text()"))):
            ele_content = {
                "ip_addr": html.xpath("//tr/td[2]/text()")[i],
                "port": html.xpath("//tr/td[3]/text()")[i],
                "verb": html.xpath("//tr/td[6]/text()")[i],
                "survive_time": html.xpath("//tr/td[9]/text()")[i],
                "auth_time": html.xpath("//tr/td[10]/text()")[i],
                "is_vaild": True
            }
            ip_list.append(ele_content)
        # print(ip_list)
        # print('进程:',name)
        return ip_list

    def auth_is_vaild(self,name):
        print('进程:',name)
        url='http://www.baidu.com'
        for i in self.get_parse():
            if str(i["verb"]).lower() in ("https","http"):
                proxies={
                    "http":"http://"+i["ip_addr"]+":"+i["port"]
                }
                try:
                    res=requests.get(url,headers=self.header,timeout=10,proxies=proxies)
                    if res.status_code==200:
                        print("----code----",res.status_code)
                        with open('ip_vaild.txt','a') as f:
                            print(proxies["http"])
                            f.write(proxies["http"])
                    else:
                        pass
                except Exception as e:
                    print(e)

    def wirte_ip(self):
        with open('ip_vaild.txt',"a") as f:
            f.write('aaaaaaa')

if __name__ == '__main__':
    crawl = IpProxyCrawl()
    # crawl.get_parse()
    p=Pool(processes=4)
    # 创建进程
    for i in range(5):
        # print('子进程ID',os.getegid())
        # 创建进程任务
        p.apply_async(crawl.auth_is_vaild,args=(i,))
        # 开启进程
        # p.start()
        # 父进程阻塞
    p.close()
    p.join()
    print('----父进程结束-----')
    # crawl.auth_is_vaild()
    # crawl.wirte_ip()

