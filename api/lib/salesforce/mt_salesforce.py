# import setting
from pprint import pprint as p
import os
import pickle  # object serialize
from simple_salesforce import Salesforce
import settings


class MtSalesForce():
    """simple_salesforce を使うためのクラス
    """

    def __init__(self):
        p("__init__")
        self.client_instance_file = './access_object'
        self.client_instance()


    ####  初期設定関連  ####

    def client_instance(self):
        """set simple_salesforce instance
        """
        p("instance")
        if os.path.exists(self.client_instance_file) == False:
            p("[log]re autehntication from salesforce")
            self.load_client_instance()
            self.client_instance()
        else:
            with open(self.client_instance_file, 'rb') as f:
                p("[log] autehntication from file")
                self.client = pickle.load(f)

    def load_client_instance(self):
        p("load_client_instance")
        sf = Salesforce(
            username=settings.SALESFORCE_USERNAME, 
            password=settings.SALESFORCE_PASSWORD,
            security_token=settings.SALESFORCE_SECURITY_TOKEN
        )
        # シリアライズ
        with open(self.client_instance_file, 'wb') as f:
            pickle.dump(sf, f)

    ####  リクエスト関連 ####

    def query(self, soql):
        p("query")
        return self.client.query(soql)
