import requests
import gevent
from gevent import monkey

monkey.patch_all()

def download(url):
    respone = requests.get(url)
    content = respone.text
    print(f'下载了{url}的数据，长度：{len(content)}')


if __name__ == '__main__':
    urls = ['http://www.baidu.com','http://www.163.com']
    g1 = gevent.spawn(download,urls[0])
    g2 = gevent.spawn(download, urls[1])


    #gevent.joinall(g1,g2)
    g1.join()
    g2.join()