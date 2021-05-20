import unittest

def fib(n, memo = {}):
     if n in memo:
          return memo[n]
     elif n == 0:
          return 0
     elif n <= 2:
          return 1
     memo[n] = fib(n-1) + fib(n-2)
     return memo[n]


class TestFib(unittest.TestCase):
    def test_values(self):
        expected = { 0:0, 1:1, 2:1, 3:2, 4:3,
                     5:5, 6:8, 50:12586269025,
                     60: 1548008755920
                   }
        for key, exp_val in expected.items():
          got = fib(key)
          self.assertEqual(exp_val, got)    

if __name__ == "__main__"          :
    unittest.main(argv=['first-arg-is-ignored'], exit=False)