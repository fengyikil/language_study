class Order(object):
    def __init__(self):
        self.code = []
        self.data = []
        self.call_frame = []
        self.pc = 0


class Code(object):
    def __init__(self, op, *data):
        self.op = op
        self.data = []
        for tmp in data:
            self.data.append(tmp)

    def __str__(self):
        return 'code({op},{data})'.format(
            op=self.op,
            data=self.data
        )

    def __repr__(self):
        return self.__str__()


class Data(object):
    def __init__(self, type, name, value):
        self.type = type
        self.name = name
        self.value = value

    def __str__(self):
        return 'Data({type},{name},{value})'.format(
            type=self.type,
            name=self.name,
            value=self.value
        )

    def __repr__(self):
        return self.__str__()


cc = Code("op")
print(cc)
dd = Data('int','lv',5)
print(dd)