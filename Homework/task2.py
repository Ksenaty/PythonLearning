class Road:
    _length = 0
    _width = 0

    def mass(self, thickness):
        self.thickness = thickness
        print('Для покрытия покрытия одного кв метра дороги асфальтом необходимо {} тонн'
              .format((self._length * self._width * 25 * thickness)/1000))


first = Road()
first._length = 20
first._width = 5000
first.mass(5)
