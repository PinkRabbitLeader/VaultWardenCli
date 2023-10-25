from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from utils import get_bw, run_commands

bw = get_bw()
app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    commands = f"{bw} --help"
    response = run_commands(commands)
    if "text/html" in request.headers.get("Accept", ""):
        response["request"] = request
        return templates.TemplateResponse(name="help.html", context=response)
    else:
        response["Message"] = {
            "official_documentation_zh": "详细信息可查看官方文档（https://bitwarden.com/help/cli/）",
            "official_documentation_en":
                "Detailed information can be found in the official documentation(https://bitwarden.com/help/cli/)",
            "official_information": response["Message"]
        }
        return JSONResponse(content=response, status_code=response["Code"])