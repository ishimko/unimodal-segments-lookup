def is_increasing_at_point(function, point, epsilon=0.0001):
    return (function(point) - function(point + epsilon)) < 0


def is_decreasing_at_point(function, point, epsilon=0.0001):
    return (function(point) - function(point + epsilon)) > 0


def get_first_point_where(target_function, current_point, condition_function, delta, interval_end):
    i = 1
    while (not condition_function(target_function, current_point)) and (current_point <= interval_end):
        current_point += i * delta
        i += 1
    return current_point


def get_unimodal_segments(target_function, interval_begin, interval_end, min_extremum_delta):
    current_point = interval_begin
    result = []
    delta = min_extremum_delta / 5

    get_first_decreasing_point = lambda x: get_first_point_where(target_function, x, is_decreasing_at_point, delta,
                                                                 interval_end)
    get_first_increasing_point = lambda x: get_first_point_where(target_function, x, is_increasing_at_point, delta,
                                                                 interval_end)

    if is_decreasing_at_point(target_function, interval_begin):
        current_point = get_first_increasing_point(interval_begin)
        result.append((interval_begin, current_point))

    while current_point <= interval_end:
        current_interval_begin = get_first_decreasing_point(current_point)
        current_interval_end = get_first_increasing_point(current_interval_begin)
        result.append((current_interval_begin, current_interval_end))
        current_point = current_interval_end

    return result
