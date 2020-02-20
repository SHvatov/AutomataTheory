from automates import Automate
from automaton_equivalence import equivalent


def test_lambda_function_1_first(state, value):
    if state == '1' and value == 'a':
        return '0'
    elif state == '1' and value == 'b':
        return '1'
    elif state == '2' and value == 'a':
        return '1'
    elif state == '2' and value == 'b':
        return '0'


def test_sigma_function_1_first(state, value):
    if state == '1' and value == 'a':
        return '1'
    elif state == '1' and value == 'b':
        return '2'
    elif state == '2' and value == 'a':
        return '1'
    elif state == '2' and value == 'b':
        return '2'


def test_lambda_function_1_second(state, value):
    if state == 'p' and value == 'a':
        return '0'
    elif state == 'p' and value == 'b':
        return '1'
    elif state == 'q' and value == 'a':
        return '0'
    elif state == 'q' and value == 'b':
        return '1'
    elif state == 'r' and value == 'a':
        return '1'
    elif state == 'r' and value == 'b':
        return '0'


def test_sigma_function_1_second(state, value):
    if state == 'p' and value == 'a':
        return 'q'
    elif state == 'p' and value == 'b':
        return 'r'
    elif state == 'q' and value == 'a':
        return 'p'
    elif state == 'q' and value == 'b':
        return 'r'
    elif state == 'r' and value == 'a':
        return 'q'
    elif state == 'r' and value == 'b':
        return 'r'


def test_equivalent_automates():
    a_first = {'1', '2'}
    a_second = {'p', 'q', 'r'}
    alphabet = {'a', 'b'}

    first = Automate(in_alphabet=alphabet,
                     states=a_first,
                     transition_func=test_sigma_function_1_first,
                     out_func=test_lambda_function_1_first,
                     initial_state='1')
    second = Automate(in_alphabet=alphabet,
                      states=a_second,
                      transition_func=test_sigma_function_1_second,
                      out_func=test_lambda_function_1_second,
                      initial_state='p')

    assert equivalent(first, second) is True


def test_lambda_function_2_first(state, value):
    if state == 'p' and value == 'a':
        return '0'
    elif state == 'p' and value == 'b':
        return '1'
    elif state == 'q' and value == 'a':
        return '0'
    elif state == 'q' and value == 'b':
        return '1'
    elif state == 'r' and value == 'a':
        return '1'
    elif state == 'r' and value == 'b':
        return '0'


def test_sigma_function_2_first(state, value):
    if state == 'p' and value == 'a':
        return 'q'
    elif state == 'p' and value == 'b':
        return 'r'
    elif state == 'q' and value == 'a':
        return 'p'
    elif state == 'q' and value == 'b':
        return 'r'
    elif state == 'r' and value == 'a':
        return 'q'
    elif state == 'r' and value == 'b':
        return 'r'


def test_lambda_function_2_second(state, value):
    if state == 'p' and value == 'a':
        return '0'
    elif state == 'p' and value == 'b':
        return '1'
    elif state == 'q' and value == 'a':
        return '1'
    elif state == 'q' and value == 'b':
        return '0'
    elif state == 'r' and value == 'a':
        return '0'
    elif state == 'r' and value == 'b':
        return '1'
    elif state == 's' and value == 'a':
        return '0'
    elif state == 's' and value == 'b':
        return '1'


def test_sigma_function_2_second(state, value):
    if state == 'p' and value == 'a':
        return 'p'
    elif state == 'p' and value == 'b':
        return 's'
    elif state == 'q' and value == 'a':
        return 'p'
    elif state == 'q' and value == 'b':
        return 'r'
    elif state == 'r' and value == 'a':
        return 'q'
    elif state == 'r' and value == 'b':
        return 'r'
    elif state == 's' and value == 'a':
        return 'q'
    elif state == 's' and value == 'b':
        return 'r'


def test_not_equivalent_automates():
    a_first = {'p', 'q', 'r'}
    a_second = {'p', 'q', 'r', 's'}
    alphabet = {'a', 'b'}

    first = Automate(in_alphabet=alphabet,
                     states=a_first,
                     transition_func=test_sigma_function_2_first,
                     out_func=test_lambda_function_2_first,
                     initial_state='p')
    second = Automate(in_alphabet=alphabet,
                      states=a_second,
                      transition_func=test_sigma_function_2_second,
                      out_func=test_lambda_function_2_second,
                      initial_state='p')

    assert equivalent(first, second) is not True


if __name__ == '__main__':
    test_equivalent_automates()
    test_not_equivalent_automates()
