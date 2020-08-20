# import setting
from pprint import pprint as p
import os
import pickle  # object serialize
from simple_salesforce import Salesforce
from simple_salesforce.exceptions import *
import settings
import sys


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
            # セッション破棄
            p("[Log]TokenTimeout" + retry + 1)
            if(retry < 3):
                self.reload_client()
                return self.query(soql, retry + 1)
