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
#         # ����� ��� ������� ������ Runner
#         runner1 = Runner("Runner1")
#         runner2 = Runner("Runner2")
#         # �������� � ������� run, � � ������� walk 10 ���
#         for _ in range(10):
#             runner1.run()
#             runner2.walk()
#         # ��������� �� �� �������� (100 != 50)
#         self.assertNotEqual(runner1.distance, runner2.distance)
#
# if __name__ == '__main__':
#     unittest.main()
# ***********************************************************************
# ������ ��������� �������� � test_walk. ������ ���������, ��� ��������� ����� 10 ������� walk ����� 50.
# ������� ��� �������� �� 40, ����� ����������, ��� ���� �� ������.

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Walker")
        for _ in range(10):
            runner.walk()
        # ���������� ������ �� 40 (��������� 50)
        self.assertEqual(runner.distance, 40)

    def test_run(self):
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        # �������� � ������� run, � � ������� walk 10 ���
        for _ in range(10):
            runner1.run()
            runner2.walk()
        # ���������, ��� ��������� �� ����� (100 != 50)
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()
