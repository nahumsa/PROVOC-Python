import unittest

## Fibonati looping

def fib(n):
    if n == 0:
        return 0
    res =  0
    temp = 1
    for _ in range(n):
        res += temp
        temp = res - temp
    return res

## Fibonati recursivo sem memorização

def fib2(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)

## Fibonacci rescursivo com memorização

def fib3( n, dict = {}):

    if n == 0:
        return 0
    if n <= 2:
        return 1
    elif n in dict.keys():
        return dict[n]
    else:
        dict[n] = fib3(n-1) + fib3(n-2)
        return fib3(n)

class TestFib(unittest.TestCase):
    def test_values(self):
        expected = { 0:0, 1:1, 2:1, 3:2, 4:3,
                     5:5, 6:8, 50:12586269025,
                     60: 1548008755920
                   }
        for key, exp_val in expected.items():
          got = fib3(key)
          self.assertEqual(exp_val, got)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
