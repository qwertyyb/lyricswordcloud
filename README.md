# 歌手歌词词云
![test](https://github.com/qwertyyb/lyricswordcloud/workflows/test/badge.svg)

## 运行效果
![运行截图](https://puui.qpic.cn/vupload/0/1571202906332_p94wkus4c7j.png/0)

## 用法
```
# 下载歌词
$ python download.py 许嵩

# 分析歌词并绘制词云
$ python analyse.py 许嵩

# 或者，下载歌词并绘制词云
$ python download.py 许嵩 && python analyse.py 许嵩
```

## 依赖
基于python3
```
pip install -r requirements.txt
```

## 获取歌词接口：
https://c.y.qq.com/soso/fcgi-bin/client_search_cp?t=7&p=1&n=10&w=%E6%B2%B3%E5%9B%BE&format=json

#### 接口分析：
- p: 当前页面
- n: 每面显示的数量
- w: 歌手姓名
- format: 返回格式
#### 注意
经试验，该接口仅能返回至多20页数据，其中大约有110条来自搜索的歌手

## 关于词云的形状
如果在对应歌手的目录有图片 `bg.jpg` ,则以此图片为依据绘制词云，如果在歌手目录未来发现，则用根目录下的 `bg.jpg` 为依据绘制词云。
