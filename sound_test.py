import pygame

pygame.init() # Get ready to play the sound
pygame.mixer.music.load('audio/game_win.wav')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
pygame.quit()

print("Done")