import logging
from HumanMoveTest import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            runner = Runner('Bob', -5)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
        except ValueError as err:
            logging.warning('Неверная скорость для Runner')
            #raise ValueError(f'Скорость не может быть отрицательной, сейчас')

    def test_run(self):
        try:
            runner = Runner(123, 5)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')
            #raise TypeError(f'Имя должно быть строкой, передано {type(runner.name).__name__}')

    def test_challenge(self):
        runner_1 = Runner('Bob')
        runner_2 = Runner('Dave')
        for i in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        filename='runner_tests.log',
                        #encoding='utf-8',
                        format='%(asctime)s - %(levelname)s - %(message)s')

    unittest.main()
