def array():
    user_input = input("Zadej čísla s mezerami: ")
    number_list = list(map(int, user_input.split()))
    total_sum = sum(number_list)
    print(f"Zadané čísla jsou: {number_list}")
    print(f"Součet zadaných čísel: {total_sum}")


array()
print("\ncheš pokračovat")
print("1 - Pokračovat")
print("2 - konec")

print("\n")
ano_ne = input()
if ano_ne == "1":
    array()
elif ano_ne == "2":
    exit()
