from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
import hashlib
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    file_path = "/tmp/flag.txt"

    if not os.path.exists(file_path):
        return Response("FLAG NOT FOUND", status_code=404)

    with open(file_path, "r") as f:
        flag = f.read()

    cookies = request.cookies
    uid = cookies.get("UID")

    headers = {}

    if uid is None:
        uid_val = hashlib.md5("100".encode()).hexdigest()
        headers["set-cookie"] = f"UID={uid_val}; Max-Age=172800; Path=/"
    else:
        if uid == hashlib.md5("0".encode()).hexdigest():
            headers["set-cookie"] = f"FLAG={flag}; Path=/"
        else:
            headers["set-cookie"] = "FLAG=encryptCTF{y0u_c4nt_U53_m3}; Path=/"

    html = """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Hidden</title>
    </head>
    <body>
        <h2>Hey You, yes you!<br>are you looking for a flag, well it's not here bruh!<br>Try someplace else<h2>
    </body>
    </html>
    """
    return HTMLResponse(content=html, headers=headers)
