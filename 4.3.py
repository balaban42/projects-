print('Добро пожаловать в игру Mad Libs!')
k = 1
while k == True:
    print('Ну что ж, давайте сыграем!')
    verb = input('Введите глагол мн. числа, прошедшего времени: ')
    _verb = input('Введите глагол ед. числа, прошедшего времени, мужского рода: ')
    animal = input('Введите название животного, мужского рода: ')
    name = input('Введите имя: ')
    _name = input('Введите еще одно имя: ')
    noun = input('Введите сущиствительное в Пр.п.: ')
    adjective = input('Введите прилагательное, отвечающее на вопрос (каким?): ')
    part = input('Введите часть тела в В.п.: ')
    _adjective = input('Введите прилагательное мн. числа: ')
    _noun = input('Введите существительное ед. числа в Пр.п.: ')
    print()
    print(verb, 'по лесу два товарища, и', _verb, 'на них', animal, '.')
    print(name, 'бросился бежать, влез на дерево и спрятался,')
    print('а', _name, 'остался на', noun + '. Делать ему нечего он')
    print('упал наземь и притворился', adjective + '.')
    print(animal, 'подошёл к нему и стал нюхать: он и дышать перестал.')
    print(animal, 'понюхал его лицо и отошёл.')
    print('Когда', animal, 'ушёл,', name, 'слез с дерева и начал смеяться.')
    print('— Ну что,- говорит,-', animal, 'тебе на', part, 'говорил?')
    print('— А он сказал мне, что', _adjective, 'люди те, которые в', _noun, 'от товарищей убегают.')
    print('Введите 1 - если хотите продолжить, 0 - если завершить игру')
    k = int(input())

print('Спасибо за игру!')
