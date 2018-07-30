#!/usr/bin/env python3
#!encoding=utf-8


def ch1_1():
    '''
    1.1 将序列分解为单独的变量
    对象可迭代，就可以分解，包括字符串，文件，迭代器，生成器
    分解操作可以使用"_"来丢弃一些特定的值
    '''
    print("\nch1_1:")
    data=['hello','ch1',["*","_"], (-6,1,4)]

    _,a,[_,b], (_,middle,_) = data

    print(a+b+str(middle)) #ch1_1



def ch1_2():
    '''
    1.2 从任意长度的可迭代对象中分解元素
    "*表达式" 用于未知长度或者任意长度的对象分解
    分解linux shadow文件字符串
    '''
    print("\nch1_2:")

    linux_shadow = "username:$1$jMzjGK//$Do9jjAM9TqHVhkH3eSytT.:14576:0:99999:7:::"
    username,passwd,*drop = linux_shadow.split(":")
    _, encrpty_type, encrpty_salt,encrptyed_str = passwd.split("$")

    print("type:%s\nsalt:%s\npasswd:%s\n" % (encrpty_type,encrpty_salt,encrptyed_str))



def ch1_3():
    '''
    1.3 保存最后N个元素
    使用colletions.deque
    添加，弹出均为O(1)
    '''
    print("\nch1_3:")

    from collections import deque

    def search(lines, pattern, history=5):
        pre_lines = deque(maxlen=history) #保存最后5个搜索结果
        for line in lines:
            if pattern in line:
                yield line, pre_lines
            pre_lines.append(line)


    with open('ch1_3.txt') as f:
        for line, prelines in search(f, 'Java', 5):
            print(prelines, len(prelines))
            print(line)


def ch1_4():
    '''
    1.4 找到最大或者最小的N个元素
    使用heapq中的nlargest和nsmallest
    找出学生成绩的前五名
    '''
    print("\nch1_4:")

    from heapq import  nlargest,heapify,heappop
    from operator import  itemgetter

    #元素数量相对较小时使用nlargest nsmallest
    dict1 = {'name1': 34, 'name2':45, 'name3': 98, 'name4':34, 'name5': 66, "name6":90, "name7":90}
    top5 = nlargest(5, dict1.items(),key=lambda x:x[1])   #注意python3 iteritem没有了 用items替代了
    print(top5)


    #如果元素总数很大，N很小
    heap = list(dict1.values()) #转化为list 变成堆 pop
    heapify(heap)
    for i in range(5): #输出最小的5个值
        print(heappop(heap))

    #如果元素数量和N差不多大，建议排序再做切片
    for name,score in sorted(dict1.items(), key=itemgetter(1),reverse=True)[:5]:
        print(name,score)


def ch1_5():
    '''
    1.5 实现优先级队列
    使用heapq来pop优先级最高的元素
    '''
    print("\nch1_5:")

    import  heapq

    class PrioriyQueue:
        def __init__(self):
            self._queue=[]
            self._index = 0
        def push(self, item, priority):
            heapq.heappush(self._queue, [-priority,self._index,item]) #从高到低排列
        def pop(self):
            return heapq.heappop(self._queue)[-1]

    q= PrioriyQueue()
    q.push('1',1)
    q.push('10',10)
    q.push('100',100)
    q.push('50',50)
    q.push('double 50',50)
    q.push('25',25)

    for i in range(5):
        print(q.pop())



def ch1_6():
    '''
    1.6 在字典中将键映射到多个值上 （一键多值字典）
    使用collections中的defaultdir
    '''

    print("\nch1_6:")

    from collections import defaultdict
    d = defaultdict(list)
    #一个键对应一个list
    d['a'].append(1)
    d['a'].append(2)
    d['a'].append(3)

    d['b'].append(4)

    print(d)


