# Password management platform ([VaultWarden](https://github.com/dani-garcia/vaultwarden)) terminal management tool ([BW](https://bitwarden.com/help/cli))

**<p align="right">Other language versions: [Chinese](README.md)</p>**

---

## Introduction

- Since the open source password management platform ([VaultWarden](https://github.com/dani-garcia/vaultwarden)) does not have a corresponding API interface, it only has a terminal management tool, namely [BW](https://bitwarden.com/help/cli), so here we use the [BW](https://bitwarden.com/help/cli) tool combined with the FastAPI framework to implement a terminal management tool that can be requested through the network. Here, we only need to access the application and run it to generate The IP address and port can be used to access the service. See the details below.

## Install related dependencies

```shell
pip install -r requirements.txt
```

## Start application

```shell
python -m uvicorn main:app --host host address --port port
```