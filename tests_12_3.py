import unittest
import inspect
from unittest import TestCase

from modele_3_5 import result
from runner_and_tournament import Runner, Tournament
TestCase = unittest.TestCase
class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        peshehod = Runner('Пешеход')
        for i in range(10):
            peshehod.walk()
        self.assertEqual(peshehod.distance, 50)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        begun = Runner('Бегун')
        for i in range(10):
            begun.run()
        self.assertEqual(begun.distance, 100)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        peshehod = Runner('Пешеход')
        begun = Runner('Бегун')
        for i in range(10):
            peshehod.walk()
            begun.run()
        self.assertNotEqual(peshehod.distance, begun.distance)

class TournamentTest(TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usan = Runner("Усэйн",10)
        self.andrey = Runner("Андрей",9)
        self.nik = Runner("Ник",3)

    @classmethod
    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            print()
            print(f'{test}:')
            print({k: str(v) for k, v in cls.all_results[test].items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usan_nik(self):
        tour = Tournament(90, self.usan, self.nik)
        result = tour.start()
        self.__class__.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_nik(self):
        tour = Tournament(90, self.andrey, self.nik)
        result = tour.start()
        self.__class__.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usan_andrey_nik(self):
        tour = Tournament(90, self.usan,self.andrey, self.nik)
        result = tour.start()
        self.__class__.all_results[inspect.stack()[0][3]] = result
        self.assertTrue('Ник' == result[len(result)].name)

if __name__ == '__main__':
    unittest.main()