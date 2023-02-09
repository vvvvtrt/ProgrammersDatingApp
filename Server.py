from typing import Tuple, Dict
from http import HTTPStatus
from urllib.parse import unquote
import json


def Read():
    try:
        with open("/home/vvvvtrt/UserData.json", "r") as ReadFile:
            data = json.load(ReadFile)
            return data
    except:
        return None

def Write(arr, mess):

    data = {
        "arr": arr,
        "message": mess
    }
    try:
        with open("/home/vvvvtrt/UserData.json", "w") as WriteFile:
            json.dump(data, WriteFile)
        return True
    except:
        return False


def your_processor(path:str) -> Tuple[int, Dict[str, str], str]:
    global se
    if path[1] == "j":
        m = path.split()
        path = "false"
        for i in Read()["arr"]:
            if m[1] == i[0]:
                path = "true"
    elif path[1] == "s":
        m = path.split()[1:]
        c = Read()["message"]
        path = ""
        for i in range(len(c)):
            if m[0] in c[i] and m[1] in c[i]:
                for j in range(2, len(c[i])):
                    path += c[i][j][0] + "*" + c[i][j][1] + "/"
    elif path[1] == "c":
        m = path.split()[1:]
        c = Read()["message"]
        path = ""
        for i in range(len(c)):
            if m[0] in c[i]:
                if m[0] == c[i][0]:
                    path += c[i][1] + "/"
                else:
                    path += c[i][0] + "/"
                # if m[0] == c[i][0]:
                #     for j in range(len(n)):
                #         if c[i][1] in n[j]:
                #             path += n[j][2] + "*"
                #     path += c[j][1] + "/"
                # else:
                #     for j in range(len(n)):
                #         if c[i][0] in n[j]:
                #             path += n[j][2] + "*"
                #     path += c[j][0] + "/"
    elif path[1] == "n":
        m = path.split("^")[1:]
        r = Read()["arr"]
        path = "false"
        for i in range(len(r)):
            if m[0] == r[i][0]:
                r[i][2] = m[1]
                r[i][3] = m[2]
                r[i][4] = m[3]
                Write(r, Read()["message"])
                path = "ok"
                break
    elif path[1] == "w":
        m = path.split("/")[2:]
        path = "ok"
        j = Read()["arr"]
        j.append(m)
        Write(j, Read()["message"])

    elif path[1] == "i":
        i = path.split()
        i = int(i[1])
        mails = Read()["arr"]
        path = ""
        if len(mails) - 1 < i:
            path = ""
            for j in range(5):
                path += "Clear/"
            path += "0/"
        else:
            path = ""
            for j in range(6):
                path += mails[i][j] + "/"
    elif path[1] == "p":
        i = path.split()
        i = i[1]
        path = i
        mails = Read()["arr"]
        for mail in range(len(mails)):
            if mails[mail][0] == i:
                for j in range(6):
                    path += mails[mail][j] + "/"
                break
        # ails = Read()["arr"]
        # for mail in mails:
        #     if mail == i:
        #         path = "true"
        #         break
        # else:
        #     path = "false"m

    elif path[1] == "m":
        i = path.split("/")[1:]
        path = i[1]
        chats = Read()["message"]
        for j in range(len(chats)):
            if i[1] in chats[j] and i[2] in chats[j]:
                chats[j].append([i[1], i[3]])
                Write(Read()["arr"], chats)
                path = "ok"
                break
        else:
            chats.append([i[1], i[2], [i[1], i[3]]])
            Write(Read()["arr"], chats)
            path = "new"

    return (200, {'Content-Type': 'text/txt'}, path)

def application(environ, start_response):
    try:
        status, headers, content = your_processor(unquote(environ.get('REQUEST_URI')))
        headers['Content-Length'] = str(len(content))

        start_response(
            "%d %s" % (status, HTTPStatus(status).phrase),
            list(headers.items())
        )

        yield content.encode('utf-8')
    except Exception as err:
        status, headers, content = 500, {'Content-Type': 'text/txt'}, err.__class__.__name__ + " ".join(err.args)
        headers['Content-Length'] = str(len(content))

        start_response(
            "%d %s" % (status, HTTPStatus(status).phrase),
            list(headers.items())
        )

        yield content.encode('utf-8')
