这个项目受到了 [BaiduBlogTransfer](https://github.com/cheezer/BaiduBlogTransferer) 这个项目的启发. 但是运行时候发现pycookiecheat这个库不能兼容最新的chrome浏览器：会在在 `chrome_decrypt`里面的 `decode('utf-8')` 出错

-----

把 http://wenzhang.baidu.com/ 内容保存到 "wenzhang_full.html" 文件里

如果是chrome插件的话，安装一个editthiscookie插件，并且输出格式选择"Perl:LWP", 保存到cookies.txt文件. 虽然这个格式声称是Set-Cookie3 format, 但是不能被python cookielib正确识别. 所以需要手动修改cookies.txt

- 去掉 // 注释部分
- 在开头加上 `#LWP-Cookies-0.0`

下面是一个参考格式

```
#LWP-Cookies-0.0
Set-Cookie3: __cfduid=d7bb55765059ed2a8ab8d57eabe0bc3dc1469109976; path="/"; domain=.baidu.com; path_spec; expires="1500645975.594865"; version=0
Set-Cookie3: BAIDUID=B05F139B39EA36674DC53A15CFDE2A67:FG=1; path="/"; domain=.baidu.com; path_spec; expires="3609196457.617117"; version=0
```

运行`./crawler.py` 会输出output.html. 这个html文件是一个single file.

如果想修改样式的话，可以修改里面的`generate_single_html`函数
