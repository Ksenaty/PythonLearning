from time import sleep


class TrafficLight:

    __color = 'Red'

    def running(self):
        while True:
            if TrafficLight.__color == 'Red':
                print('Горит красный свет')
                TrafficLight.__color = 'Yellow'
                sleep(7)
            elif TrafficLight.__color == 'Yellow':
                print('Горит желтый свет')
                TrafficLight.__color = 'Green'
                sleep(2)
            else:
                print('Горит зеленый свет')
                TrafficLight.__color = 'Red'
                sleep(7)


TrafficLight.running('Red')
