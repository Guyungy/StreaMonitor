# StreaMonitor
## 支持的站点
| 站点名称          | 缩写     | 别名                          | 特殊情况                   | 可选择的分辨率             |
| ------------- | ------ | --------------------------- | ---------------------- | ------------------- |
| Amateur.TV    | `ATV`  |                             |                        | Yes                 |
| Bongacams     | `BC`   |                             |                        | Yes                 |
| Cam4          | `C4`   |                             |                        | Yes                 |
| Cams.com      | `CC`   |                             |                        | Currently only 360p |
| CamSoda       | `CS`   |                             |                        | Yes                 |
| Chaturbate    | `CB`   |                             |                        | Yes                 |
| Cherry.TV     | `CHTV` |                             |                        | Yes                 |
| Dreamcam VR   | `DCVR` |                             |                        | No                  |
| Flirt4Free    | `F4F`  |                             |                        | Yes                 |
| ManyVids Live | `MV`   |                             |                        | Yes                 |
| MyFreeCams    | `MFC`  |                             |                        | Yes                 |
| SexChat.hu    | `SCHU` |                             | use the id as username | No                  |
| StreaMate     | `SM`   | PornHubLive, PepperCams,... |                        | Yes                 |
| StripChat     | `SC`   | XHamsterLive,...            |                        | Yes                 |
| StripChat VR  | `SCVR` |                             | for VR videos          | No                  |


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

### 添加
```
python3 Controller.py add xxx SC
```
```
python3 Controller.py add beverlyvega CB
```
删除
```
python3 Controller.py remove xxx
```

启动/停止录制流媒体用户
```
python3 Controller.py <start|stop> <用户名>
```

列出配置中的流媒体用户
```
python3 Controller.py status
```

#### Web界面

您可以在端口5000上访问Web界面。
它只是打印与状态命令相同的信息。
您还可以获取记录的流媒体列表。

可以期待更多的改进。

## Docker支持

您可以在Docker中运行此应用程序。我更喜欢使用docker-compose，因此我包含了一个示例docker-compose.yml文件供您使用。
只需在包含该文件的文件夹中使用 `docker-compose up` 启动它。

## 配置

您可以在 parameters.py 文件中设置一些参数。

## 免责声明

此程序仅为概念验证和教育项目，我不鼓励任何人使用它。\
大多数（如果不是全部）的流媒体用户都禁止录制其演出。请尊重他们的意愿。\
如果您违背此要求而记录了他们，千万不要发布或分享任何录音。\
如果您录制或分享了录制的演出，可能会受到法律惩罚。\
此外，请不要以任何方式使用此工具进行盈利。
