# Programa: término n-ésimo y suma de n términos de una PA

a1 = float(input("Ingresa el primer término (a1): "))
d = float(input("Ingresa la diferencia (d): "))
n = int(input("Ingresa el número de términos (n): "))

# Programa: término n-ésimo de una progresión geométrica

a1 = float(input("Ingresa el primer término (a1): "))
r = float(input("Ingresa la razón (r): "))
n = int(input("Ingresa el número de término que quieres (n): "))

an = a1 * (r ** (n - 1))

print("El término número", n, "de la progresión geométrica es:", an)