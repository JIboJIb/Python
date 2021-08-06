# Pick your solution to one of the exercises in this module. Design tests for this solution and write tests using
# unittest library.
import unittest
import Func_first_class.Task2


class TestUpper(unittest.TestCase):
    def test_shout(self):
        text1 = "Text for checking the task"
        self.assertEqual(Func_first_class.Task2.shout(text1), "TEXT FOR CHECKING THE TASK")

    def test_whisper(self):
        text2 = "Text for checking the task"
        self.assertEqual(Func_first_class.Task2.whisper(text2), "text for checking the task")


unittest.main()
