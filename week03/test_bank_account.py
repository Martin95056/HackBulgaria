import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
	def setUp(self):
		self.bank_account = BankAccount("Rado", 0, "$")

	def test_bankaccount_init(self):
		self.assertEqual(self.bank_account._name, "Rado")
		self.assertEqual(self.bank_account._balance, 0)
		self.assertEqual(self.bank_account._currency, "$")

	def test_bankaccount_str(self):
		self.assertEqual(str(self.bank_account), "Bank account for Rado with balance of 0$")

	def test_bankaccount_int(self):
		self.assertEqual(int(self.bank_account), 0)

	def test_bankaccount_eq(self):
		other1 = BankAccount("Martin", 1000, "$")
		self.assertTrue(self.bank_account._currency == other1._currency)

		other2 = BankAccount("Martin", 1000, "lv")
		self.assertFalse(self.bank_account._currency == other2._currency)

	def test_bankaccount_deposit(self):
		self.bank_account.deposit(100)
		self.assertEqual(self.bank_account._balance, 100)

	def test_bankaccount_balance(self):
		self.assertEqual(self.bank_account.balance(), '0$')

	def test_bankaccount_withdraw(self):
		self.bank_account._balance = 100
		self.assertTrue(self.bank_account.withdraw(50))
		self.assertFalse(self.bank_account.withdraw(200))

	def test_bankaccount_transfer_to(self):
		other = BankAccount("Martin", 1000, "$")
		self.bank_account._balance = 100
		self.assertTrue(self.bank_account.transfer_to(other, 50))
		#self.bank_account.transfer_to(other, 50)
		self.assertEqual(other._balance, 1050)
		self.assertEqual(self.bank_account._balance, 50)


if __name__ == '__main__':
    unittest.main()