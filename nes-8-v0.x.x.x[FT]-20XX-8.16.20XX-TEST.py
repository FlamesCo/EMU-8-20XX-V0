import pygame
import sys
import random

pygame.init()

# Initialize Chip-8 memory and display
memory = [0] * 4096
V = [0] * 16
I = 0
pc = 0x200
display = [[0] * 64 for _ in range(32)]
stack = []
delay_timer = 0
sound_timer = 0
keys = [0] * 16

# Load font set into memory
fontset = [
    0xF0, 0x90, 0x90, 0x90, 0xF0,
    0x20, 0x60, 0x20, 0x20, 0x70,
    0xF0, 0x10, 0xF0, 0x80, 0xF0,
    0xF0, 0x10, 0xF0, 0x10, 0xF0,
    0x90, 0x90, 0xF0, 0x10, 0x10,
    0xF0, 0x80, 0xF0, 0x10, 0xF0,
    0xF0, 0x80, 0xF0, 0x90, 0xF0,
    0xF0, 0x10, 0x20, 0x40, 0x40,
    0xF0, 0x90, 0xF0, 0x90, 0xF0,
    0xF0, 0x90, 0xF0, 0x10, 0xF0,
    0xF0, 0x90, 0xF0, 0x90, 0x90,
    0xE0, 0x90, 0xE0, 0x90, 0xE0,
    0xF0, 0x80, 0x80, 0x80, 0xF0,
    0xE0, 0x90, 0x90, 0x90, 0xE0,
    0xF0, 0x80, 0xF0, 0x80, 0xF0,
    0xF0, 0x80, 0xF0, 0x80, 0x80
]

for i in range(80):
    memory[i] = fontset[i]

# Initialize pygame screen
screen = pygame.display.set_mode((640, 320))
pygame.display.set_caption('Chip-8 Emulator')

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Fetch, decode, and execute opcode
    opcode = memory[pc] << 8 | memory[pc + 1]
    pc += 2

    # Handle opcode (simplified for demonstration, many opcodes are not implemented)
    if opcode & 0xF000 == 0xA000:
        I = opcode & 0x0FFF

    # Update timers
    if delay_timer > 0:
        delay_timer -= 1
    if sound_timer > 0:
        sound_timer -= 1
        if sound_timer == 0:
            print("BEEP!")

    # Draw display (simplified, assumes screen is cleared each cycle)
    screen.fill((0, 0, 0))
    for y in range(32):
        for x in range(64):
            if display[y][x]:
                pygame.draw.rect(screen, (255, 255, 255), (x * 10, y * 10, 10, 10))
    pygame.display.update()

# Note: This is a very simplified and incomplete example. A full implementation would include many more opcodes,
# keyboard input, sound, and proper timing.
