import json
from pprint import pprint 

from simple_salesforce import Salesforce

USERNAME = 'nakamura0803+dev@gmail.com'
PASSWORD = 'nakamura0803'
SECURITY_TOKEN = 'sNKTbBBJy6rHqm9Cc7zuXRz8'

## メモ
### sfの認証をしてクライアントを返す処理を持つベースのclassを作成して
## 独自のapi vieww classのコンストラクタでsfインスタンスを持つようにする。
### 最初は各viewのaction内でそのインスタンスを使ってsfへのリクエストを発行する
### （発行データの戻りの整形はsfクラスに持たせたい）
### これでpyファイルがあまりに長くなるようだったら、sfを継承したサブクラスをviewと同じカテゴリで作成して
### pyの中で重くなったリクエスト周りの処理を寄せていくイメージ


def main():
    # sf = Salesforce(username=USERNAME, password=PASSWORD,
    #                 security_token=SECURITY_TOKEN, sandbox=False)
    sf = Salesforce(username=USERNAME, password=PASSWORD,
                    security_token=SECURITY_TOKEN)
    # ユーザー一覧取得                    
    res = sf.query(
        'SELECT Id, Name, LastLoginDate FROM User')
    
    pprint(res)
    # print(json.dumps(res, indent=4))


if __name__ == '__main__':
    main()