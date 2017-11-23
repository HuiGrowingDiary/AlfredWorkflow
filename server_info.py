import workflow
import os
import sys


def load_servers():
    server_list = []
    with open(os.path.expanduser('~') + '/.alfred/resource.txt') as f:
        header = f.readline()
        header = header.strip()
        header_infos = header.split('\t')

        for line in f:
            line = line.strip()
            infos = line.split('\t')
            server_info = {}
            for i in range(len(infos)):
                server_info[header_infos[i]] = infos[i]
            server_list.append(server_info)
    return server_list


def search_server(param):
    sys.stderr.write('seach param: %s\n' % param)
    server_list = load_servers()

    idc = ''
    ip = ''
    find_items = []

    params = param.split()
    try:
        int(params[0][0])
        ip = params[0]
        if len(params) > 1:
            idc = params[1]
    except:
        idc = params[0]
        if len(params) > 1:
            ip = params[1]

    for server in server_list:
        if ip in server['detail_ip'] and idc in server['idc']:
            find_items.append(server)

    wf = workflow.Workflow()
    for server in find_items:
        title = server['idc'] + ' ' + server['pub_ip']
        for k, v in server.items():
            try:
                if int(v) == 1:
                    title += ' ' + k
            except:
                continue

        try:
            wf.add_item(title=server['pub_ip'], subtitle=title, arg=server['pub_ip'], valid=True)
        except:
            continue
    wf.send_feedback()
