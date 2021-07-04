from unittest import mock
from unittest import TestCase, main
from _9_charlottepeart_functiontotest import is_correct_pin, is_enough_money, transaction_complete

class TestIsCorrectPinFunction(TestCase):

    def test_correct_pin(self):
        expected = 'True'
        result = is_correct_pin(pin=1111, pin_target=1111)
        self.assertEqual(expected, result)

    def test_incorrect_pin(self):
        expected = 'False'
        result = is_correct_pin(pin=1234, pin_target=1111)
        self.assertEqual(expected, result)

class TestIsEnoughMoney(TestCase):

    def test_enough_money(self):
        expected = 'True'
        result = is_enough_money(wthdraw_amnt=98, acc_bal=100)
        self.assertEqual(expected, result)

    def test_not_enough_money(self):
        expected = 'False'
        result = is_enough_money(wthdraw_amnt=101, acc_bal = 100)
        self.assertEqual(expected, result)

class TestTransactionComplete(TestCase):

    def test_successful_transaction(self):
        expected = 'True'
        result = transaction_complete()
        self.assertEqual(expected, result)

    def test_unsuccessful_transaction(self):
        expected = 'False'
        result = transaction_complete()
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()