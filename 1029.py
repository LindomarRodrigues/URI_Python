# -*- coding: utf-8 -*-

vetor = [
    'fib(1) = 0 calls = 1', 'fib(2) = 2 calls = 1', 'fib(3) = 4 calls = 2',
    'fib(4) = 8 calls = 3', 'fib(5) = 14 calls = 5', 'fib(6) = 24 calls = 8',
    'fib(7) = 40 calls = 13', 'fib(8) = 66 calls = 21',
    'fib(9) = 108 calls = 34', 'fib(10) = 176 calls = 55',
    'fib(11) = 286 calls = 89', 'fib(12) = 464 calls = 144',
    'fib(13) = 752 calls = 233', 'fib(14) = 1218 calls = 377',
    'fib(15) = 1972 calls = 610', 'fib(16) = 3192 calls = 987',
    'fib(17) = 5166 calls = 1597', 'fib(18) = 8360 calls = 2584',
    'fib(19) = 13528 calls = 4181', 'fib(20) = 21890 calls = 6765',
    'fib(21) = 35420 calls = 10946', 'fib(22) = 57312 calls = 17711',
    'fib(23) = 92734 calls = 28657', 'fib(24) = 150048 calls = 46368',
    'fib(25) = 242784 calls = 75025', 'fib(26) = 392834 calls = 121393',
    'fib(27) = 635620 calls = 196418', 'fib(28) = 1028456 calls = 317811',
    'fib(29) = 1664078 calls = 514229', 'fib(30) = 2692536 calls = 832040',
    'fib(31) = 4356616 calls = 1346269', 'fib(32) = 7049154 calls = 2178309',
    'fib(33) = 11405772 calls = 3524578', 'fib(34) = 18454928 calls = 5702887',
    'fib(35) = 29860702 calls = 9227465',
    'fib(36) = 48315632 calls = 14930352',
    'fib(37) = 78176336 calls = 24157817',
    'fib(38) = 126491970 calls = 39088169',
    'fib(39) = 204668308 calls = 63245986'
]

n = int(input())

for a in range(n):
    i = int(input())
    print(vetor[i - 1])
