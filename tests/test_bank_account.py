import unittest
from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(balance=1000)


    def test_deposit(self):
        #account = BankAccount(balance=1000)
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        #account = BankAccount(balance=1000)
        new_balance = self.account.withdraw(200)
        assert new_balance == 800
        self.assertEqual(new_balance, 800)

    def test_get_balance(self):
        #account = BankAccount(balance=1000)
        self.assertEqual(self.account.get_balance(), 1000)