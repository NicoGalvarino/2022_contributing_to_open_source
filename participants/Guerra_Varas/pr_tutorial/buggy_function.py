import math

def angle_to_sexigesimal(angle_in_degrees, no_decimals=3):
    """
    Convert the given angle to a sexigesimal string of hours of RA.

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle, expressed in degrees

    Returns
    -------
    hms_str : str
        The sexigesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`
    """

    assert((type(angle_in_degrees) == float) or (type(angle_in_degrees) == int))

    if math.floor(no_decimals) != no_decimals:
        raise OSError('number of decimals should be an integer!')

    hours_num = angle_in_degrees * 24 / 180
    hours = math.floor(hours_num)

    min_num = (hours_num - hours) * 60
    minutes = math.floor(min_num)

    seconds_or = (min_num - minutes) * 60
    seconds = math.floor(seconds_or)

    decimals = seconds_or - seconds
    decimals_round = round(seconds, no_decimals)

    format_string = '{}:{}:{:.' + str(decimals_round) + 'f}'

    angle_sexigesimal = format_string.format(hours, minutes, seconds)

    return angle_sexigesimal
