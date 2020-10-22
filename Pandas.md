
# Pandas
http://online-ppt-education.gitee.io/online-ppt/show.html?file=https://cdn.jsdelivr.net/gh/konghayao/notuse/Pandas.md
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



### 缺失值

### 重复值

### 异常值

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