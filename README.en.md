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

## Usage example

1. Get help information

    ```python
   import requests
    
   if (response := requests.get("http://127.0.0.1:8000")).status_code == 200:
      # TODO: Improve the operation after successfully obtaining help
      print(response.json())
   else:
     # TODO: Improve the operation after failure to obtain help
     print(response.json())
    ```

2. Execute tool-related commands, such as login
   
   > Note: If it is a self-hosted service, you need to set up the server before logging in.
   
   ```python
   import requests
    
   # For example: a user who logs in with an account whose email is test and whose password is test.
   if (response := requests.post("http://127.0.0.1:8000/bw/", json={"commands": "login test test"})).status_code == 200:
      # TODO: Improve the operation after successfully obtaining help
      print(response.json())
   else:
     # TODO: Improve the operation after failure to obtain help
     print(response.json())
    ```
   
3. For other interfaces, please view official documents(https://bitwarden.com/help/cli)