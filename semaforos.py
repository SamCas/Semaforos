from Queue import *
from random import *

ciclo_total = 120
semaforo = {1:"Norte",2:"Sur",3:"Este",4:"Oeste"}

class LaneQueue(object):

    def __init__(self):
        total_queue = 0

    def lane_randomfill(self):
        lane_queue = Queue(maxsize=0)
        for i in range(5):
            i = randint(2,5)
            lane_queue.put(i)
            print(lane_queue.get())

class TrafficLight(object):

    def __init__(self):
        semaforo = {1:"Norte",2:"Sur",3:"Este",4:"Oeste"}

    def light_change(self):
        state_change = {'green':'Verde','yellow':'Amarillo','red':'Rojo'}
        for count_down in range(ciclo_total, 0, -1):
            if count_down <= 120 and count_down > 62:
                print[state_change['green'], count_down]
            if count_down <= 62 and count_down > 58:
                print[state_change['yellow'], count_down]
            if count_down <= 58:
                print[state_change['red'], count_down]

def main():
    semaforo_prueba = TrafficLight()
    lane_prueba = LaneQueue()

    # print(lane_prueba.lane_fill())
    print(lane_prueba.lane_randomfill())
    #semaforo_prueba.light_change()

main()
