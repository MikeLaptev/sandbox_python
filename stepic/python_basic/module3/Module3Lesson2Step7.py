# coding=utf-8
__author__ = "mlaptev"


def f(x):
    return "Fake"


if __name__ == "__main__":
    amount_of_tests = int(eval(input()))
    cached_results = dict()
    for test_id in range(amount_of_tests):
        parameter = int(eval(input()))
        if parameter not in cached_results:
            cached_results[parameter] = f(parameter)
        print((cached_results[parameter]))
