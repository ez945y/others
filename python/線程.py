from threading import Thread, Lock
from time import sleep

class Account(object):
    def __init__(self):
        self._balance=0
        self._lock=Lock()
    
    def deposit(self, money):
        self._lock.acquire()
        try:
            newBalance=self._balance+money
            sleep(0.01)
            self._balance=newBalance
        finally:
            self._lock.release()
    
    @property
    def getbalance(self):
        return self._balance

class withdraw(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account=account
        self._money=money

    def run(self):
        self._account.deposit(self._money)
def main():
    account = Account()
    threads =[]
    for i in range(100):
        t=withdraw(account,1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("帳戶餘額%d元" % account.getbalance)
    print("版本二")


if __name__ == "__main__":
    main()





