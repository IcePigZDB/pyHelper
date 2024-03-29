import requests
import os
import random
import time
from bs4 import BeautifulSoup
# 本地导入
from download_one_paper import getHTMLText, download_one_paper


def get_paper_url_list(html):
    '''获取所有论文的下载地址
    '''
    paper_url_list = []

    soup = BeautifulSoup(html, 'html.parser')
    for content in soup.find_all('a'):
        url = content.get('href')
        if (url != None) and (url[0:16] == 'https://doi.org/'):
            paper_url_list.append(url)
    paper_url_list = list(set(paper_url_list))  # 去重
    return paper_url_list


if __name__ == "__main__":
    conf_list = [
        # {
        #     'url':'https://dblp.org/db/journals/vldb/vldb29.html',
        #     'year':'2020',
        #     'typ':'A',
        #     'conf':'VLDB'
        # },
        # {
        #     'url':'https://dblp.org/db/journals/vldb/vldb28.html',
        #     'year':'2019',
        #     'typ':'A',
        #     'conf':'VLDB'
        # },
        {
            'url': 'https://dblp.org/db/conf/sigmod/sigmod2022.html',
            'year': '2022',
            'typ': 'A',
            'conf': 'SIGMOD'
        }
    ]
    # fromFile = False
    for conf in conf_list:
    #     conf_url = conf['url']  # 获取会议的网站
    #     html = getHTMLText(conf_url)
    #     paper_url_list = get_paper_url_list(html)  # 获取所有论文的下载地址
    #     paper_url_list.sort()

    #     with open('urls.txt', 'w') as f:
    #         for url in paper_url_list:
    #             f.write(url)
    #             f.write('\n')
    #         f.close()
    #         print("%s文件保存成功" % ("urls.txt"))

        fromFile = True
        paper_url_list = []
        with open('urls.txt', 'r') as f:
            paper_url_list = f.readlines()

        # paper_url_list = paper_url_list[:]
        totnum_list = len(paper_url_list)
        for i in range(len(paper_url_list)):
            if paper_url_list[i] =="https://doi.org/10.1145/3514221":
                continue
            print('\ndealing with %d/%d=%f%%' %
                  (i + 1, totnum_list, 100.0 *
                   (i + 1) / totnum_list))  # 用来观察进度
            paper_url = paper_url_list[
                i]  # paper_url= 'https://doi.org/10.1145/3299869.3314037'
            # TODO remove when donot use file
            if (fromFile):
                paper_url = paper_url[:-1]
            # sleep
            time.sleep(random.random()*5)
            download_one_paper(paper_url, conf['year'], conf['typ'],
                               conf['conf'])
