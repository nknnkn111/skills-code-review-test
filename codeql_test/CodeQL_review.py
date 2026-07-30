"""
仅用于 CodeQL 安全扫描测试。

代码中故意包含漏洞，请勿运行或合并到生产代码。
"""

import subprocess

from flask import Flask, request


app = Flask(__name__)


@app.route("/read-file")
def read_file():
    """路径遍历测试。"""
    filename = request.args.get("filename")

    # 外部输入直接作为文件路径
    data = open(filename, "rb").read()

    return data


@app.route("/run-command")
def run_command():
    """命令注入测试。"""
    action = request.args.get("action", "")

    # 外部输入直接进入系统命令
    subprocess.call(["application", action])

    return "command executed"


@app.route("/calculate")
def calculate():
    """代码注入测试。"""
    expression = request.args.get("expression", "")

    # 外部输入直接进入 eval
    return str(eval(expression))