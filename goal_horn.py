import pygame
import time
import threading

AUDIO_AVAILABLE = True

try:
    pygame.mixer.init()
except pygame.error:
    AUDIO_AVAILABLE = False
    print("[WARN] No audio device available")

# Shared flag to stop the horn
stop_horn = False

def play_blast(duration):
    if not AUDIO_AVAILABLE:
        print(f"[SIMULATION] Playing {duration}-second blast")
        time.sleep(duration)
        return

    sound = pygame.mixer.Sound("horn.mp3")
    sound.play()
    time.sleep(duration)
    sound.stop()


def play_sequence():
    print("[INFO] Goal horn sequence started")

    for duration in [4, 4, 6]:
        play_blast(duration)
        time.sleep(1)

    print("[INFO] Goal horn sequence complete")


def stop_sequence():
    global stop_horn
    stop_horn = True
