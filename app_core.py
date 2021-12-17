# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('zItrizzPeBAbXnFAyjObZsTPIlYt8uV6KTlF8uFflST9vywXYbz/is0eNFSBGwLLZgmaJDF+MG7Zjf5NsSZPuXUVDznTR4SkH/dnQtiKMCtfxd6zwMFKZPlIEoNMjNodnZovofbnjCG01FEVfXM2uAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('87c075c80d2127a720f7fbfe3f7991cf')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()