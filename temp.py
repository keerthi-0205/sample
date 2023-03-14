class Temp:
    def __init__(self,t):
      self.t=t
    def process(self):
        if(self.t>=50):
            print('swimming')
            print('table tennis')
            print('carroms')
        print('coconut')
        print('go to home')
t=int(input('enter temperature'))
obj=Temp(t)
obj.process()