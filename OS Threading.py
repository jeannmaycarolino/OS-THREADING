# Operating System
# Single and Multi Threading
# CAROLINO | GARCIA | MONTER
import time
import threading
import os
import random
# Import necessary libraries and modules.


class Fibonacci:
    def calculate(self, n):
        if n < 2:
            return n
        else:
            return self.calculate(n - 1) + self.calculate(n - 2)
# The Fibonacci class provides a method to calculate the Fibonacci sequence.

class Square:
    def calculate(self, n):
        if n < 1:
            return n
        else:
            return n * n
# The Square class provides a method to calculate the square of a number.


class SortNumbers:
    def sort(self, numbers):
        return sorted(numbers)
# The SortNumbers class provides a method to sort a list of numbers.


class SingleThreaded:  # Function for single threading
    def __init__(self, fib, sqr, sort):
        self.fib = fib
        self.sqr = sqr
        self.sort = sort

    def run(self):
        print("\nStarting single-threading system...")
        while running:
            n = random.randint(0, 20)

            try:
                fib_num = [self.fib.calculate(i) for i in range(n + 1)]
                print("Single-Threaded- Thread Number:", threading.get_ident())
                print("Single-Threaded- Given:", n)
                print("Single-Threaded- Fibonacci number is:", fib_num, "\n")
            except ValueError as e:
                print("\nERROR:", e)
            try:
                sqr_num = self.sqr.calculate(n)
                print("Single-Threaded- Thread Number:", threading.get_ident())
                print("Single-Threaded- Given:", n)
                print("Single-Threaded- Squared number is: [", sqr_num, "]\n")
            except ValueError as e:
                print("\nERROR:", e)

            sort_num = [random.randint(0, 100) for _ in range(5)]
            try:
                sorted_num = self.sort.sort(sort_num)
                print("Single-Threaded- Thread Number:", threading.get_ident())
                print("Single-Threaded- Unsorted numbers:", sort_num)
                print("Single-Threaded- Sorted numbers:", sorted_num, "\n")
            except ValueError as e:
                print("\nERROR:", e)

            time.sleep(1)


class MultiThreaded: # Function for Multi threading
    def __init__(self, fib, sqr, sort): # initializing
        self.fib = fib
        self.sqr = sqr
        self.sort = sort

    def run(self):
        print("\nStarting multi-threading system...")
        while running:
            threads = []
            for _ in range(5):
                sort_num = [random.randint(0, 100) for _ in range(5)]
                n = random.randint(0, 20)

                t1 = threading.Thread(target=self.print_fib, args=(n,))
                t2 = threading.Thread(target=self.print_sqr, args=(n,))
                t3 = threading.Thread(target=self.print_sort, args=(sort_num,))

                threads.extend([t1, t2, t3])

                t1.start()
                t2.start()
                t3.start()

                print("Thread [", t1.name, "] has pID of:", os.getpid())
                print("Thread [", t2.name, "] has pID of:", os.getpid())
                print("Thread [", t3.name, "] has pID of:", os.getpid())

            for t in threads:
                t.join()

            time.sleep(5)

    def print_fib(self, n):
        try:
            fib_num = [self.fib.calculate(i) for i in range(n + 1)]
            print("Multi-threaded- Thread Number:", threading.get_ident())
            print("Multi-threaded- Given:", n)
            print("Multi-threaded- Fibonacci number is:", fib_num, "\n")
        except ValueError as e:
            print("\nERROR:", e)

    def print_sqr(self, n):
        try:
            sqr_num = self.sqr.calculate(n)
            print("Multi-threaded- Thread Number:", threading.get_ident())
            print("Multi-threaded- Given:", n)
            print("Multi-threaded- Squared number is: [", sqr_num, "]\n")
        except ValueError as e:
            print("ERROR:", e)

    def print_sort(self, sort_num):
        try:
            sorted_num = self.sort.sort(sort_num)
            print("Multi-threaded- Thread Number:", threading.get_ident())
            print("Multi-threaded- Unsorted numbers:", sort_num)
            print("Multi-threaded- Sorted numbers:", sorted_num, "\n")
        except ValueError as e:
            print("\nERROR:", e)


running = True
fibonacci = Fibonacci()
square = Square()
sort_numbers = SortNumbers()
# Create instances of the Fibonacci, Square, and SortNumbers classes.

single_threaded = SingleThreaded(fibonacci, square, sort_numbers)
multi_threaded = MultiThreaded(fibonacci, square, sort_numbers)
# Single and Multi Threaded classes, passing the instances of Fibonacci, Square, and SortNumbers.

single_threaded_thread = threading.Thread(target=single_threaded.run)
single_threaded_thread.start()
print("Single-threaded system pID:", os.getpid())

multi_threaded_thread = threading.Thread(target=multi_threaded.run)
multi_threaded_thread.start()
print("Multi-threaded system pID:", os.getpid())
# start separate threads for the single and multi-threaded, and print their process IDs.

input("\nTerminating the program...\n")
running = False
# terminate the program.

single_threaded_thread.join()
multi_threaded_thread.join()

