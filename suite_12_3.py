import unittest
import tests_12_3
TestSuite = unittest.TestSuite()
TestSuite.addTest(unittest.TestLoader() \
                  .loadTestsFromTestCase(tests_12_3.RunnerTest))
TestSuite.addTest(unittest.TestLoader() \
                  .loadTestsFromTestCase(tests_12_3.TournamentTest))
TeTeRu = unittest.TextTestRunner(verbosity=2)
TeTeRu.run(TestSuite)