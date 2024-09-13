StreaMonitor 使用方法和支持站点：

**支持的网站：**

| 网站名称       | 缩写  | 可选分辨率 |
| -------------- | ----- | ---------- |
| Bongacams      | BC    | 是         |
| Cam4           | C4    | 是         |
| Cams.com       | CC    | 仅支持 360p |
| CamSoda        | CS    | 是         |
| Chaturbate     | CB    | 是         |
| Dreamcam VR    | DCVR  | 否         |
| Flirt4Free     | F4F   | 是         |
| MyFreeCams     | MFC   | 是         |
| SexChat.hu     | SCHU  | 否         |
| StreaMate      | SM    | 是         |
| StripChat      | SC    | 是         |
| StripChat VR   | SCVR  | 否         |
| XLoveCam       | XLC   | 否         |

**使用方法：**

启动下载器并自动导入配置文件中的所有主播：

```bash
python3 Downloader.py
```

控制台命令：

- `add <用户名> <网站>` - 添加并开始监控主播
- `remove <用户名> [<网站>]` - 删除主播
- `start <用户名> [<网站>]` - 开始监控指定主播
- `start *` - 开始监控所有主播
- `stop <用户名> [<网站>]` - 停止监控指定主播
- `stop *` - 停止监控所有主播
- `status` - 显示状态
- `status2` - 显示更可读的状态表格
- `quit` - 退出