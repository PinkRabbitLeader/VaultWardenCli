from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from utils import get_bw, run_commands, update_bw

bw = get_bw()
app = FastAPI()
templates = Jinja2Templates(directory="templates")
# 创建一个后台调度器
scheduler = BackgroundScheduler()
scheduler.start()


# 定义每日凌晨执行的任务函数
def daily_task():
    # 在这里执行您想要每日凌晨执行的任务
    update_bw()


# 使用 CronTrigger 触发器安排任务，每日凌晨执行
trigger = CronTrigger(hour=0, minute=0)
scheduler.add_job(daily_task, trigger)


@app.get("/")
async def root(request: Request):
    commands = f"{bw} --help"
    response = run_commands(commands)
    if "text/html" in request.headers.get("Accept", ""):
        response["request"] = request
        return templates.TemplateResponse(name="help.html", context=response)
    else:
        response["Message"] = {
            "official_documentation_zh": "关于 BW 使用的详细信息可查看官方文档（https://bitwarden.com/help/cli/）",
            "official_documentation_en":
                "How use of BW, please view the official documentation(https://bitwarden.com/help/cli/)",
        }
        return JSONResponse(content=response, status_code=response["Code"])
