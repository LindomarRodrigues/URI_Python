# -*- coding: utf-8 -*-

obs_um = input()
obs_dois = input()
obs_tres = input()

if obs_um == 'vertebrado':
    if obs_dois == 'ave':
        if obs_tres == 'carnivoro':
            print('aguia')
        elif obs_tres == 'onivoro':
            print('pomba')

    elif obs_dois == 'mamifero':
        if obs_tres == 'onivoro':
            print('homem')
        elif obs_tres == 'herbivoro':
            print('vaca')

elif obs_um == 'invertebrado':
    if obs_dois == 'inseto':
        if obs_tres == 'hematofago':
            print('pulga')
        elif obs_tres == 'herbivoro':
            print('lagarta')

    elif obs_dois == 'anelideo':
        if obs_tres == 'hematofago':
            print('sanguessuga')
        elif obs_tres == 'onivoro':
            print('minhoca')