def ch1_7():
    '''
    1.7 让字典保持有序
    使用collections中的OrderedDict类
    '''

    print("\nch1_7:")

    from collections import  OrderedDict
    #OrderedDict 中维护了一个双向链接，来保持顺序加入的位置，大量数据会增大内存消耗
    d= OrderedDict()
    d['1'] = 1
    d['2'] = 2
    d['3'] = 3
    d['4'] = 4

    for key in d:
        print(key,d[key])


def ch1_8():
    '''
    1.8 与字典有关的计算问题 如最小值，最大值，排序等
    使用zip把字典的键值反过来
    '''
    print("\nch1_8:")

    scores = {'name1': 34, 'name2':45, 'name3': 98, 'name4':34, 'name5': 66, "name6":90, "name7":90}

    min_score = min(zip(scores.values(),scores.keys()))
    max_score = max(zip(scores.values(),scores.keys()))
    scores_sorted = sorted(zip(scores.values(), scores.keys()),reverse=True)

    print(min_score,max_score)
    print(scores_sorted)


def ch1_9():
    '''
    1.9 在两个字典中寻找相同点
    寻找相同的键，相同的值等
    使用集合操作 如 & -
    '''

    print("\nch1_9:")

    a={'x':1,'y':2,'z':3}
    b={'w':100,'x':50,'y':2}

    print(a.keys() & b.keys())
    print(a.keys() - b.keys())
    print(a.items()& b.items())



def ch1_10():
    '''
    1.10 从序列中移除重复项且保持元素间顺序不变
    利用set和生成器，返回不同的元素
    '''
    print("\nch1_10:")

    def dedupe(items, key= None):
        b = set()
        for i in items:
            val = i if key is None else key(i)
            if val not in b:
                yield i  #生成器
                b.add(val)

    a=[{'x':1,'y':5},{'x':2,'y':7},{'x':1,'y':5},{'x':1,'y':100}]

    print(a)

    print( list(dedupe(a,key=lambda d:(d['x'],d['y']))) )


def ch1_11():
    '''
    1.11 对切片命名
    避免在代码中存在硬编码的索引值，可以利用slice对切片命名
    '''
    print("\nch1_11:")

    items = [1,2,3,4,5,6,7,8,9]

    odd_slice = slice(0,9,2)
    odd = items[odd_slice]

    print(odd_slice.start,odd_slice.stop,odd_slice.step)
    print(odd)


def ch1_12():
    '''
    1.12 找出序列中出现次数最多的元素
    使用collections 中的Counter
    '''

    print("\nch1_12:")

    from collections import  Counter

    scores_one = [99,89,87,76,98,76,89,92,89,67,59,78,98,92,90,85,56]
    scores_two = [100,89,56,98,78,97,96,99,94,93,91,90]

    one_same_top_three = Counter(scores_one).most_common(3)
    print(one_same_top_three)

    #Counter可以使用各种数学运算操作
    all_same_top_three = ( Counter(scores_one) + Counter(scores_two) ).most_common(3)
    print(all_same_top_three)


def ch1_13():
    '''
    1.13 通过公共键对字典列表排序
    使用operator中的itemgetter得到字典的值
    '''

    print("\nch1_13:")

    from operator import  itemgetter

    rows = [
        {'fname':'A','lname':'B','uid': 1001},
        {'fname':'B','lname':'C','uid': 1003},
        {'fname':'E','lname':'D','uid': 1002},
        {'fname':'A','lname':'F','uid': 1010},
    ]

    rows_by_uid_and_fname =sorted(rows, key=itemgetter('uid','fname'))

    print(rows_by_uid_and_fname)

    #使用lambda 如果考虑性能使用itemgetter
    rows_by_uid = sorted(rows, key=lambda s:s['uid'], reverse=True)
    print(rows_by_uid)

    print(  max(rows, key=itemgetter('uid')) )


def ch1_14():
    '''
    1.14 对不原生支持比较操作的对象排序
    sorted 传入key参数
    '''

    print("\nch1_14:")

    from operator import  attrgetter  #属性提取

    class User:
        def __init__(self,user_id):
            self.user_id = user_id
        def __repr__(self):
            return 'User({})'.format(self.user_id)

    users = [User(1),User(2),User(3),User(100)]
    users_by_user_id= sorted(users, key=lambda s:s.user_id, reverse=True)

    print(users_by_user_id)

    users_by_user_id= sorted(users, key=attrgetter('user_id'), reverse=True)
    print(users_by_user_id)

    print(max(users, key=attrgetter('user_id')))


