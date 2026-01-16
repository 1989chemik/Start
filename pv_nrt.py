M_WATER = 18.0        # g/mol
R = 8.314             # J/(mol*K)
T = 293.15            # K (20°C)
V = 40.0              # m^3

#Typowy pokój 15m^2

while True:
    user_input = input("\nPodaj ilość dostarczonej wody [g] (q = wyjście): ")

    if user_input.lower() == "q":
        print("Koniec programu.")
        break

    try:
        mass_g = float(user_input)
    except ValueError:
        print("Błąd: podaj liczbę lub q.")
        continue

    n = mass_g / M_WATER
    pressure_pa = (n * R * T) / V
    pressure_kpa = pressure_pa / 1000
    pressure_bar = pressure_pa / 100000
    pressure_hpa = pressure_pa / 100

    print("\nWYNIKI:")
    print(f"Liczba moli: {n:.2f} mol")
    print(f"Ciśnienie: {pressure_pa:.2f} Pa")
    print(f"Ciśnienie: {pressure_hpa:.2f} hPa")
    print(f"Ciśnienie: {pressure_kpa:.4f} kPa")
    print(f"Ciśnienie: {pressure_bar:.6f} bar")

