# import setting
from pprint import pprint as p
import os
import pickle  # object serialize
from simple_salesforce import Salesforce
from simple_salesforce.exceptions import *
import settings
import sys
import requests
import json

""" clientの中身
{'apex_url': 'https://cs6.salesforce.com/services/apexrest/',
 'api_usage': {},
 'auth_site': 'https://test.salesforce.com',
 'auth_type': 'password',
 'base_url': 'https://cs6.salesforce.com/services/data/v42.0/',
 'bulk_url': 'https://cs6.salesforce.com/services/async/42.0/',
 'domain': 'test',
 'headers': {'Authorization': 'Bearer '
                              '00DN0000000AQ1U!AQQAQMx.fQbWJyJfnoBEIxSb5r2sbkOXh6JdVb8hkBgsTbMHGzWIOKOJWEEEVVHFnRwPedad2WylAZZTxswqmkF.HZu5LYjH',
             'Content-Type': 'application/json',
             'X-PrettyPrint': '1'},
 'proxies': {},
 'session': <requests.sessions.Session object at 0x10d95bb50>,
 'session_id': '00DN0000000AQ1U!AQQAQMx.fQbWJyJfnoBEIxSb5r2sbkOXh6JdVb8hkBgsTbMHGzWIOKOJWEEEVVHFnRwPedad2WylAZZTxswqmkF.HZu5LYjH',
 'sf_instance': 'cs6.salesforce.com',
 'sf_version': '42.0'}

"""


class MtSalesForce():
    """simple_salesforce を使うためのクラス
    """

    def __init__(self):
        self.client_instance_file = './access_object'
        self.load_client()

    ############################################
    # authnticatoion
    ############################################

    def load_client(self):
        """set simple_salesforce instance
        """
        if os.path.exists(self.client_instance_file) == False:
            p("[Log]]autehntication from salesforce")
            self.authenticate()
            self.load_client()
        else:
            with open(self.client_instance_file, 'rb') as f:
                p("[Log]autehntication from file")
                self.client = pickle.load(f)

    def reload_client(self):
        os.remove(self.client_instance_file)
        self.load_client()

    def authenticate(self):
        sf = Salesforce(
            username=settings.SALESFORCE_USERNAME,
            password=settings.SALESFORCE_PASSWORD,
            security_token=settings.SALESFORCE_SECURITY_TOKEN,
            organizationId=settings.SALESFORCE_ORGANIZATION_ID,
            domain=settings.DOMAIN
        )
        # シリアライズ
        with open(self.client_instance_file, 'wb') as f:
            pickle.dump(sf, f)

    ############################################
    # action
    ############################################

    def query(self, soql, retry=0):
        try:
            return self.client.query(soql)
        except SalesforceExpiredSession as e:
            p("[Log]SalesforceExpiredSession")
            if(retry < 3):
                self.reload_client()
                return self.client.query(soql)
            else:
                # TODO: log出力と通知
                p("[Log]retry stop")
                p(e)
        except Exception as e:
            # TODO: log出力と通知
            p("[Log]query Exception")
            p(e)

    def apexecute(self, api_path, method, data, retry=0):
        try:
            return self.client.apexecute(api_path, method, data)
        except SalesforceExpiredSession as e:
            p("[Log]SalesforceExpiredSession")
            if(retry < 3):
                self.reload_client()
                return self.client.apexecute(api_path, method, data)
            else:
                # TODO: log出力と通知
                p("[Log]retry stop")
        except Exception as e:
            # TODO: log出力と通知
            p("[Log]query Exception")
            p(e)

    def raw_request(self, api_path):
        p("■■■■■■ raw_request")
        p(vars(self.client))






    """
    etry処理を１っ箇所にまとめたい....
    """

    """
    def query(self, soql, retry = 0):
        return self._request_with_retry(self.client.query, soql=soql)

    def apexecute(self, api_path, method, data, retry = 0):
        # return self.client.apexecute( api_path, method, data)
        return self._request_with_retry(self.client.apexecute, api_path=api_path, method=method, data=data)
        
    # 引数が異なると別のリクエストを使い分けられない..
    def _request_with_retry(self, func, *args, retry=0):
        try:
            return func(args)
        except SalesforceExpiredSession as e:
            p("[Log]SalesforceExpiredSession")
            if(retry < 3):
                self.reload_client()
                return func(args, retry + 1)
            else:
                # TODO: log出力と通知
                p("[Log]retry stop")
        except Exception as e:
            # TODO: log出力と通知
            p("[Log]query Exception")
    """
