from bs4 import BeautifulSoup
import requests as rq

def work(file_name,output_name='output_file'):

    f=open(file_name+'.html','r',encoding='utf-8')
    page = f.read()
    f.close()

    page.encode('utf-8')

    f=open(output_name+'.txt','w',encoding='utf-8')

    soup = BeautifulSoup(page,'lxml')
    soup.p.encode("utf-8")
    #print(soup.prettify())
    #print(soup.find_all('tr'))
    k=1
    #print(soup.find_all(style="text-align:left;")[0].get_text())
    name = soup.find_all(style="text-align:left;")
    for i in soup.find_all(id='magnet'):
        try:
            #print(str(k)+' '+i['href'])
            #print(name[k-1].get_text())
            f.write('['+str(k)+']\n')
            f.write(name[k-1].get_text()[2:]+'\n')
            f.write(i['href']+'\n\n')
        except TypeError:
            print('TypeError!!!')
            continue
        except AttributeError:
            print('AttributeError!!!')
            continue
        k+=1
    f.close()