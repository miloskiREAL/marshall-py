# Lesson 7
import random
dc = random.randrange(1,21)
print("rolling...")
roll = random.randrange(1,21)
if roll >= dc:
    print(f"Success! you beat the Dungeon Masters DC of {dc} with your roll of {roll}")
else :
    print(f"Failure! :( you failed to beat the Dungeon Masters DC of {dc} with your roll of {roll}")