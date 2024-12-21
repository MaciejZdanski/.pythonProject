import random
import time  # Import modułu do pomiaru czasu
from sympy import mod_inverse

def lagrange_interpolation(x, points, prime):
    """ Funkcja do interpolacji Lagrange'a w celu odzyskania sekretu. """
    total = 0
    for i, (xi, yi) in enumerate(points):
        term = yi
        for j, (xj, _) in enumerate(points):
            if i != j:
                numerator = (x - xj) % prime
                denominator = (xi - xj) % prime
                term = (term * numerator * mod_inverse(denominator, prime)) % prime
        total = (total + term) % prime
    return total

def generate_shares(secret, k, n, prime):
    """ Funkcja generująca udziały sekretu przy użyciu wielomianu. """
    coefficients = [secret] + [random.randint(1, prime - 1) for _ in range(k - 1)]
    shares = []
    polynomial = f"P(x) = {coefficients[0]}"
    for i in range(1, len(coefficients)):
        polynomial += f" + {coefficients[i]}*x^{i}"

    for i in range(1, n + 1):
        y = sum([coefficients[j] * (i ** j) for j in range(k)]) % prime
        shares.append((i, y))
    
    print("\nWzór funkcji wielomianowej: ")
    print(polynomial)
    
    return shares

def main():
    print("#################################################")
    print("## Witaj w programie dzielenia sekretu Shamira ##")
    print("#################################################\n")

    prime = 104729  # Duża liczba pierwsza dla działań modulo
    
    while True:
        print("Wybierz opcję:")
        print("1. Podziel sekret")
        print("2. Odczytaj sekret")
        print("3. Zakończ program")
        choice = input("Twój wybór: ")

        if choice == '1':
            try:
                secret = int(input("Podaj sekret (liczba całkowita): "))
                k = int(input("Podaj minimalną liczbę udziałów (k): "))
                n = int(input("Podaj całkowitą liczbę udziałów (n, n>=k): "))

                if n < k:
                    print("Liczba udziałów nie może być mniejsza niż k. Spróbuj ponownie.\n")
                    continue

                start_time = time.time()  # Rozpoczęcie pomiaru czasu
                shares = generate_shares(secret, k, n, prime)
                end_time = time.time()  # Zakończenie pomiaru czasu

                print("\nWygenerowane udziały:")
                for share in shares:
                    print(f"Udział: {share}")
                
                elapsed_time_ms = (end_time - start_time) * 1000  # Przeliczenie na milisekundy
                print(f"\nCzas działania: {elapsed_time_ms:.2f} ms\n")
                
            except ValueError:
                print("Błąd: Nieprawidłowe dane wejściowe.\n")

        elif choice == '2':
            try:
                k = int(input("Podaj liczbę udziałów potrzebnych do odzyskania sekretu (k): "))
                print("Podaj udziały w formacie x y (np. 1 1234):")
                points = []
                for _ in range(k):
                    x, y = map(int, input("Udział: ").split())
                    points.append((x, y))

                recovered_secret = lagrange_interpolation(0, points, prime)
                print(f"\nOdzyskany sekret: {recovered_secret}\n")
            except ValueError:
                print("Błąd: Nieprawidłowe dane wejściowe.\n")
            except Exception as e:
                print(f"Wystąpił błąd: {e}\n")

        elif choice == '3':
            print("Dziękujemy za skorzystanie z programu. Do widzenia!")
            break
        else:
            print("Nieznana opcja. Spróbuj ponownie.\n")

if __name__ == "__main__":
    main()
