import ctypes
import workflow

def to_uint(param):
    if len(param) == 1 and param == '-':
        param = 0

    param = int(param)
    uint_num = str(ctypes.c_uint32(param).value)

    wf = workflow.Workflow()
    try:
        wf.add_item(title=uint_num, subtitle='to uint',
                    arg=uint_num, valid=True)
    except:
        pass

    wf.send_feedback()
