EPS = 0.0001
EXTREMUM_DELTA_COEFFICIENT = 1/3

def is_increasing_at_point(function, point, epsilon=EPS):
    return (function(point) - function(point + epsilon)) < 0


def is_decreasing_at_point(function, point, epsilon=EPS):
    return (function(point) - function(point + epsilon)) > 0


def get_first_point_where(target_function, current_point, condition_function, delta, interval_end):
    i = 1
    while (not condition_function(target_function, current_point)) and (current_point <= interval_end):
        current_point += i * delta
        i += 1
    return current_point <= interval_end, current_point


def get_unimodal_segments(target_function, interval_begin, interval_end, min_extremum_delta):
    result = []
    delta = min_extremum_delta * EXTREMUM_DELTA_COEFFICIENT

    get_first_decreasing_point = lambda x: get_first_point_where(target_function, x, is_decreasing_at_point, delta,
                                                                 interval_end)
    get_first_increasing_point = lambda x: get_first_point_where(target_function, x, is_increasing_at_point, delta,
                                                                 interval_end)

    current_interval_end = interval_begin
    is_in_interval = True
    if is_decreasing_at_point(target_function, interval_begin):
        is_in_interval, current_interval_end = get_first_increasing_point(interval_begin)
        if is_in_interval:
            result.append((interval_begin, current_interval_end))

    end_iteration = not is_in_interval
    while not end_iteration:
        is_in_interval, current_interval_begin = get_first_decreasing_point(current_interval_end)
        if is_in_interval:
            is_in_interval, current_interval_end = get_first_increasing_point(current_interval_begin)
            if is_in_interval:
                result.append((current_interval_begin, current_interval_end))
            else:
                end_iteration = True
        else:
            end_iteration = True

    return result
