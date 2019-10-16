# -*- coding: utf-8 -*-
'''
下载所有的歌词
接口： https://c.y.qq.com/soso/fcgi-bin/client_search_cp?t=7&p=1&n=10&w=%E6%B2%B3%E5%9B%BE&format=jsonp
p: page
w: 关键词
'''

from urllib.request import urlopen
import urllib.parse
import json
import os
import math
import sys

class Download:
    '''下载歌词'''
    def __init__(self, keyword):
        self.keyword = keyword
        self.page = 0
        self.titles = set([])
        self.filePath = 'lyrics/'+self.keyword+'/'
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath)
        self.getTotalPage()

    def getTotalPage(self):
        resp = self.getPage(1)
        self.totalPage = math.ceil(resp['data']['lyric']['totalnum']/resp['data']['lyric']['curnum'])    

    def getPage(self, page):
        w = urllib.parse.quote(self.keyword)
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?t=7&p='+ str(page) +'&n=10&w='+w+'&format=json'
        res = urlopen(url)
        resp = json.loads(res.read())
        return resp

    def handlePage(self, resp):
        lyrics = resp['data']['lyric']['list']
        for lrc in lyrics:
            singers = lrc['singer']
            singers = filter(lambda singer: singer['name']==self.keyword, singers)
            if len(list(singers))<1 or lrc['songname'] in self.titles:
                continue
            content = lrc['content']
            content = content.replace('\\n', '\n').replace('<em>', '').replace('</em>', '')
            self.titles.add(lrc['songname'])
            with open(self.filePath + lrc['songname']+'.txt', 'w', encoding='utf-8') as f:
                f.write(content)

    def start(self):
        for page in range(1, self.totalPage+1):
            print('正在爬取第%s页' % page)
            res = self.getPage(page)
            self.handlePage(res)
            print('第%s页爬取完毕' % page)
        print('全部爬取完毕，共爬取%s条歌词信息' % len(self.titles))



if __name__ == '__main__':
    if len(sys.argv)==2:
        singer = sys.argv[1]
        d = Download(singer)
        d.start()
  
  