# Anime-Spyder

**动漫网站爬虫**

动漫下载网站：[末日動漫資源庫 - Project AcgnX Torrent Asia](https://share.acgnx.se/)

~~搜索要看的番后下载网页HTML文件，操作`main.py`，即可。~~
详见v3.0更新。

~~暂不支持多页。~~
v2.0已支持多页。

## v3.0更新

可以通过命令行操作：

```shell
$ python main.py key_word [-t time] [-o output_file]
```

其中用方括号包围的为可选参数。

## `catch()`函数说明

1. 第一个参数：搜索关键词。
2. 第二个参数：缓冲时间，根据网速设定，默认20秒。
3. 第三个参数：输出文件，默认为output_file.txt。

~~别问网站上的广告怎么回事，眼不见为净。~~