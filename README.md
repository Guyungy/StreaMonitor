StreaMonitor

一个基于 Python3 的应用程序，用于监控和保存来自各个网站的（主要是成人内容）直播。

灵感来源于 Recordurbate

支持的网站：

| 网站名称       | 缩写  | 别名                      | 特殊情况                         | 可选分辨率 |
| -------------- | ----- | ------------------------- | -------------------------------- | ---------- |
| Bongacams      | BC    |                            | 是                               |
| Cam4           | C4    |                            | 是                               |
| Cams.com       | CC    |                            | 目前仅支持 360p                   |
| CamSoda        | CS    |                            | 是                               |
| Chaturbate     | CB    |                            | 是                               |
| Dreamcam VR    | DCVR  |                            | 否                               |
| Flirt4Free     | F4F   |                            | 是                               |
| MyFreeCams     | MFC   |                            | 是                               |
| SexChat.hu     | SCHU  | 使用 ID 作为用户名         | 否                               |
| StreaMate      | SM    | PornHubLive, PepperCams... | 是                               |
| StripChat      | SC    | XHamsterLive,...           | 是                               |
| StripChat VR   | SCVR  | 专用于 VR 视频             | 否                               |
| XLoveCam       | XLC   |                            | 否                               |

当前不支持的网站：

- Amateur.TV（他们现在使用 Widevine 加密）
- Cherry.tv（他们转用了 Agora）
- ImLive（验证码保护过于严格，无法抓取）
- LiveJasmin（免费直播中没有裸露内容）
- ManyVids Live（他们转用了 Agora）

上面提到的网站有数百个克隆站点，详细信息可以在此网站上阅读。

**系统要求：**

- Python 3
- 使用 `pip` 安装 `requirements.txt` 中列出的依赖包
- FFmpeg

**使用方法：**

应用程序提供以下接口：

- 控制台
- 通过 ZeroMQ 的外部控制台（暂时支持）
- Web 界面

**启动和控制台操作：**

启动下载器（目前不支持分叉）：

- 自动从配置文件中导入所有主播。
  
```bash
python3 Downloader.py
```

控制台可用命令：

- `add <用户名> <网站>` - 将主播添加到列表中（并开始监控）
- `remove <用户名> [<网站>]` - 从列表中删除主播
- `start <用户名> [<网站>]` - 开始监控指定主播
- `start *` - 开始监控所有主播
- `stop <用户名> [<网站>]` - 停止监控指定主播
- `stop *` - 停止监控所有主播
- `status` - 显示状态
- `status2` - 更加可读的状态表格
- `quit` - 清理退出（按 CTRL-C 也可以实现）

输入主播用户名时，通常需要输入房间原始 URL 中的用户名。有些网站对大小写敏感。

输入网站时，可以使用完整名称或缩写，且对大小写不敏感。

**“远程”控制器：**

- 添加或删除需要录制的主播（也会保存配置文件）

```bash
python3 Controller.py add <用户名> <网站>
python3 Controller.py remove <用户名>
```

- 开始/停止录制主播

```bash
python3 Controller.py <start|stop> <用户名>
```

- 列出配置中的主播

```bash
python3 Controller.py status
```

**Web 界面：**

Web 界面可通过 5000 端口访问。如果在 `parameters.py` 中设置了密码，用户名为 `admin`，密码为 `admin`，也允许空密码访问。设置 `WEBSERVER_HOST` 后，可允许其他网络中的电脑访问。

**Docker 支持：**

你可以在 Docker 中运行此应用程序。我更偏向于使用 docker-compose，所以我提供了一个示例的 `docker-compose.yml` 文件，你可以直接使用。在目录中运行 `docker-compose up` 即可启动。

**配置：**

你可以在 `parameters.py` 中设置一些参数。

**免责声明：**

此程序仅为概念验证和学习项目，我不鼓励任何人使用它。

大多数（如果不是所有）主播不允许录制他们的节目。请尊重他们的意愿。

如果你忽视了他们的请求并进行录制，请不要发布或分享任何录制内容。

如果你录制或分享了录制的节目，你可能会面临法律处罚。

另外，请不要以任何形式将此工具用于盈利目的。