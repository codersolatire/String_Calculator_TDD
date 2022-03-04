import unittest

def Add(numbers):
    num_split = numbers.split(",")
    if numbers == "":
        return "0"
    elif len(num_split) == 1:
        return numbers
    elif len(num_split) > 1:
        return str(int(num_split[0]) + int(num_split[1]))

class index(unittest.TestCase):
    def test_index_no_params(self):
        self.assertEqual(Add(""), "0")
        
    def test_index_one_param(self):
        self.assertEqual(Add("9"), "9")

    def test_index_tow_param(self):
        self.assertEqual(Add("9, 10"), "19")

if __name__ == '__main__':
    unittest.main()