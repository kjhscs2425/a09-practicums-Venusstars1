def choose_practicum():
    practicum = input("please sign up for a practicum ")
    if practicum in ["costumes", "scenery", "lighting", "sound", "Costumes", "Scenery", "Lighting", "Sound"]:
        return practicum
    else:
        print ("invalid choice")
        return choose_practicum()

def main_function():
    name = input("Hello, what is your name? ")
    practicum = choose_practicum()
    print(f"Congratulations {name} you are signed up for {practicum}")
main_function()