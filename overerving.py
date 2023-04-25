class Persoon:

    def __init__(self,id):
        self.id = id

class Docent(Persoon):

    def __init__(self,id,vak):
        super().__init__(id)
        self.vak = vak
class Cursist(Persoon):

    def __init__(self,id,opleiding):
        super().__init__(id)
        self.opleiding = opleiding
p = Persoon("p1")
d = Docent("p2","Python")
c = Cursist("p3","Software developer")



