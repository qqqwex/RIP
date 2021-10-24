# используется для сортировки
from operator import itemgetter
 
class Vod:
    """Водитель"""
    def __init__(self, id, fio, sal, avto_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.avto_id = avto_id
 
class Avto:
    """Автопарк"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class VodAvto:
    """
    'Сотрудники отдела' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, avto_id, vod_id):
        self.avto_id = avto_id
        self.vod_id = vod_id
 
# Отделы
vods = [
    Vod(1, 'Конев', 340, 2),
    Vod(2, 'Андронов', 520, 1),
    Vod(3, 'Григорьев', 210, 3),
    Vod(4, 'Агров', 320, 4),
 ]
 
# Сотрудники
avtos = [
    Avto(1, 'Горгараж'),
    Avto(2, 'АвтоСтринк'),
    Avto(3, 'Автолюбитель'),
    Avto(4, 'Автодом'),
]
 
avtos_vods = [
    VodAvto(1,1),
    VodAvto(2,2),
    VodAvto(3,3),
    VodAvto(3,4),
    VodAvto(3,5),
 ]
 
def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(e.fio, e.sal, d.name) 
        for d in avtos 
        for e in vods
        if e.avto_id==d.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.avto_id, ed.vod_id) 
        for d in avtos
        for ed in avtos_vods
        if d.id==ed.avto_id]
    
    many_to_many = [(e.fio, e.sal, avto_name) 
        for avto_name, avto_id, vod_id in many_to_many_temp
        for e in vods if e.id==vod_id]
 
    print('Задание B1')
    a1 = list(filter(lambda x : (str)(x[2]).startswith('А'), one_to_many))
    a1 = [(el[2], el[1]) for el in a1]
    print(a1)

    print('Задание B2')
    res_2 = []
    for d in avtos:
        d_vods = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_vods) > 0:
           res_2.append(min(d_vods, key = lambda i: i[1] ))

        res_2 = sorted(res_2, key = lambda i: i[1])
    print(res_2)
 
    print('Задание B3')
    res_3 = sorted(many_to_many, key = itemgetter(2))
    print(res_3)

if __name__ == '__main__':
    main()
 

