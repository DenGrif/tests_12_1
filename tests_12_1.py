import unittest
from runner import Runner

# class RunnerTest(unittest.TestCase):
#
#     def test_walk(self):
#         runner = Runner("Walker")
#         for _ in range(10):
#             runner.walk()
#         self.assertEqual(runner.distance, 50)
#
#     def test_run(self):
#         runner = Runner("Runner")
#         for _ in range(10):
#             runner.run()
#         self.assertEqual(runner.distance, 100)
#
#     def test_challenge(self):
#         # Пишем два объекта класса Runner
#         runner1 = Runner("Runner1")
#         runner2 = Runner("Runner2")
#         # Вызываем у первого run, а у второго walk 10 раз
#         for _ in range(10):
#             runner1.run()
#             runner2.walk()
#         # Проверяем на не равность (100 != 50)
#         self.assertNotEqual(runner1.distance, runner2.distance)
#
# if __name__ == '__main__':
#     unittest.main()
# ***********************************************************************
# Меняем ожидаемое значение в test_walk. Сейчас ожидается, что дистанция после 10 вызовов walk будет 50.
# Изменим это значение на 40, чтобы посмотреть, что тест не пройдёт.

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Walker")
        for _ in range(10):
            runner.walk()
        # Специально меняем на 40 (правильно 50)
        self.assertEqual(runner.distance, 40)

    def test_run(self):
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        # Вызываем у первого run, а у второго walk 10 раз
        for _ in range(10):
            runner1.run()
            runner2.walk()
        # Проверяем, что дистанции не равны (100 != 50)
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()
