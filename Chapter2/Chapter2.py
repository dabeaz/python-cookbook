#!/usr/bin/python3
#encoding=utf8

def ch2_1():
    '''
    2.1 使用多个界定符分割字符串
    一个字符串中的分隔符不固定需要使用re.split开灵活切割字符串
    '''

    print("\nch2_1:")

    import  re
    line = '我 是中国;人,你是-哪国人'
    result = re.split(r'[ ;,-]\s*', line)
    print(result)


def ch2_2():
    '''
    2.2  在字符串的开头或者结尾处做文本匹配
    startswith和endswith
    '''

    print("\nch2_2:")

    import  os
    filenames = os.listdir(".")
    md_file = [file for file in filenames if file.endswith((".md",".MD"))]
    print(md_file)

    https = ["https:","HTTPS:"]
    urls =["http://baidu.com","www.qq.com:80","https://github.com","ftp://mirror.aliyun.com"]
    https_url = [url for url in urls if url.startswith(tuple(https))]
    print(https_url)

    #使用正则
    import  re
    result=re.match(r"^(https:)","https://github.com")
    if result:
        print(result.groups())
    else:
        print("no result")


def ch2_3():
    '''
    2.3利用Shell通配符做字符串匹配
    使用fnmatch模块中的fnmatch和fnmatchcase
    '''

    print("\nch2_3:")

    from fnmatch import fnmatch,fnmatchcase

    #fnmatch按照平台是否区分大小写，window不区分
    files = ["config.ini","data1.csv","data2.csv","ata_train.csv","README.md","CONTINUE.MD"]
    print(files)

    data_file = [file for file in files if fnmatch(file,"data*.csv")]
    print(data_file)

    #fnmatchcase 可以区分大小写
    print(files)
    data_file = [file for file in files if fnmatchcase(file, "*.MD")]
    print(data_file)




def main():

    for i in range(1,4):
        func='ch2_%d()'%(i)
        exec(func)


if __name__ == "__main__":
    main()