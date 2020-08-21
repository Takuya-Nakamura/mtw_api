from pprint import pprint as p
from mt_salesforce import MtSalesForce
import sys
import pandas as pd
from util import * 

def main():
    """ SalesforceのLightning Platform REST API にリクエスト
        Excel ５行目
    """

    # https://cs6.salesforce.com/services/data/v28.0/sobjects/Account/001N000001HsLSUIA3?_HttpMethod=PATCH
    args = sys.argv
    check_args(args, 2)

    # init
    account_id = args[1]
    session_id = args[1]
    msf = MtSalesForce()

    # main
    api_path = 'sobjects/Account/%s?_HttpMethod=PATCH' % (account_id)
    data = {'SessionId__c': session_id}
    response = msf.http_request(api_path, 'POST', data)
    return response


if __name__ == "__main__":
    main()
