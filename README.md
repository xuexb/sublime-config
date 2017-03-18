# 我的sublime插件配置 - v3 

> [点击这里查看v2](https://github.com/xuexb/sublime-config/tree/v2)

## 安装插件

> 所有配置均覆盖到`Settings-User`里, `Settings-Default`配置不要动, 以下是我常用的插件, 兼容了百度代码规范

- Babel - 你懂的
- ConvertToUTF8 - utf8编码
- DocBlockr - 注释自动化
> 配置文件[./docblockr.sublime-settings](./docblockr.sublime-settings)到`DocBlockr/Settings - User`里
- Emmet - 自动补全, 自动完成
> 配置文件[./emmet.sublime-settings](./emmet.sublime-settings)到`Element/Settings - User`里
- ETPL - 百度efe模板引擎
> 配置文件[./ETPL.sublime-settings](./ETPL.sublime-settings)到`ETPL/Settings - User`里
- jsFormat - 格式化js, 支持片段格式化
> 配置文件[./jsFormat.sublime-settings](./JsFormat.sublime-settings)到`jsFormat/Settings - User`里
- OmniMarkupPreviewer - markdown文件实时浏览器里预览
- SideBarEnhancements - 快捷侧边栏
- MarkdownEditing - markdown文件编辑高亮
- fecs - 格式化、检测代码 - 百度风格
> [https://github.com/xuexb/sublime-fecs](https://github.com/xuexb/sublime-fecs)

## 其他

- `./*.sublime-keymap` - 快捷键配置
- `./(JavaScript|CSS|vue).sublime-settings` - 对应文件的的配置, 如: 被支持的扩展名
- `./nodejs.sublime-build` - 编辑器内运行nodejs, `command+b`
- `Preferences.sublime-settings` - 主配置文件, 如: 120标尺、4空格缩进、自动tab转空格等

## 解决sublime text3安装插件报错

编辑`Package Control.sublime-settings`配置文件, 修改:

```json
{
    "channels":
    [
        "https://github.xuexb.com/static/sublime/channel_v3.json"
    ]
}
```
