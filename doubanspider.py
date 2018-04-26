import requests,time,random,gevent
from lxml import etree
from multiprocessing.dummy import Pool
from gevent import monkey
monkey.patch_all()

class DoubanSpider():


    def __init__(self):
        self.urls = ['https://movie.douban.com/top250?start='+str(num) for num in range(0,226,25)]
        print('访问地址为：%s'%self.urls)
        self.headers = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0) "}
        self.j = 1
        self.arr = []

    def send(self,url):
        time.sleep(random.randint(1,3))
        html = requests.get(url, headers=self.headers).content.decode('utf-8')
        print('正在发送第%s请求'%self.j)
        html_response = etree.HTML(html)
        self.response(html_response)

    def response(self, html_obj):
        node_list = html_obj.xpath("//div[@class='info']")
        for node in node_list:
            title = node.xpath(".//div[@class='hd']/a/span[1]/text()")[0]
            score = node.xpath(".//span[@class='rating_num']/text()")[0]
            try:
                info = node.xpath(".//span[@class='inq']/text()")[0]
            except:
                info = "None"
            self.arr.append(title + "\t" + score + "\t" + info)
    def write(self):
        print('正在写入数据......')
        with open('./movie_data.txt','a') as f:
            for i in self.arr:
                f.write(i+'\n')

    def main(self):
        """
        多线程版本 threading
        threads_list = []
        for self.j,url in enumerate(self.urls):
            ttt = threading.Thread(target=self.send,args=(url,))

            ttt.start()
            threads_list.append(ttt)

        for ddd in threads_list:
            ddd.join()
        """
        # 线程
        # pool = Pool(len(self.urls))
        # pool.map(self.send,self.urls)
        # pool.close()
        # pool.join()
        #
        # 协程
        job_list = []
        for url in self.urls:
            # 创建⼀个协程任务
            job = gevent.spawn(self.send, url)
            # 将协程任务放⼊任务队列⾥
            job_list.append(job)
        # 获取所有的协程任务，并放⼊任务队列
        gevent.joinall(job_list)

        self.write()
        print('第%s次写入完成!!'% self.j)

if __name__ == '__main__':
    spider = DoubanSpider()
    stat = time.time()
    spider.main()
    print('总花费时间%s'% (time.time()-stat))