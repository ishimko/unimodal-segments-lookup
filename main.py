from math import *
from unimodal_segments_lookup import get_unimodal_segments
import numpy as np
import matplotlib.pyplot as plt

SAFE_LIST = ['math', 'acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
             'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 'modf', 'pi',
             'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']
POINTS_COUNT = 1000

def get_function_object_for_plotting(user_function, args):
    for name in SAFE_LIST:
        user_function = user_function.replace(name, 'np.' + name)
    return eval(user_function, {'np': np}, {'x': args})


def get_function_object(user_function):
    def f(x):
        math_functions = dict([(k, globals().get(k, None)) for k in SAFE_LIST])
        return eval(user_function, math_functions, {'x': x})

    return f


def draw_plot(user_function, unimodal_segments, interval_start, interval_end):
    points = np.linspace(interval_start, interval_end, POINTS_COUNT)

    f = get_function_object_for_plotting(user_function, points)
    plt.plot(points, f)

    unimodal_segment_boundaries = [segment_item for segment in unimodal_segments for segment_item in segment]
    for unimodal_segment_boundary in unimodal_segment_boundaries:
        plt.axvline(unimodal_segment_boundary, color='r', linestyle='dashed')
    plt.show()


def print_result(unimodal_segments):
    print('Интервалы унимодальности:')
    for segment in unimodal_segments:
        print('[{}, {}]'.format(segment[0], segment[1]))


def main():
    function = input('Функция: ')
    d = float(input('d: '))
    print('[a, b]')
    interval_start = float(input('a: '))
    interval_end = float(input('b: '))

    unimodal_segments = get_unimodal_segments(get_function_object(function), interval_start, interval_end, d)

    print_result(unimodal_segments)
    draw_plot(function, unimodal_segments, interval_start, interval_end)

if __name__ == '__main__':
    main()
