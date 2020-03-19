from bs4 import BeautifulSoup
import requests as rq
from time import sleep
from selenium import webdriver

def get_page(key_word,page,t):

    # 浏览器设置
    options = webdriver.ChromeOptions()
    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"')
    driver = webdriver.Chrome(chrome_options=options)

    driver.get("https://share.acgnx.se/search.php?sort_id=0&keyword="+key_word+"&page="+str(page))

    # 缓冲t秒
    sleep(t)

    # 返回网页源代码
    return driver.page_source

def catch(key_word,time=15,output_name='output_file'):

    cnt=1 # 总链接个数
    pid=1 # 总页数

    # 清空输出文件
    f=open(output_name+'.txt','w',encoding='utf-8')
    f.write('')
    f.close()

    while True:
        page = get_page(key_word,pid,time)
        page.encode('utf-8')

        f=open(output_name+'.txt','a',encoding='utf-8')

        soup = BeautifulSoup(page,'lxml')
        k=1 # 当前页的循环变量
        name = soup.find_all(style="text-align:left;")
        # 查找链接
        for i in soup.find_all(id='magnet'):
            f.write('['+str(cnt)+']\n')
            namelen=len(name[k-1].get_text())
            f.write(name[k-1].get_text()[2:namelen-2]+'\n')
            f.write(i['href']+'\n\n')
            k+=1
            cnt+=1
        f.close()
        # 只有一页的情况
        if len(soup.find_all('a','nextprev')) == 0:
            print("Page "+str(pid)+" OK!")
            #print('Just one Page.')
            break
        # 只有两页，且当前是最后一页的情况
        if len(soup.find_all('a','nextprev')) == 1 and pid != 1:
            print("Page "+str(pid)+" OK!")
            #print('The last page.')
            break
        print("Page "+str(pid)+" OK!")
        pid+=1