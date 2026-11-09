import datetime


def broken_total():
    return missing_total


def add(a, b):
    return a + b


def record(value, history):

    if history is not None:
        history.append(value)
        return history
    else:
        new_history = [value]
        return new_history


def timeNow():
    return datetime.datetime.now()
