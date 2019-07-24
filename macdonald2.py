# macdonald2

def main():
    animals = ["cow", "pig", "horse", "duck", "chicken"]
    sounds = ["moo", "oink", "neigh", "quack", "cluck"]

    for i in range(5):
        chorus(animals[i], sounds[i])
        print()

def chorus(animal, sound):
    oldMac()
    print("And on that farm he had a " + animal + ", Ee-igh, Ee-igh, Oh!")
    print("With a " + sound + ", " + sound + " here and a " + sound + ", " + sound + " there.")
    print("Here a " + sound + ", " + "there a " + sound + " everywhere a " + sound + " " + sound + "!")
    oldMac()

def oldMac():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh")

main()
