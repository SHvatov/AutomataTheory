from automates import Automate
from automaton_equivalence import equivalent


def lambda_func(s, a):
    if a == "a" and s == "1":
        return 0
    elif a == "b" and s == "1":
        return 1
    elif a == "b" and s == "2":
        return 0
    elif a == "a" and s == "2":
        return 1


def sigma_func(s, a):
    if a == "a" and s == "1":
        return "1"
    elif a == "b" and s == "1":
        return "2"
    elif a == "b" and s == "2":
        return "2"
    elif a == "a" and s == "2":
        return "1"


if __name__ == "__main__":
    A = {"a", "b"}
    S = {"1", "2"}
    a = Automate(A, S, lambda_func, sigma_func, "1")
    b = Automate(A, S, lambda_func, sigma_func, "2")
    print(equivalent(a, b))