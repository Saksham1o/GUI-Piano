# Importing the libraries
from tkinter import *
import pygame

# initializing the pygame
pygame.init()
root = Tk()

# Setting the title and geometry
root.title("Music Box")
root.geometry("1352x700+0+0")
root.configure(background="white")

# creating the Frames
abc = Frame(root, bg="powder blue", bd=20, relief=RIDGE)
abc.grid()
abc1 = Frame(abc, bg="powder blue", bd=20, relief=RIDGE)
abc1.grid()
abc2 = Frame(abc, bg="powder blue", relief=RIDGE)
abc2.grid()
abc3 = Frame(abc, bg="powder blue", relief=RIDGE)
abc3.grid()

str = StringVar()
str.set("Just like Music")

#Functions for sound
def value_Cs():
    str.set("C#")
    sound = pygame.mixer.Sound("C#.wav")
    sound.play()


def value_A():
    str.set("A")
    sound = pygame.mixer.Sound("A.wav")
    sound.play()

def value_B():
    str.set("B")
    sound = pygame.mixer.Sound("B.wav")
    sound.play()

def value_C():
    str.set("C")
    sound = pygame.mixer.Sound("C.wav")
    sound.play()

def value_Bb():
    str.set("Bb")
    sound = pygame.mixer.Sound("Bb.wav")
    sound.play()

def value_Gs():
    str.set("G#")
    sound = pygame.mixer.Sound("G#.wav")
    sound.play()

def value_Ds():
    str.set("D#")
    sound = pygame.mixer.Sound("D#.wav")
    sound.play()

def value_Fs():
    str.set("F#")
    sound = pygame.mixer.Sound("F#.wav")
    sound.play()

def value_G():
    str.set("G")
    sound = pygame.mixer.Sound("G.wav")
    sound.play()

def value_D():
    str.set("D")
    sound = pygame.mixer.Sound("D.wav")
    sound.play()

def value_E1():
    str.set("E1")
    sound = pygame.mixer.Sound("E.mp3")
    sound.play()

def value_E():
    str.set("E")
    sound = pygame.mixer.Sound("E!.mp3")
    sound.play()

def value_F():
    str.set("F")
    sound = pygame.mixer.Sound("F!.mp3")
    sound.play()

def value_F1():
    str.set("F1")
    sound = pygame.mixer.Sound("F.mp3")
    sound.play()

def value_C1():
    str.set("C1")
    sound = pygame.mixer.Sound("C1.mp3")
    sound.play()

def value_D1():
    str.set("D1")
    sound = pygame.mixer.Sound("D1.mp3")
    sound.play()

