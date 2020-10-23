
# [Pandas](http://online-ppt-education.gitee.io/online-ppt/show.html?file=https://cdn.jsdelivr.net/gh/konghayao/notuse/Pandas.md)

---



## 相关库

在一个.py中最好载入下面的库，下面的代码示例默认为这个配置。

```python
import numpy as np #用于描述一些数学符号
import pandas as pd # 主要库
import matplotlib.pyplot as plt # 绘图库，主要用来看看图像
```

---



## Series 与 DataFrame

数据操作时最常用的是 DataFrame（下面简称 df）。df 是一个二维表，而 Series 是一维表。我们一般不会主动操作这些对象，这些对象一般是通过载入数据文件时直接载入。

---



## 从载入文件开始

原始数据一般也是一个二维表，通常是可以使用 Excel 打开的文件格式，[通过 Excel 可以把数据文件转化为 CSV 格式](https://jingyan.baidu.com/article/5d6edee214719c99eadeece0.html)，方便载入Python 分析。

```python
df = pd.read_csv('./date.csv') # df 是一个 DataFrame。
```

载入的文件在 Python 中读取为 DataFrame , 为二维表的格式,下面的所有代码中的 df 都是类似于上面的 df。

---



# DataFrame 基本操作

---



## 表的操作

### 行和列的操作

在 pandas 中的行索引是一个表示顺序的东西，对于每一行的数据都可以认为是一个对象，而列索引为属性名称。

```python
df['date'] # 取列
df['noExist'] = [1,1,2,3] # 若对不存在的属性赋值，会创建一个新列

df.drop(['noExist','data'],axis=1)# 删除列，指定axis = 1 时为列，0为行，数组内为要删除的东西

df.T # 行列转置
```

---



### iloc 函数

iloc 函数像 Excel 中的框选操作，可以选中框选中的部分。

```python
df.iloc[1:,1:] #行索引值大于1并列索引值大于1 的方框内的值都选中。
```

---



## 数据格式 划分与转化

我们操作的一般只有 字符串，数值和日期型数据，从 CSV 载入的数据会经过自动类型转换，但是一般不准，所以我们需要在 read_csv 中定义数据格式( dtype )。![在这里插入图片描述](https://www.pianshen.com/images/246/6918933946f695116210e08c251cf27e.png)

```python
df = pd.read_csv('./date.csv', dtype={
    "year": "int",
    "day": "int",
    "month": "float",
}, parse_dates=['Date'])#parse_dates=['Date'] 用于时间类型转化
```

---



但是上面这一种只适合部分情况，当遇到数字和字符串结合在一起的情况下定为 “int” 或 “float” 时，会导致报错。例如，数字格式和空格杂糅在一列时，会报错。

这时候我们需要强制类型转化。

```python
df = pd.read_csv('./date.csv', dtype={
    "year": "int",
    "day": "int",
    "month": "int",
},)

# 下面这一行将 data 列强制转化为数值型，若不能转化为数值型会转化为 NaN。
df['data'] = df['data'].apply(pd.to_numeric, errors='coerce')
```

---



有些情况下，货币符号和数字结合在一起，需要通过文本处理去除。

```python
# 注意，这是 pandas 自带的正则解析，所以不用导入 re 库
# 这一行使用了正则表达式将非数字的字符全部替换为空，然后转格式
df['money'] = df['money'].astype(np.str).str.replace(r'\D', '')
df['money'] = df['money'].apply(pd.to_numeric, errors='coerce')
```

---



## 数据处理

pandas 是数据的批量处理工具，批量处理数据十分容易，但是对于查看和人工填入数据没有 Excel 好用，所以可以配合 Excel 人工填写。

1.  pandas 分析一般先将完全重复的行删除。

2.  然后找到一个理论上没有重复项的列作为索引

3.  保存索引的所有重复项为 CSV ，人工处理

4.  导入 CSV 并开始缺失值操作
5.  查看异常值

---



### 具体操作

下面的小节全部为技术代码，应该按照数据处理需要来使用。

---



### 缺失值

缺失值是没有进行填写而默认的值，可以为实际的值（例如 -1），也可以为 NaN。

#### 删除整行

```python
# 首先查看缺失情况         得到的是缺失的值的占比
print(df.apply(lambda col:sum(col.isnull())/col.size))
# 依据某一行的 空值 将这个行删掉
df.dropna(subset=['duration'], axis=0, inplace=True)
```

---



#### 对缺失值填充

我们使用 fillna 这个函数对缺失值填充

```python
# 首先查看缺失情况
print(df.apply(lambda col:sum(col.isnull())/col.size))
# 填充为这一列的中位数
df['duration'].fillna(df['duration'].mean(), inplace=True)
# 可以设置使用周围的值填充 ffill 表示向下填充，bfill 表示向上填充
df['data'].fillna(method='ffill', inplace=True)
```

---



### 重复值

当处理完缺失值后，我们需要查看重复值。有些数据拥有 ID 序号等等具有唯一性的属性，这些属性重复时，需要处理。

```python
# 查看重复值
dup = df[df.duplicated(subset=['movie_title'], keep=False)]
# keep 是 默认值 时不会把重复项中的第一项收集起来，False 时收集全部重复项

print(dup.sort_values(by=['movie_title']))  # 查看排序后的重复值
dup.to_csv('./dup.csv', index=0) #  保存为 csv 查看并修改
```

---



重复值若不是完全重复，一般需要查看后才能删除，所以需要另外使用 Excel 查看编辑。

```python
# 完全重复值需要先于缺失值进行删除
df.drop_duplicates(inplace=True)

#部分重复值 需要找一个索引并保存下来，进行人工分析
dup = df[df.duplicated(subset=['movie_title'], keep=False)]
dup.to_csv('dup.csv', index=0)
print(dup.size)

########### 人工处理后 把更改项更新上去 ########
print(df.size)
df.drop_duplicates(subset=['movie_title'], keep=False,inplace=True)
df = df.append(pd.read_csv('dup.csv', encoding='UTF-8'))
print(df.size)
```

---



### 异常值

异常值可以是越界的数据，不合理的数据，这些需要经过限定操作。

而有一定规律的数据中的异常值，我们可以使用下面的方式检查

![img](https://img2018.cnblogs.com/i-beta/1764470/201911/1764470-20191129003646428-796731845.png)

[图来源](https://www.cnblogs.com/tinglele527/p/11955103.html)

---

#### 查看异常值

下面的代码均更改自 [pandas - 异常值处理](https://www.cnblogs.com/tinglele527/p/11955103.html)

下面两种方式均适合评估一个对象的某一属性的变化，或某一属性具有正太分布特性的部分

```python
# 标准差检查适合正太分布数据
xbar = df['imdb_score'].mean()
xstd = df['imdb_score'].std()
print('标准差法异常值上限检测:\n', '异常'if any(
    df['imdb_score'] > xbar + 2 * xstd) else "正常")
print('标准差法异常值下限检测:\n', '异常'if any(
    df['imdb_score'] < xbar - 2 * xstd) else "正常")

# 箱线图法
Q1 = df['imdb_score'].quantile(q=0.25)
Q3 = df['imdb_score'].quantile(q=0.75)
IQR = Q3 - Q1
print('箱线图法异常值上限检测:\n', '异常'if any(df['imdb_score'] > Q3 + 1.5*IQR) else '正常')
print('箱线图法异常值下限检测:\n', '异常'if any(df['imdb_score'] < Q1 - 1.5*IQR) else '正常')
```

---

#### 处理异常值

一般有删除和填充两种方式。

```python
# 删除的方式
print(df.size) # 只需要在下式的 判断条件更改为上面的4个条件中的任何一个就可以删除
df.drop(df[df['image_score'] > xbar + 2 * xstd].index, axis=0, inplace=True)
print(df.size)
```

---

#### 填充异常值

```python
 # 用符合边界的最大最小值 更改大于上边界和小于下边界的值
UP = Q3 + 1.5 * IQR # 上边界
DOWN = Q3 - 1.5 * IQR # 下边界

df[cols][df[cols] > UP] = df[cols][df[cols] < UP].max()
df[cols][df[cols] < UP] = df[cols][df[cols] > DOWN].min()
print('异常值替换后的数据统计特征：\n', df[cols].describe())
```





### 条件替换

根据条件替换某一列/行中的某些值 

```python
df['data'] = np.where(df.data < 10, 0, 1)#第一个参数为条件， 0 为否定赋值， 1 为肯定赋值
```

## 数据采样

数据透视表

数据重采样

## 高级操作

### 归一化

[归一化](https://www.cnblogs.com/kuangkuangduangduang/p/10279053.html)