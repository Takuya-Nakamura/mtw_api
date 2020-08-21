from pprint import pprint as p
from mt_salesforce import MtSalesForce


def main():
    p("main")
    msf = MtSalesForce()
    p(msf.query("SELECT Id, Name FROM Organization"))

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


if __name__ == "__main__":
    main()
