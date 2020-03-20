from anime import *
import sys,getopt

if __name__=='__main__':
    key_word = sys.argv[1]
    ot,args = getopt.getopt(sys.argv[2:],'ht:o:')
    time = -1
    out = 'ERROR'
    for op,arg in ot:
        if op == '-t':
            time = int(arg)
        elif op == '-o':
            out = arg
    print(key_word,time,out)
    if time == -1 and out == 'ERROR':
        catch(key_word)
    elif time != -1 and out == 'ERROR':
        catch(key_word,time=time)
    elif time ==-1 and out != 'ERROR':
        catch(key_word,output_name=out)
    else:
        catch(key_word,time=time,output_name=out)
    #第一个参数：搜索关键词
    #第二个参数：缓冲时间，根据网速设定，默认15秒
    #第三个参数：输出文件，默认为output_file.txt