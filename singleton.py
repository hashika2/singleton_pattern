class Singleton:
    _instance=None
    @staticmethod
    def getInstance():
        if Singleton._instance==None:
            Singleton()
        return Singleton._instance
    def _init_(self):
        if Singleton._instance!=None:
            raise Exception("this class is singleton")
        else:
            Singleton._instance=self
s=Singleton()
print s

s=Singleton.getInstance()
print s

s=Singleton.getInstance()
print s
