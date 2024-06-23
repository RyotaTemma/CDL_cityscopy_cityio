import json
from flask import *

app = Flask(__name__)

#盤面の状態（JSON情報）を保持しておく変数
cityIO_json = {}

#GAMA側からの要求に対してレスポンスする処理
@app.route('/', methods=['GET'])
def index():
    print("GET request received")   
    return Response(response=json.dumps({'response': cityIO_json}), status=200)

#CityScopy側から受け取る処理
@app.route('/', methods=['POST'])
def receive_message():
    global cityIO_json
    try:
        #盤面の状態を更新
        cityIO_json = request.get_json()  # POSTされたJSONを取得
        # print(cityIO_json)
        return Response(response=json.dumps({'response': 0}), status=200)
    except:
        return Response(response=json.dumps({'response': -1}), status=500)
    

if __name__ == "__main__":
    #ポート8888番で上の処理を実行（待ち受け状態）
    app.run(port=8888)


    # 340.0  0.0  0.0  0.0  340.0  680.0  0.0  680.0