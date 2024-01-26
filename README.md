# StreaMonitor
A Python3 application for monitoring and saving (mostly adult) live streams from various websites.

Inspired by [Recordurbate](https://github.com/oliverjrose99/Recordurbate)

## 支持的站点
| 站点名称         | 缩写 | 别名                       | 特殊情况               | 可选择的分辨率     |
|----------------|--------------|-----------------------------|------------------------|-----------------------|
| Amateur.TV     | `ATV`        |                             |                        | Yes                   |
| Bongacams      | `BC`         |                             |                        | Yes                   |
| Cam4           | `C4`         |                             |                        | Yes                   |
| Cams.com       | `CC`         |                             |                        | Currently only 360p   |
| CamSoda        | `CS`         |                             |                        | Yes                   |
| Chaturbate     | `CB`         |                             |                        | Yes                   |
| Cherry.TV      | `CHTV`       |                             |                        | Yes                   |
| Dreamcam VR    | `DCVR`       |                             |                        | No                    |
| Flirt4Free     | `F4F`        |                             |                        | Yes                   |
| ManyVids Live  | `MV`         |                             |                        | Yes                   |
| MyFreeCams     | `MFC`        |                             |                        | Yes                   |
| SexChat.hu     | `SCHU`       |                             | use the id as username | No                    |
| StreaMate      | `SM`         | PornHubLive, PepperCams,... |                        | Yes                   |
| StripChat      | `SC`         | XHamsterLive,...            |                        | Yes                   |
| StripChat VR   | `SCVR`       |                             | for VR videos          | No                    |

Currently not supported:
* ImLive (Too strict captcha protection for scraping)
* LiveJasmin (No nudity in free streams)

There are hundreds of clones of the sites above, you can read about them on [this site](https://adultwebcam.site/clone-sites-by-platform/).

## 要求
* Python 3
  * 使用pip安装requirements.txt中列出的包。
* FFmpeg

## 使用方法

该应用程序具有以下界面：
* 控制台
* 通过ZeroMQ的外部控制台（有点工作）
* Web界面（仅限状态）

#### 启动和控制台
启动下载器（目前尚未分叉）\
自动从配置文件导入所有流媒体用户。
```
python3 Downloader.py
```

在控制台上，您可以使用以下命令：
```
add <用户名> <站点> - 将流媒体用户添加到列表（同时开始监控）
remove <用户名> [<站点>] - 从列表中删除流媒体用户
start <用户名> [<站点>] - 启动监控流媒体用户
start * - 启动所有
stop <用户名> [<站点>] - 停止监控
stop * - 停止所有
status - 显示状态
status2 - 稍微更可读的状态表
quit - 安全退出（按CTRL-C也会执行此操作）
```

对于`username`输入，通常必须输入原始URL中表示的用户名。
某些站点区分大小写。

对于`site`输入，可以使用站点名称的完整格式或简短格式。 （不区分大小写）

#### "远程"控制器
添加或删除要录制的流媒体用户（同时保存配置文件）
```
python3 Controller.py add <用户名> <网站>
python3 Controller.py remove <用户名>
```

启动/停止录制流媒体用户
```
python3 Controller.py <start|stop> <用户名>
```

列出配置中的流媒体用户
```
python3 Controller.py status
```

#### Web interface

You can access the web interface on port 5000. 
It just prints the same information as the status command. 
You can also get a list of the recorded streams.

Further improvements can be expected.

## Docker support

You can run this application in docker. I prefer docker-compose so I included an example docker-compose.yml file that you can use.
Simply start it in the folder with `docker-compose up`.

## Configuration

You can set some parameters in the parameters.py.

## Disclaimer

This program is only a proof of concept and education project, I don't encourage anybody to use it. \
Most (if not every) streamers disallow recording their shows. Please respect their wish. \
If you don't, and you record them despite this request, please don't ever publish or share any recordings. \
If you either record or share the recorded shows, you might be legally punished. \
Also, please don't use this tool for monetization in any way.
