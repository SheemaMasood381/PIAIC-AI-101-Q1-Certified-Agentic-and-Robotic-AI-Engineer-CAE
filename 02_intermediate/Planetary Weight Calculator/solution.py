all_planets_gravity = {
    "mercury": 37.6/100,
    "venus": 88.9/100,
    "mars": 37.8/100,
    "jupiter": 236.0/100,
    "saturn": 108.1/100,
    "uranus": 81.5/100,
    "neptune": 114.0/100
}
earth_weight = float(input("Enter a weight on Earth: "))
print("This is a list of all planets: ")
for key, val in all_planets_gravity.items():
    print(key)
planet = input("Enter a planet: ")

if (planet in all_planets_gravity):
    print(f"Your weight on planet {planet} is { round(earth_weight*all_planets_gravity[planet], 2) }N")
else:
    print(f"{planet} is not exist in our list")