print("Wlazl kotek na plotek")

print("Wojtek")

# print(Wlazl kotek na plotek)
#
# print(Wojtek)

# wywyołanty kod błędu to: SyntaxError: invalid syntax. Perhaps you forgot a comma?


# print"Wlazl kotek na plotek"
#
# print"Wojtek"

# wywołany kod błędu to: SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

print('Wlazl kotek na plotek')

print('Wojtek')

print("Wlazł kotek na płotek", 'Wojtek')

print("""
Wlazł kotek na płotek
Wojtek""")

print("Wlazł kotek na płatek"), print("wojtek")

print("Kurs","Programowania","w", sep="***", end="...")
print("Pythonie")

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

print("    *","\n   * *","\n  *   *", "\n *     *","\n***   ***","\n  *   *","\n  *   *","\n  *****")

print("    *     "*2)
print("   * *    "*2)
print("  *   *   "*2)
print(" *     *  "*2)
print("***   *** "*2)
print("  *   *   "*2)
print("  *   *   "*2)
print("  *****   "*2)

print('"Ucze sie"','\n""jezyka""', '\n"""Python"""')

pomoaranczowy_krol = 3
agnieszka = 5
adam = 6

print(pomoaranczowy_krol, agnieszka, adam, sep=",")

pomaranczy_razem = pomoaranczowy_krol + agnieszka + adam

print(pomaranczy_razem)

print(pomaranczy_razem // adam)
print(pomaranczy_razem // agnieszka)
print(pomaranczy_razem // pomoaranczowy_krol)

print(str(agnieszka), str(pomaranczy_razem), int(pomaranczy_razem))

kilometry = 12.25
mile = 7.38

mile_na_kilometry =  mile * 1.61
kilometry_na_mile =  mile / 1.61

print(mile, "mi to", round(mile_na_kilometry, 2), "km")
print(kilometry, "km to", round(kilometry_na_mile, 2), "mi")

x = 12
x = float(x)
y= 3*x**3 - 2*x**2 + 3*x -1
print("y =", y)


#Ten program oblicza liczbę sekund w danej liczbie godzin.

a = 3 #liczba godzin
sekundy = 3600 #liczba sekund w 1 godzinie

print("Godzin: ", a) # wyświetla ilość godzin
print("Sekund w godzinach: ", a * sekundy)  # wyswietla ilość sekund w zadanej liczbie godzin
print("Do widzenia")


a = 1.2
b = 2.5

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("\nI to by było na tyle!")

x = float(input("Wprowadź wartość dla x: "))

y = (1 /( x + (1 /( x + (1 / (x + ( 1 /x)))))))

print("y =", y)

h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

czas_zakonczenia_minuty = (h * 60 + m + d) % (24 * 60)
godzina_zakonczenia = czas_zakonczenia_minuty // 60
minuta_zakonczenia = czas_zakonczenia_minuty % 60

print("Czas zakończenia:", f"{godzina_zakonczenia:02}:{minuta_zakonczenia:02}")

#Stwórz program, dzięki któremu użytkownik przekonwertuje odległość podaną w kilometrach na podane jednostki:
# milimetry, centrymentry, metry, cale, stopy, mile.

kilometry = input("Podaj liczbę kilometrów: ")


kilometry_na_mile = int(kilometry) * 1.61
kilometry_na_stopy = int(kilometry) * 3280.84
kilometry_na_cale = int(kilometry) * 39370.1
kilometry_na_metry = int(kilometry) * 1000
kilometry_na_centymetry = int(kilometry) * 100_000
kilometry_na_milimetry = int(kilometry) * 1_000_000


print(kilometry, "km to", round(kilometry_na_mile, 2), "mi")

print(kilometry, "km to", round(kilometry_na_stopy, 2), "ft")

print(kilometry, "km to",  round(kilometry_na_cale, 2), "inch")

print(kilometry, "km to", round(kilometry_na_metry, 2), "m")

print(kilometry, "km to", round(kilometry_na_centymetry, 2), "cm")

print(kilometry, "km to", round(kilometry_na_milimetry, 2), "mm")