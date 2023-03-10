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
        self.assertEqual("AB+C*D/", postfix("(A+B)*C/D"))
        self.assertEqual("AB+C*D/EF^+G/", postfix("((A+B)*C/D+E^F)/G"))
        self.assertEqual("ABCD+EF+*G/+*H*", postfix("A*(B+(C+D)*(E+F)/G)*H"))
        self.assertEqual("AB+S/E*", postfix("(A+B)/S*E"))
        self.assertEqual("KL+MN*-OP^W*U/V/T*+QJA^^+",
                         postfix("K+L-M*N+(O^P)*W/U/V*T+Q^J^A"))
        self.assertEqual("ABC^^", postfix("A^B^C"))
        self.assertEqual("XABC^^+", postfix("X+A^B^C"))

    def test_Postfix_to_Infix(self):
        self.assertEqual("((A+B)*C)/D", infix("AB+C*D/"))
        self.assertEqual("((((A+B)*C)/D)+(E^F))/G", infix("AB+C*D/EF^+G/"))
        self.assertEqual("(A*(B+(((C+D)*(E+F))/G)))*H",
                         infix("ABCD+EF+*G/+*H*"))
