# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. 🇧🇷
# Write a Python program that opens and plays the audio from an MP3 file. 🇺🇸
# Escribe un programa en Python que abra y reproduzca el audio de un archivo MP3. 🇪🇸
# Écrivez un programme Python qui ouvre et lit le contenu audio d'un fichier MP3. 🇫🇷

import pygame
import time

pygame.init()
pygame.mixer.music.load("audio.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(0.1)
