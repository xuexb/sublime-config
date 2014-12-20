# 我的sublime配置

## 插件包

### emmet

> 一个输出`html`结构神器

* tab键补全
* 以对`css`属性空格作处理 `.test{overflow: hidden;}` -> `.test{overflow:hidden;}`

### jsFormat

> js格式化

* `Mac` control+shift+f
* `Win` ctrl+alt+f

### OmniMarkupPreviewer

> md文档预览

* `Mac` control+f12
* `Win` ctrl+f12

### open_browser

> 在浏览器打开，部分代码摘自ququ

* `Mac` command+f12
* `Win` ctrl+f12

### DocBlockr

## nodejs运行环境

必须安装有`nodejs`环境，如果没有设置过`PATH`变量，则需要修改`nodejs.sublime-build`文件里的路径，在JS文件里执行命令，
js文件所在路径不能有中文

* `Mac` 目前不支持或者我配置不对
* `Win` ctrl+b

**目前在mac上运行不通过**

## snippet

### js

* define - 定义cmd模块
* console.log - 调试输出
* parseInt - 解析为数字
* console.time - 调试时间

### php

* debug - 打印信息并中断

## Todo

把`open_browser`的站点配置提出来为`json`文件