from pprint import pprint as p
from mt_salesforce import MtSalesForce
import sys
import pandas as pd


def main():
    """ AccountIDを指定して、該当ユーザーの主たる勤務先のIDを取得する
    """

    # https://cs6.salesforce.com/services/apexrest/account/with_relations/?id=001N000001HsLSUIA3

    check_args()

    args = sys.argv    
    account_id = args[1]
    msf = MtSalesForce()

    api_path = 'account/with_relations?id=%s' %(account_id)
    payload = {}
    response = msf.apexecute(api_path, method='GET', data=payload)
    p(response)
    return response


def check_args():
    if len(sys.argv) <= 1  :
        p("invalid arguments") 
        sys.exit(0)
    


if __name__ == "__main__":
    main()



