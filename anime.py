from bs4 import BeautifulSoup
import requests as rq
from time import sleep
from selenium import webdriver

def get_page(key_word,page,t):

    # 进入浏览器设置
    options = webdriver.ChromeOptions()
    # 设置中文
    #options.add_argument('lang=zh_CN.UTF-8')
    # 更换头部
    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(chrome_options=options)

    #driver = webdriver.Chrome()
    driver.get("https://share.acgnx.se/search.php?sort_id=0&keyword="+key_word+"&page="+str(page))


    #print(driver.page_source)
    sleep(t)

    return driver.page_source

def catch(key_word,time=15,output_name='output_file'):

    #f=open(file_name+'.html','r',encoding='utf-8')
    #page = f.read()
    #f.close()
    #print(page)

    cnt=1
    pid=1

    f=open(output_name+'.txt','w',encoding='utf-8')
    f.write('')
    f.close()

    while True:

        page = get_page(key_word,pid,time)

        page.encode('utf-8')

        f=open(output_name+'.txt','a',encoding='utf-8')

        soup = BeautifulSoup(page,'lxml')
        #soup.p.encode("utf-8")
        #print(soup.prettify())
        #print(soup.find_all('tr'))
        k=1
        #print(soup.find_all(style="text-align:left;")[0].get_text())
        name = soup.find_all(style="text-align:left;")
        for i in soup.find_all(id='magnet'):
            try:
                #print(str(k)+' '+i['href'])
                #print(name[k-1].get_text())
                f.write('['+str(cnt)+']\n')
                namelen=len(name[k-1].get_text())
                f.write(name[k-1].get_text()[2:namelen-2]+'\n')
                f.write(i['href']+'\n\n')
            except TypeError:
                print('TypeError!!!')
                continue
            #except AttributeError:
                #print('AttributeError!!!')
                #continue
            k+=1
            cnt+=1
        f.close()
        #print(len(soup.find_all('a','nextprev')))
        if len(soup.find_all('a','nextprev')) == 0:
            print("Page "+str(pid)+" OK!")
            #print('Just one Page.')
            break
        if len(soup.find_all('a','nextprev')) == 1 and pid != 1:
            print("Page "+str(pid)+" OK!")
            #print('The last page.')
            break
        print("Page "+str(pid)+" OK!")
        pid+=1