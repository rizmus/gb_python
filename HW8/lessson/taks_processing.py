from data_storage import get_data, change_data

a = None


def print_job(x, date):
    global a
    if a is None:
        a = get_data(x)
    return a[date]


def create_job(x, date, time, txt):
    global a
    if a is None:
        a = get_data(x)
    a[date] = txt

    return True


def delete_job(x, date, time):
    if a is None:
        a = get_data(x)
    a[date][time - 1] = ''
    return True


def unlog_sys(x):
    global a
    if a is None:
        a = get_data(x)
    change_data(a)
    a = None
    return True