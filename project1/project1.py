import time #时间计算
from rich.progress import track #rich库实现进度条
import pinyin #另外使用pip安装pinyin包
import difflib #模糊搜索库
import logging #写日志
import numpy as np #构造一个小数的range
import sys #参数文件路径解析

#读文件部分
with open('city.txt','r',encoding='utf-8') as f:
    '''for line in f:
        txt.append((line.split(' '))'''
        
#       time_start = time.time() #计时0.0016s\
    txt=f.read()
    for i in track(np.arange(0,0.0016,0.0001), description="Downloading..."):
        str_all = txt.split('\n')
        time.sleep(0.000000001)
#    time_end = time.time()
#time_c= time_end - time_start   #运行所花时间
#print('time cost', time_c, 's')
#print(str_all)
        f.close()

'''
for i in track(range(len(str_all)), description="Printing..."):
    print(str_all[i])
    time.sleep(0.000000001) 
    #这是打印城市的进度条
'''

#这是使用pinyin库,获取输入文字的首字首字母拼音,输入文字的首字母拼音部分

def getStrAllAplha(str):
    return pinyin.get_initial(str, delimiter="").upper()
    
'''    
def getStrFirstAplha(str):
    str=getStrAllAplha(str)
    str=str[0:1]
    return str.upper()
'''


str=input()
print(getStrAllAplha(str))
#print(getStrFirstAplha(str))


#这是模糊查询 find函数速度较慢
str2=input()
res = difflib.get_close_matches(str2, str_all, 5, cutoff=0.6)
print(res)


def writeln(path):
#写日志文件部分
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler("log.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
 
    logger.info("Start print log")
    logger.debug("Do something")
    logger.info("project1")
    logger.error("ERROR message!")
    logger.warning("abc")
    logger.info("Finish your work!Good job!")

if __name__ == '__main__':
    argv=sys.argv
    city_str=argv[1]
    log_str=argv[2]
