class foo:
    def hello(self):
        print(self.__class__.__name__.lower())


class Bar(foo):
    def hello(self):
        return super().hello()
    
bar = Bar()
bar.hello()