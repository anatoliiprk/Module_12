import unittest

print('Задача "Проверка на выносливость"')

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        first = Runner('first runner')
        i = 10
        while i:
            first.walk()
            i -= 1
        self.assertEqual(first.distance, 50)

    def test_run(self):
        second = Runner('second runner')
        i = 10
        while i:
            second.run()
            i -= 1
        self.assertEqual(second.distance, 100)

    def test_challenge(self):
        third = Runner('third runner')
        fourth = Runner('fourth runner')
        i = 10
        while i:
            third.run()
            fourth.walk()
            i -= 1
        self.assertNotEqual(third.distance, fourth.distance)

if __name__ == '__main__':
    unittest.main()