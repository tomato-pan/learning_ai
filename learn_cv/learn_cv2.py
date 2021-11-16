class Person():
    def __init__(self, name, sex):
        self._name = name
        self._sex = sex

    @property
    def name(self):
        return self._name

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self,sex):
        self._sex = sex

    @name.setter
    def name(self,name):
        self._name=name

    def play(self):
        if self._sex <= "male":
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


if __name__ == '__main__':
    pp1 = Person("pj","male")
    pp2 = Person("lsy","female")
    print(pp1.sex)
    pp2.name = "abc"
    print(pp2.name)
    pp1.play()
    pp2.play()


