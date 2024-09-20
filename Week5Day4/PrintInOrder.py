# Suppose we have a class:

# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }
# The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

# Note:

# We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

# Problem Link: https://leetcode.com/problems/print-in-order/description/

from typing import Callable
from threading import Event

class Foo:
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done.set()  # Signal that 'first' is done

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_done.wait()  # Wait for 'first' to complete
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_done.set()  # Signal that 'second' is done

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_done.wait()  # Wait for 'second' to complete
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
