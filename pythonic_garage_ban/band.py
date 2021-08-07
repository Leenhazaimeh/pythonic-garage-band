from abc import abstractclassmethod

class Musician:
    members = [] #list of instances
    def __init__(self,name):
        self.name = name
        Musician.members.append(self)
        

    @abstractclassmethod
    def __str__(self):
        pass

    @abstractclassmethod
    def __repr__(self):
        pass

    @abstractclassmethod
    def get_instrument(self):
        pass

    @abstractclassmethod
    def play_solo(self):
        pass
class Guitarist(Musician):
    def __str__(self) :

        return "My name is {} and I play guitar".format(self.name)

    def __repr__(self):

        return "Guitarist instance. Name = {}".format(self.name)

    def get_instrument(self):
        return  "guitar"

    def play_solo(self):
        return "face melting guitar solo"

class Drummer(Musician):
 
    def __str__(self) :

        return "My name is {} and I play drums".format(self.name)

    def __repr__(self):

        return "Drummer instance. Name = {}".format(self.name)

    def get_instrument(self):
        return  "drums"

    def play_solo(self):
        return "rattle boom crash"


class Bassist(Musician):
    def __str__(self) :

        return "My name is {} and I play bass".format(self.name)

    def __repr__(self):

        return "Bassist instance. Name = {}".format(self.name)

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Band(Musician):
    instances=[]
    def __init__(self, name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)
             
    def play_solos(self):
        each_member=[]
        for x in self.members:
            each_member.append(x.play_solo())
        return each_member
    def __str__(self):
        
        return f" i am {self.name} and welcome to you "

    def __repr__(self):

        return f"Name = {self.name}"
    @classmethod
    def to_list(class_method):
        
        return class_method.instances