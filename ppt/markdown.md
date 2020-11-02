---
title: Markdown 语法
theme: white
---

#  Markdown-Slide 


  Markdown 语法对应

---

## 总述
- Markdown-Slide 在渲染 Markdown 的时候对于基本的 Markdown 是完全支持的。
- Markdown-Slide 在 reveal.js 的基础上创建了一些自定义的语法，可以提供更为强大的功能。

- - -

## 使用什么软件来编写？

- Markdown-Slide 并没有提供 Markdown 的编写器， 但是网络上有很多的在线 Markdown 编辑器，如[马克飞象](https://maxiang.io/),[CMD Markdown](https://www.zybuluo.com/mdeditor)等，本地编辑器软件例如[Typora](https://www.typora.io/)（最为推荐）等。

- 他们可能对于我们自定义的语法展示不全，但是熟悉我们的自定义语法后仍然具有可读性！

[我们的自定义语法]()

---

# 开始编写 .md 文件！

---

## 创建一页幻灯片

- 我们的项目依赖于开源项目 reveal.js 所以我们使用 `---` 作为每一横页的分隔符号。
- 如果想要让 幻灯片 向下播放，则使用 - - - 即可实现向下转换。
-  推荐在 `---`，- - - 和正文之间使用换行断开以免发生渲染错误。



---

## 标题渲染

通过 # 可以控制标题的大小，提供更好的展示效果

- - -

| 标记             | 对应渲染          |
| ---------------- | ----------------- |
| 普通文本         | 普通文本          |
| \# 一级标题      | <h1>一级标题</h1> |
| #\# 二级标题     | <h2>二级标题</h2> |
| ##\# 三级标题    | <h3>三级标题</h3> |
| ###\# 四级标题   | <h4>四级标题</h4> |
| ####\# 五级标题  | <h5>五级标题</h5> |
| #####\# 六级标题 | <h6>六级标题</h6> |

---

## 文字特效
| 标记              | 对应渲染       |
| ----------------- | -------------- |
| **粗体**          | **粗体**       |
| \*斜体*           | *斜体*         |
| *\*\*斜体加粗\*** | ***斜体加粗*** |
| \~\~删除线\~\~    | ~~删除线~~     |

---

## 引用区域

引用文本可以用在突出文本，并不是只使用在引用他人话语的场景。
例子在下面。

- - -

#### 例子：

<div class = 'cols'>


<div>

##### 原来的文本

\> 这是一个文本渲染的区域

</div>
<div>

##### 渲染后的文本

>   这是一个文本渲染的区域

</div>
</div>

---

## 列表
 列表有 ***有序列表*** 和 ***无序列表*** 两种。

---

### 无序列表

列表的声明只需要在一行文本的前面使用 `*` 或`+`或`-`和文本空格隔开就可以渲染为一个列表。

- - -

#### 例子：

<div class = 'cols'>
<div>

##### 原来的文本

\- 一

\* 二

\+ 三


</div>
<div>

##### 渲染后的文本
- 一

* 二

+ 三

</div>
</div>

---

### 有序列表

有序列表直接使用数字即可

- - -

#### 例子：
<div class='cols'>


<div>



##### 原来的文本

\1.  文本

\2.  文本

\3.  文本


</div>
<div>


##### 渲染后的文本

1.  文本
2.  文本
3.  文本

</div>
</div>

---

## 网页跳转 和 图片展示 


<div class='cols'>
<div>

###### 源代码

[baidu\](跳转连接的URL)

###### 渲染后的代码

[baidu](https://www.baidu.com) ---它能转到百度

</div>
<div>

###### 源代码

![baidu\](图片的URL)

###### 渲染后的图片

![baidu](https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png) 

</div>

- - -

## 关于 URL 路径的问题


- URL 在 md 代码中可以为绝对路径，即网络上提供的路径。

- URL 同样可以为相对地址，但是包括相对地址时，需要压缩包含 md 文件夹为 zip 文件。详细的打包方式请查看[我们项目的gitee首页]()。


---

## 单独视频

```text
<video data-src='http://nndoenfne/ppt/video.mp4' controls>
替换 data-src 中路径为你想要的视频地址
然后写到某一页中即可展示
```

<video data-src='https://cdn.jsdelivr.net/gh/KonghaYao/notuse/ppt/video.mp4' controls>

---

## 代码展示
这是 reveal.js 提供的功能之一，可以很好地展示代码的相关信息，非常适合为 编程教学者使用。

```js
​```js [1-2|3|4]

​```

js 代表的是编程语言的种类
[1-2|3|4] 表示点击下一页时展示 1-2 行代码，第 3 行代码，第 4 行代码。
```

- - -

```js [1|3-4|6]
const ALL = { Ajax, Cookies, ...Copy};

class JSpider {}
Object.assign(JSpider.prototype, ALL);

export default JSpider;

```




---

## 数学公式输入

reveal.js 采用的是 MathJax 对 LaTeX 公式进行渲染，我们可以在markdown 文档中直接书写公式。

![百度百科对 LaTeX 的说明](https://cdn.jsdelivr.net/gh/KonghaYao/notuse/ppt/latex.png)

- - -

## 数学公式

```text
$$
E_0=mc^2 \\
a^2+b^2=c^2
$$
把上面的这一行写入文档即可呈现下面的效果
```


$$
E_0=mc^2 \\
a^2+b^2=c^2
$$

由于LaTeX 的公式的相关符号很多，网络上教程也有很多，所以我们推荐查看 MathJax 的 [XMind的 LaTeX帮助文档](https://www.xmind.cn/faq/question/what-command-does-xmind-equation-support/) 

---

## 我们的独特语法

1.  这些语法是我们在 reveal.js 的 Markdown 语法渲染上提供的更为实用的语法。

2.  这些语法是基于 Markdown 编辑器可以渲染的形式进行书写的，所以在编写者编写的时候仍然具有可读性！

---

## YAML 文件情况

YAML 头在很多博客系统中可以渲染，我们采用 YAML 来表示作者对于 Markdown-Slide 的总的格式构建, 很多设置可以通过 YAML 进行设置。

- - -

### 写 YAML 标题

**YAML 必须写在整个文档的开头！！**

YAML 的格式，冒号前面为指定属性，**冒号与后面的描述必须有一个空格的间隔**。

```yaml
 ---
title: 这是一个测试文件
theme: white
transition: zoom
 ---
```

- - -

-   最常用的是 theme 属性，您可以填入 **black,white,league,beige**等 这些可以改变 **每一页的主题色**
-   接着的是 transition 属性，您可以写入 **fade,slide,convex,concave,zoom** 这个可以改变 每一页之间转换的动画。

---

## 选择题渲染

我们为了保护 markdown 文档的可读性，使用 HTML 的书写方式。


![question](https://cdn.jsdelivr.net/gh/KonghaYao/notuse/ppt/question.png)

- - -

<question>
问题 1 
请选择正确答案 ABCD
***
- [ ] A
- [x] B
- [ ] C
- [ ] D
<!-- 1,2,3,4 -->
<!-- 解析 -->
<!-- 这是一个关于这一题的解析 -->
<!-- 这个可以使用两行进行描写 
同时支持换行
 -->
***
</question>

- - -

