
# Markdown-Slide
在线教学展示幻灯片

---

### 简单介绍

- 这是一个在线 PPT， 是解决 PPT 排版不美观不方便的利器。
- 同时，软件基于浏览器页面制作，您可以一次制作，在几乎所有设备上得到一致的体验。
- 这个项目希望能够将前端技术应用于教育领域，使用简单的方式编写教学幻灯片。

- - -

#### 编写的方式 —— Markdown
- 我们采用了 Markdown 语法对文本进行渲染，当您通过侧边的教程对这些渲染有一定的印象时，您便可以开始写作了。
- 当然，如果您对于 Markdown 有一定的写作经验，可以使用添加幻灯片分隔符的方式对您的文档进行改造！

---

##  快速开始
在这一部分，我们将会编写一个 Markdown 用来渲染我们的在线 PPT。

- - -

### 第一步 —— 编写 Markdown 文件
您可以在一个 **.txt 文件** 中编写符合 markdown 语法的文件然后更改后缀名为 .md。

在编写的时候，由于排版原因，您可能需要在编写完成之后放置到我们的软件中进行查看，若不符合您的要求，则需要自己更改。

[关于 Markdown 语法对应的详细渲染，请点击这里](./show.html?https://cdn.jsdelivr.net/gh/KonghaYao/notuse/ppt/markdown.md)

- - -

### 第二步 —— 根据需要打包您的文件
- 可以直接进行展示的有 .md 后缀名的文件，但是若是这个文件中引入了本地的图片等多媒体文件，需要使用下面的方式引入
- 若是您需要导入本地的图片，可以将 .md　文件连同您的图片一起压缩为 .zip 格式，我们的软件可以自动解析并还原您打包内的图片文件。

- - -

![使用本地 zip 文件](https://cdn.jsdelivr.net/gh/KonghaYao/notuse/ppt/zipfile.png)

- 若您拥有像 github 这样的代码仓库，可以直接使用 url 地址导入您的在线文件而不需要下载。

- - -

### 第三步 —— 展示文件
您可以直接将文件拖入并加载文件

- - -


## 简单的幻灯片操作
1. 使用方向键更换幻灯片 
2. 在幻灯片打开的时候，按 f 键可以开关全屏状态。
3. 在幻灯片打开的时候，按 o 键可以开关预览模式



---

### 关于项目

感谢所有的开源插件的开发者，他们的成果为我们的项目提供了极大的帮助。

- - -

#### 项目依赖

- 整个项目基于 **[reveal.js](https://github.com/hakimel/reveal.js)** 提供的 api 进行文本转幻灯片的操作。
- 同时，我们使用了很好用的 **[weetalert2](https://github.com/sweetalert2/sweetalert2)** 作为通知插件。
- 我们的项目通过 [jsDelivr](http://www.jsdelivr.com/) 引入了相关的 js 和 css, 所有的插件通过这个网站提供的免费 api 载入。
- 我们将项目迁移到了 [Gitee](https://gitee.com/) 仓库中，并通过Gitee Pages 搭建了这个应用。


- - -

#### 项目的创新

- 原本 reveal.js 是不支持在线自动解析 Markdown 文本的，但是经过我们的努力，我们使用 HTML5 和 js Ajax 的特性，成功地将这个软件制作出来，使得我们的项目**可以通过网络 URL 或本地上传的方式注入您的幻灯片**。

- - -

#### 项目的创新

- reveal.js 原本是直接 “翻译” Markdown 文本作为幻灯片页面，但是我们通过 Javascript 和 css 扩充了**排版结构和问题选项**，若是未来有可能，我们将会扩充更加多的方便的扩展功能。

---

### 项目开发者
| [动中之动](https://www.gitee.com/dongzhongzhidong)           | [泽林白鹿](https://www.gitee.com/Lerror0)                    | [jabt](https://www.gitee.com/jabt)                           | [Cheeseb](https://www.gitee.com/Cheeseb)                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![](https://portrait.gitee.com/uploads/avatars/user/1780/5342313_dongzhongzhidong_1604048676.png!avatar200) | ![](https://portrait.gitee.com/uploads/avatars/user/2744/8233054_Lerror0_1604047833.png!avatar200) | ![](https://portrait.gitee.com/uploads/avatars/user/2668/8004884_jabt_1599396827.png!avatar200) | ![](https://portrait.gitee.com/uploads/avatars/user/2753/8260480_Cheeseb_1604304552.png!avatar200) |


