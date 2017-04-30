#Copyright by Brett Fraley 2017

class CLASS:
    def __init__(self, name):
        self.name = name
        self.s = 'class {}:\n    '.format(self.name)

    def __str__(self):
        return self.s


class ARGS:
    def __init__(self, arglist):
        self.arglist = arglist
        self.s = 'def __init__('
        
        for i in range(len(self.arglist)):
            self.s += (arglist[i] + ', ')


        self.s += '):\n    '

    def __str__(self):
        return self.s


class VAR:
    def __init__(self, keyname, value):
        self.s = '    self.{} = {}\n    '.format(keyname, value)

    def __str__(self):
        return self.s



class METHOD:
    def __init__(self, name):
        self.name = name
        self.s = '\n    def {}(self):\n    '.format(self.name)

    def __str__(self):
        return self.s



c = CLASS('Person')
a = ARGS(['test'])
v = VAR('hello', 'world')
m = METHOD('do')
result = str(c) + str(a) + str(v) + str(m)
print(result)
