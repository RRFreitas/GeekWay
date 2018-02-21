import unittest
from util.Validator import Validator

class Testes(unittest.TestCase):
    def email_valido(self):
        validator = Validator()
        self.assertTrue(validator.validEmail("rennan@gmail.com"), "E-mail inválido")
        self.assertTrue(validator.validEmail("@gmail.com"), "E-mail inválido")
        self.assertTrue(validator.validEmail("rennan@gmailcom"), "E-mail inválido")
        self.assertTrue(validator.validEmail("rennangmail.com"), "E-mail inválido")

    def data_valida(self):
        validator = Validator()
        self.assertTrue(validator.validDate("01/01/2000"), "Data inválida.")
        self.assertTrue(validator.validDate("01/012000"), "Data inválida.")
        self.assertTrue(validator.validDate("0101/2000"), "Data inválida.")
        self.assertTrue(validator.validDate("33/01/2000"), "Data inválida.")

testes = Testes()

testes.email_valido()
testes.data_valida()