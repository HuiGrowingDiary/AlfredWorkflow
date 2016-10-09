import struct
import socket
import workflow


def ip2int(value):
    return str(socket.ntohl(struct.unpack("I",socket.inet_aton(str(value)))[0]))


def int2ip(value):
     return socket.inet_ntoa(struct.pack('I',socket.htonl(value)))


def query(param):
    wf = workflow.Workflow()
    try:
        wf.add_item(title=int2ip(int(param)), subtitle='int2ip',
                    arg=int2ip(int(param)), valid=True)
    except:
        pass

    try:
        wf.add_item(title=ip2int(param), subtitle='ip2int',
                    arg=ip2int(param), valid=True)
    except:
        pass

    wf.send_feedback()
