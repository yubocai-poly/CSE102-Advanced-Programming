# Question 8
class Rdict:
    def __init__(self):
        self.__fwd = {}
        self.__bwd = {}

    def associate(self, a, b):
        if a in self.__fwd or b in self.__bwd:
            print('Runtime Erro')
            raise RuntimeError
        self.__fwd[a] = b
        self.__bwd[b] = a

# Question 9

    def __len__(self):
        return len(self.__fwd)

# Question 10

    def __getitem__(self, key):
        (ind, keyname) = key
        if ind > 0:
            return self.__fwd[keyname]
        elif ind < 0:
            return self.__bwd[keyname]


# Question 11

    def __setitem__(self, key, value):
        (ind, keyname) = key
        if ind > 0:
            self.associate(keyname, value)
        else:
            self.associate(value, keyname)