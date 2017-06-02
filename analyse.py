# -*- conding: utf-8 -*-

import os
import jieba
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread
import sys

class Analyse:
  def __init__(self, keyword):
    path = os.path.join('lyrics', keyword)
    if not os.path.exists(path):
      print('未找到可分析的文件目录，请先抓取')
      sys.exit()
      return
    self.files = [f for f in os.listdir(path) if os.path.splitext(f)[1] == '.txt']
    self.files = map(lambda file: os.path.join(path, file), self.files)
    self.picfile = os.path.join(path, 'bg.jpg')
    if not os.path.exists(self.picfile):
      self.picfile = './bg.jpg'
    self.data = {}
    
  def readfiles(self):
    files = list(self.files)
    for file in files:
      with open(file, 'r', encoding='utf-8') as f:
        # 过滤前三行，标题，词，曲
        for i in range(3):
          f.readline()
        while True:
          line = f.readline()
          if not line:
            break
          self.handleLine(line)
    print('分析了%s个歌词文件' % len(files))

  def handleLine(self, line):
    # 去掉空格和换行
    line = line.replace(' ', '')
    line = line.replace('\n', '')
    line = line.replace('em', '')
    # 切词
    words = jieba.cut(line)
    for word in words:
      if len(word)<=1:
        continue
      if word in self.data:
        self.data[word] = self.data[word]+1
      else:
        self.data[word] = 1
  
  def showData(self):
    print('请稍等,正在绘图···')
    mask = imread(self.picfile)
    imgcolor = ImageColorGenerator(mask)
    wcc = WordCloud(font_path='./msyhl.ttc', 
    mask=mask, background_color='white', 
    max_font_size=200, 
    max_words=300,
    color_func=imgcolor
    )
    wc = wcc.generate_from_frequencies(self.data)
    plt.figure()
    plt.imshow(wc)
    plt.axis('off')
    print('绘图完成！')
    plt.show()

if __name__ == '__main__':
    if len(sys.argv)==2:
      singer = sys.argv[1]
      a = Analyse(singer)
      a.readfiles()
      a.showData()
    else:
      print('请指定歌手姓名')
