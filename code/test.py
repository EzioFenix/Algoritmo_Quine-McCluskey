import unittest
import main
class Pruebas(unittest.TestCase):
    def test(self):
        miniterminos=[0, 2, 8, 10, 11, 20, 21, 22, 23, 26, 27, 28, 29, 30, 31]
        numVariables=5
        assert(len(main.programa(miniterminos, numVariables))==len(miniterminos))
        ass
        #print(main.programa(miniterminos, numVariables))
