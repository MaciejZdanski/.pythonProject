import math, hashlib, os
from tabulate import tabulate
import matplotlib.pyplot as plt
import pennylane as qml
import numpy as np
import random
from scipy.stats import chisquare
from collections import Counter

# Długość każdej liczby w bitach
bit_length = 8

# Ustawienie urządzenia z pięcioma qubitami dla większej losowości
dev = qml.device("default.qubit", wires=5, shots=1)

@qml.qnode(dev)
def quantum_random_bits():
    """
    Generuje pięć losowych bitów (0 lub 1) przy użyciu obliczeń kwantowych.
    """
    for i in range(5):
        qml.Hadamard(wires=i)
    return [qml.sample(qml.PauliZ(i)) for i in range(5)]

def quantum_random_number(bit_length):
    """
    Generuje losową liczbę dziesiętną z szumu kwantowego.
    """
    bits = []
    for _ in range(math.ceil(bit_length / 5)):
        generated_bits = quantum_random_bits()
        bits.extend(int((bit + 1) / 2) for bit in generated_bits)
    return int("".join(map(str, bits[:bit_length])), 2)

def bits_to_decimal(bits):
    """
    Konwertuje ciąg bitów na liczbę dziesiętną.
    """
    return int("".join(map(str, bits)), 2)

def bit_rotation_xor(number, rng, bit_length=8):
    """
    Losowe przesunięcie bitów i operacja XOR w celu poprawy rozkładu.
    """
    shift = rng.integers(1, bit_length)  # Losowe przesunięcie bitów
    rotated = ((number << shift) | (number >> (bit_length - shift))) & ((1 << bit_length) - 1)
    return number ^ rotated

def dynamic_hash_mixing(number, rng, bit_length=8):
    """
    Miesza liczbę za pomocą SHA256, BLAKE2, XOR z rotacją oraz dodatkowego źródła losowości.
    Liczba iteracji mieszania jest dynamicznie wybierana od 5 do 15.
    """
    max_value = 2 ** bit_length
    iterations = rng.integers(5, 16)  # Losowa liczba iteracji od 5 do 15
    for _ in range(iterations):
        if rng.random() > 0.5:
            hash_object = hashlib.sha256(str(number).encode('utf-8'))
        else:
            hash_object = hashlib.blake2b(str(number).encode('utf-8'), digest_size=2)
        hash_number = int(hash_object.hexdigest(), 16) % max_value
        number = bit_rotation_xor(hash_number, rng, bit_length)
        number = (number + int.from_bytes(os.urandom(1), "big")) % max_value
    return number

def generate_random_numbers(num_numbers, bit_length, seed=None):
    """
    Generuje losowe liczby dziesiętne z dynamicznym mieszaniem i większą ilością losowości.
    """
    rng = np.random.default_rng(seed)
    return [dynamic_hash_mixing(quantum_random_number(bit_length), rng, bit_length=bit_length) for _ in range(num_numbers)]

# Pobranie liczby liczb od użytkownika
while True:
    try:
        num_numbers = int(input("Podaj, ile liczb chcesz wygenerować: "))
        if num_numbers > 0:
            break
        else:
            print("Liczba musi być większa niż 0. Spróbuj ponownie.")
    except ValueError:
        print("Podaj poprawną liczbę całkowitą.")


# Generowanie liczb QRNG
random_numbers_qrng = generate_random_numbers(num_numbers, bit_length, seed=42)

# Generowanie liczb PRNG
random.seed(42)
random_numbers_prng = [random.randint(0, (2 ** bit_length) - 1) for _ in range(num_numbers)]

# Wygenerowanie bitów do testu serii
random_bits_qrng = [int(x) for num in random_numbers_qrng for x in f"{num:0{bit_length}b}"]
random_bits_prng = [int(x) for num in random_numbers_prng for x in f"{num:0{bit_length}b}"]

# Testy statystyczne

def chi_square_test(data, bins=10):
    observed, _ = np.histogram(data, bins=bins)
    expected = [len(data) / bins] * bins
    return chisquare(f_obs=observed, f_exp=expected)

def runs_test(bits):
    runs = sum(bits[i] != bits[i - 1] for i in range(1, len(bits))) + 1
    n = len(bits)
    expected_runs = (2 * n - 1) / 3
    variance = (16 * n - 29) / 90
    return runs, (runs - expected_runs) / (variance ** 0.5)

def entropy(data):
    counts = Counter(data)
    probabilities = [count / len(data) for count in counts.values()]
    return -sum(p * math.log2(p) for p in probabilities)

