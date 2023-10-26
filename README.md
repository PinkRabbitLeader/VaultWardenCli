# 密码管理平台（[VaultWarden](https://github.com/dani-garcia/vaultwarden)）终端管理工具（[BW](https://bitwarden.com/help/cli)）

**<p align="right">其他语言版本: [English](README.en.md)</p>**

---

## 简介

- 由于开源密码管理平台（[VaultWarden](https://github.com/dani-garcia/vaultwarden)）并没有相应的 API 接口，只有终端管理工具，即 [BW](https://bitwarden.com/help/cli)，因此在此借助 [BW](https://bitwarden.com/help/cli) 工具结合 FastAPI 框架实现一个可以通过网络请求的终端管理工具，在此只要通过访问应用运行后生成的 IP 地址与端口即可访问服务，具体详细见下方。

## 安装相关依赖

```shell
pip install -r requirements.txt
```

## 启动应用

```shell
python -m uvicorn main:app --host 主机地址 --port 端口
```
