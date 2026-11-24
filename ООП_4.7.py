class Pet:
    _count = 0
    # _objPet = []
    _f = None
    _l = None

    def __init__(self, name):
        self.name = name
        self.__class__._count += 1
        # self._objPet.append(self)
        if not self.__class__._f:
            self.__class__._f = self
        self.__class__._l = self

    @classmethod
    def first_pet(cls):
        if cls._l:  # cls._objPet:
            return cls._l  # cls._objPet[0]

    @classmethod
    def last_pet(cls):
        if cls._f:  # cls._objPet:
            return cls._f  # cls._objPet[-1]

    @classmethod
    def num_of_pets(cls):
        return cls._count


pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets(), pet1.first_pet().name)
