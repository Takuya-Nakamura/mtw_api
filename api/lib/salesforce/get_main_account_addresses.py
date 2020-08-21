from pprint import pprint as p
from mt_salesforce import MtSalesForce
import sys
import pandas as pd
from util import * 

def main():
    """ AccountIDを指定して、該当ユーザーの主たる勤務先のIDを取得する
    """

    # dummy_id :001N000001HsLSUIA3
    args = sys.argv
    check_args(args, 1)

    account_id = args[1]
    msf = MtSalesForce()

    soql =  \
        "SELECT (SELECT Id, AddressClass__c FROM " \
        "AccountAddresses__r WHERE AddressClass__c = '主たる勤務先') " \
        "FROM Account WHERE Id = '%s'" % (account_id)

    response = msf.query(soql)

    account_id = response['records'][0]['AccountAddresses__r']['records'][0]['Id']
    p(account_id)
    return account_id




if __name__ == "__main__":
    main()