def ch1_15():
    '''
    1.15 根据字段将记录分组
    使用itertools.groupby
    '''

    print("\nch1_15:")

    from operator import  itemgetter
    from itertools import  groupby

    rows = [
        {'cost': 190, 'date': '07/02/2016'},
        {'cost': 100, 'date':'07/01/2016'},
        {'cost': 10, 'date':'07/18/2016'},
        {'cost': 89, 'date':'07/10/2016'},
        {'cost': 78, 'date':'07/10/2016'},
        {'cost': 1000, 'date':'07/01/2016'}
    ]

    #先按时间排序
    rows.sort(key=itemgetter('date'))

    #分组
    for date, items in groupby(rows,key=itemgetter('date')):
        print(date)
        for i in items:
            print(i)

    #如果不排序，使用一键多值字典
    from collections import  defaultdict

    dict = defaultdict(list)
    for row in rows:
        dict[row['date']].append(row)
    print('\n defaultdict:')
    print(dict['07/01/2016'])


def ch1_16():
    '''
    1.16 筛选序列中的元素
    使用列表推导式和生成器表达式，或者使用itemtools.compress
    '''

    print("\nch1_16:")
    mylist=[1,4,-6,9,-7,-5,99,100,-1]
    list1=[n for n in mylist if n > 0]
    print(list1)

    list2=(n for n in mylist if n < 0)
    for i in list2:
        print(i)

    def is_int(val):
        try:
            x = int(val)
            return True
        except ValueError:
            return False
    mylist=['1','2','3','4','-','N/A','5']

    list3 = list(filter(is_int, mylist))
    print(list3)

    numbers = [
        '1',
        '2',
        '3',
        '4'
    ]

    counts=[4,100,9,0]

    from itertools import compress

    more5 =[n > 5 for n in counts]
    restult=list(compress(numbers, more5))
    print(restult)

def ch1_17():
    '''
    1.17 从字典中提取子集
    利用字典推导式

    '''

    print("\nch1_17:")
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55
    }

    p1 = {key:value for key, value in prices.items() if value > 200}
    print(p1)


def ch1_18():
    '''
    1.18 将名称映射到序列的元素中
    使用collections.namedtuple（命名元组)
    命名元组不可变，使用_replace替换元素
    '''

    print("\nch1_18:")

    from collections import  namedtuple
    Subscriber = namedtuple('Subscriber',['addr','joined'])
    sub = Subscriber('xxx@xx.com','2016-01-01')
    print(sub, sub.addr, sub.joined)

    #替换字典的作用
    s = Subscriber('1@1.com','2016-01-02')
    #命名元组不可变，使用_replace替换元素
    s = s._replace(addr='2@2.com')
    print(s)


def ch1_19():
    '''
    1.19 同时对数据做转换和换算
    '''

    print("\nch1_19:")

    nums = [1,2,3,4,5]
    s = sum(x*x for x in nums)
    print(s)

    import  os
    files = os.listdir('.')
    if any(name.endswith(".py") for name in files):
        print('Yes')
    else:
        print('No')


def ch1_20():
    '''
    1.20 将多个映射合并为单个映射
    使用collections ChainMap解决
    '''

    print("\nch1_20:")

    from collections import ChainMap

    a={'x':1,'z':3}
    b={'y':2,'z':4}

    c = ChainMap(a,b) #使用原始的字典
    print(c['x'],c['y'],c['z'])

    print(list(c.keys()),list(c.values()))

    #用新建字典代替
    merged = dict(b)
    merged.update(a)
    print(merged['x'],merged['y'],merged['z'])

def main():

    for i in range(1,21):
        func='ch1_%d()'%(i)
        exec(func)


if __name__ == "__main__":
    main()