# Obliczenie wyników testów
chi2_qrng, p_value_qrng = chi_square_test(random_numbers_qrng, bins=8)
runs_qrng, z_score_qrng = runs_test(random_bits_qrng)
ent_qrng = entropy(random_numbers_qrng)

chi2_prng, p_value_prng = chi_square_test(random_numbers_prng, bins=8)
runs_prng, z_score_prng = runs_test(random_bits_prng)
ent_prng = entropy(random_numbers_prng)

# Wyświetlenie wyników w tabelach
print("\n### Wyniki testów QRNG: ###")
print("\nWygenerowane liczby QRNG:")
print([int(num) for num in random_numbers_qrng])  # Konwersja na normalne liczby
print(tabulate([
    ["Test Chi-kwadrat", f"χ²={chi2_qrng:.2f}", f"p-value={p_value_qrng:.4f}"],
    ["Test Serii", f"Liczba serii={runs_qrng}", f"z-score={z_score_qrng:.4f}"],
    ["Test Entropii", f"Entropia={ent_qrng:.4f}", ""]
], headers=["Test", "Wynik 1", "Wynik 2"], tablefmt="grid"))

print("\n### Wyniki testów PRNG: ###")
print("\nWygenerowane liczby PRNG:")
print(random_numbers_prng)
print(tabulate([
    ["Test Chi-kwadrat", f"χ²={chi2_prng:.2f}", f"p-value={p_value_prng:.4f}"],
    ["Test Serii", f"Liczba serii={runs_prng}", f"z-score={z_score_prng:.4f}"],
    ["Test Entropii", f"Entropia={ent_prng:.4f}", ""]
], headers=["Test", "Wynik 1", "Wynik 2"], tablefmt="grid"))

# Wykresy
def plot_histogram(data):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=10, color='blue', alpha=0.7, rwidth=0.85)
    plt.title("Histogram wygenerowanych liczb losowych")
    plt.xlabel("Zakres liczb")
    plt.ylabel("Częstość")
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def plot_chi_square(observed, bins):
    expected = [len(observed) / bins] * bins
    bin_edges = np.linspace(min(observed), max(observed), bins + 1)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    plt.figure(figsize=(10, 6))
    plt.bar(bin_centers, observed, width=(bin_edges[1] - bin_edges[0]), color='orange', alpha=0.7, label="Zaobserwowane")
    plt.plot(bin_centers, expected, 'r--', label="Oczekiwane")
    plt.title("Test Chi-kwadrat - porównanie zaobserwowanych i oczekiwanych wartości")
    plt.xlabel("Zakres liczb")
    plt.ylabel("Częstość")
    plt.legend()
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def plot_runs_test(bits):
    transitions = [bits[i] != bits[i - 1] for i in range(1, len(bits))]
    runs_positions = [i for i, t in enumerate(transitions) if t]

    plt.figure(figsize=(10, 6))
    plt.plot(range(len(bits)), bits, 'bo-', alpha=0.6, label="Bity")
    plt.vlines(runs_positions, ymin=0, ymax=1, colors='red', linestyles='dashed', label="Przejścia między seriami")
    plt.title("Test Serii - wizualizacja przejść między bitami")
    plt.xlabel("Indeks bitu")
    plt.ylabel("Wartość bitu")
    plt.legend()
    plt.grid(alpha=0.75)
    plt.show()

def plot_entropy(data):
    counts = Counter(data)
    labels, values = zip(*counts.items())
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='green', alpha=0.7)
    plt.title("Entropia - rozkład liczności wartości")
    plt.xlabel("Liczby")
    plt.ylabel("Częstość")
    plt.grid(axis='y', alpha=0.75)
    plt.show()

# Wizualizacja wyników
plot_histogram(random_numbers_qrng)

observed, _ = np.histogram(random_numbers_qrng, bins=8)
plot_chi_square(observed, bins=8)

plot_runs_test(random_bits_qrng)
plot_entropy(random_numbers_qrng)

# Porównanie wyników
plt.figure(figsize=(12, 6))
plt.hist(random_numbers_qrng, bins=10, alpha=0.6, color='green', label='QRNG')
plt.hist(random_numbers_prng, bins=10, alpha=0.6, color='blue', label='PRNG')
plt.title("Porównanie QRNG i PRNG")
plt.xlabel("Wartości liczbowe")
plt.ylabel("Częstość")
plt.legend()
plt.grid()
plt.show()
