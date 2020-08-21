from pprint import pprint as p
from mt_salesforce import MtSalesForce
import sys
from util import * 


def main():
    """ AccountIDを指定して、該当ユーザーの主たる勤務先のIDを取得する
    """

    # https://cs6.salesforce.com/services/apexrest/account/with_relations/?id=001N000001HsLSUIA3
    args = sys.argv
    check_args(args, 1)

    account_id = args[1]
    msf = MtSalesForce()

    api_path = 'account/with_relations?id=%s' %(account_id)
    payload = {}
    response = msf.apexecute(api_path, method='GET', data=payload)
    p(response)
    return response


    


if __name__ == "__main__":
    main()



