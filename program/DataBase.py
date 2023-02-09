import json

def Read():
    try:
        with open("DataBase.json", "r") as ReadFile:
            data = json.load(ReadFile)
            return data
    except:
        return None

def Write(mail):

    data = {
        "mail": mail
    }

    with open("DataBase.json", "w") as WriteFile:
        json.dump(data, WriteFile)

if __name__ == '__main__':
    print(Write(""))