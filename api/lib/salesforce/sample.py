from pprint import pprint as p
from mt_salesforce import MtSalesForce


def main():
    p("main")
    msf = MtSalesForce()
    p(msf.query("SELECT Id, Name FROM Organization"))


if __name__ == "__main__":
    main()



