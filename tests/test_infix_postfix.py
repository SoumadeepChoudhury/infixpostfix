from infix_postfix.infix_postfix import infix, postfix

import unittest
import time


class TestInfixPostFix(unittest.TestCase):
    def setUp(self) -> None:
        self.startTime: int = time.time()

    def tearDown(self) -> None:
        self.endTime: int = time.time()
        print(
            f"Average Time taken to execute {str(self.id()).split('.')[-1]}: ", self.endTime-self.startTime)

    def test_Infix_to_Postfix(self):
        self.assertEqual("A B + C * D /", postfix("( A+B)* C/D"))
        self.assertEqual("A B + C * D / E F ^ + G /",
                         postfix("((A+B)*C/D+E^F)/G"))
        self.assertEqual("A B C D + E F + * G / + * H *",
                         postfix("A*(B+(C+D)*(E+F)/G)*H"))
        self.assertEqual("A B + S / E *", postfix("(A+B)/S*E"))
        self.assertEqual("K L + M N * - O P ^ W * U / V / T * + Q J A ^ ^ +",
                         postfix("K+L-M*N+(O^P)*W/U/V*T+Q^J^A"))
        self.assertEqual("A B C ^ ^", postfix("A^B^C"))
        self.assertEqual("X A B C ^ ^ +", postfix("X+A^B^C"))

    def test_Postfix_to_Infix(self):
        self.assertEqual("((A+B)*C)/D", infix("A B + C * D /"))
        self.assertEqual("((((A+B)*C)/D)+(E^F))/G",
                         infix("A B + C * D / E F ^ + G /"))
        self.assertEqual("(A*(B+(((C+D)*(E+F))/G)))*H",
                         infix("A B C D + E F + * G / + * H *"))
        self.assertEqual("20.1+5", infix("20.1 5 +"))
