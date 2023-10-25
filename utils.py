__all__ = ["response_temp", "run_commands", "get_os", "get_bw"]

import os
import platform
import subprocess
import zipfile

import requests


class UnsupportedOSError(Exception):
    pass


class DownloadError(Exception):
    pass


# 响应信息模板
def response_temp(code: int = 200, message: str or dict = None, payload: any = None, **kwargs):
    return {"Code": code, "Message": message, "Payload": payload, **kwargs}


def download_bw_tool(bw_path: str, bw_name: str):
    _bw = os.path.join(bw_path, bw_name)
    system = bw_name.split('_')[1].replace('.exe', '')
    url = f"https://vault.bitwarden.com/download/?app=cli&platform={system}"
    response = requests.get(url)
    if response.status_code == 200:
        # 获取文件名
        content_disposition = response.headers.get('Content-Disposition')
        if content_disposition:
            file_name = content_disposition.split('filename=')[1]
        else:
            file_name = os.path.basename(url)

        # 拼接ZIP文件路径并保存ZIP文件
        zip_file_path = os.path.join(bw_path, file_name)

        with open(zip_file_path, 'wb') as file:
            file.write(response.content)

        # 解压ZIP文件
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            for member in zip_ref.namelist():
                if "bw" in member:
                    with zip_ref.open(member) as source, open(_bw, 'wb') as target:
                        target.write(source.read())
                    break

        # 删除ZIP文件
        os.remove(zip_file_path)
        return _bw
    else:
        raise DownloadError(f'BW 工具下载失败, 原错误：{response.content.decode("utf-8")}')


def run_commands(commands: str):
    process = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                               universal_newlines=True)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        return response_temp(code=400, message=stderr)
    else:
        return response_temp(message=stdout)


def get_os():
    # 获取操作系统名称
    os_name = _os_name.lower() if (_os_name := platform.system()) != "Darwin" else "macos"
    if os_name != "windows" and os_name != "linux" and os_name != "macos":
        raise UnsupportedOSError(f"不支持的操作系统: {os_name}")
    else:
        return os_name


def get_bw():
    os_name = get_os()
    # 获取 BW 工具
    return _bw_whole_path if os.path.exists(
        _bw_whole_path := os.path.join(
            (_bw_path := os.path.dirname(os.path.abspath(__file__))),
            (_bw_name := (f"bw_windows.exe" if os_name == "windows" else f"bw_{os_name}"))
        )
    ) else download_bw_tool(bw_name=_bw_name, bw_path=_bw_path)