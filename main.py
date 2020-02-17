name = input("What is your name?") 

print(name + " wakes up and notices they are in a forest and have no idea why.")

envelope = input(name + " walks around and notices two envelopes labeled '1' and '2'. Which should " + name + " open?") 

if envelope == ("1"):
    print(name + " opens the one labeled '1' and inside finds a key with a weird symbol. Seconds later, envelope '2' disappears.")
else:
    print("Inside envelope '2' " + name + " finds a map of the area with an area marked with an X")

print(name + " starts walking around and runs into an animal he's never seen before.")
animal = input("Should " + name + " run or fight?") 

if animal == "run":
    print(name + " decides to run and they ran as fast as a baby running away from drinking their medicine!")
else:
    print(name + " decides to fight it for some reason and they actually beat it somehow :') ")

print(name + " keeps walking and is met by two paths")
paths = input("Should " + name + " take the left or right path?") 

if paths == ("left"):
    print(name + " wasted 40 minutes of their life walking down that path. It led to nowhere so you turn back and take the other path and 2 hours later arrive at a cave!")
else: 
    print(name + " took the right path and eventually arrives at a cave.")

print("There is a locked door with two slots. " + name + " sees one of the slots looks like the item they have so they proceed to put it in.")
print(name + " hears a click sound and the door opens. There is a sign that reads 'you won. you can go home now.'")
print("So, " + name + " goes home!")

print("THE END")



