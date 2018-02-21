# This is Homework00 test script!

ime_string=input("Koje je Vase ime: ")
ime_string=str(ime_string)

specijalna_imena=['Mirza',"Nikola", "Vanja"]

print("Hello " + ime_string)
rekao_je_broj = False

while not rekao_je_broj:

    god_string = str(input("Koliko imate godina: "))



    if god_string.isnumeric():
        god_broj=int(god_string)
        rekao_je_broj = True
    else:
        print("Izvinite ne razumijemo se!")


ime_malim_slovima = ime_string.lower()
print(ime_malim_slovima)
pozicija_poslednjeg_slovo = len(ime_string)-1
poslednje_slovo=ime_malim_slovima[pozicija_poslednjeg_slovo]

if poslednje_slovo=="a":
    pol="zenski"
else:
    pol="muski"

if god_broj >= 18:
    print(ime_string + " udjite!")
    print("Dobrodosli!")
else:
    print(ime_string + " ne mozete da udjete!")
    print("Vratite se kad porastete!")

if ime_malim_slovima.title() in specijalna_imena:
    print("Dobrodosli:")
else:
    if pol == "muski":
        print("Bravo brko!")
    else:
        print("Hello beauty")


