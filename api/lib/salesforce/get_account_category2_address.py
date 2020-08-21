from pprint import pprint as p
from mt_salesforce import MtSalesForce
import sys
import pandas as pd
from util import * 

def main():
    """ 主たる勤務先の情報を取得する? (excel10行目)
        
    """

    # dummy_id :001N000001HsLSUIA3
    args = sys.argv
    check_args(args, 1)

    account_category2_address = args[1]
    msf = MtSalesForce()

    soql =  "SELECT Id,Name,MstCategory__c,Other__c,IsPrimary__c FROM AccountCategory__c" \ 
            "WHERE AccountCategory2Address__c='%s' AND IsPrimary__c = true" %(account_category2_address)
        
    response = msf.query(soql)

    account_id = response['records'][0]['AccountAddresses__r']['records'][0]['Id']
    p(account_id)
    return account_id




if __name__ == "__main__":
    main()
