import json
def improve(data):
    res = data[:-1]
    l = list()
    while len(res) > 1:
        d = '{'+res[res.index('[')+1:res.index(']')]+'}'
        l.append(eval(d))
        res = res[res.index(']')+1:]
    return l


if __name__ == "__main__":
    data = str
    with open('Data/Digital osciiloscope tablesetvalue.txt', 'r') as File:
        data = File.read()
    res = improve(data)
    jfile = json.dumps(res,indent=4)

    with open('Data/Tablesetvalues.json','w') as JFile:
        JFile.write(jfile)

