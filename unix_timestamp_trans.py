import time
import workflow


def timestamp_datetime(value):
    date_format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(date_format, value)
    return dt


def datetime_timestamp(dt):
    time.strptime(dt, '%Y-%m-%d %H:%M:%S')
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return str(int(s))


def query(param):
    wf = workflow.Workflow()
    try:
        wf.add_item(title=timestamp_datetime(float(param)), subtitle='from unix timestamp',
                    arg=timestamp_datetime(float(param)), valid=True)
    except:
        pass

    try:
        wf.add_item(title=datetime_timestamp(param), subtitle='to unix timestamp',
                    arg=datetime_timestamp(param), valid=True)
    except:
        pass

    wf.send_feedback()
