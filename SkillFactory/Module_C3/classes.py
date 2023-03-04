class Oleg:
    def method(self):
        print('I am Oleg')


class Anna(Oleg):
    def method(self):
        super().method()
        print('I am Anna')


class Boris(Oleg):
    def method(self):
        super().method()
        print('I am Boris')


class Chris(Anna, Boris):
    def method(self):
        super().method()
        print('I am Chris')


Chris().method()
