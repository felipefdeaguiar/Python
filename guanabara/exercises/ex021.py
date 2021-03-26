"""
    curso Python 3 - Exercício Python #021
    Faça um programa em Python que abra e reproduza um audio de um arquivo em MP3.
    26.03.2021 - Felipe Ferreira de Aguiar
"""

import pyglet
music = pyglet.resource.media('ex021.mp3')
music.play()
pyglet.app.run()
