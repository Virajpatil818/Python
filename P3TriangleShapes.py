def print_triangle(n):
for i in range(n):
print("* " * (i + 1))
def print_right_triangle(n):
for i in range(n):
print(" " * (n - i - 1) + "*" * (i + 1))
def print_isosceles_triangle(n):
for i in range(n):
print(" " * (n - i - 1) + "*" * (2 * i + 1))
def print_equilateral_triangle(n):
for i in range(n):
print("* " * n)
def print_pascals_triangle(n):
for i in range(n):
for j in range(i + 1):
print(binom(i, j), end=" ")
print()
def binom(n, k):
if k == 0 or k == n:
return 1
else:
return binom(n - 1, k - 1) + binom(n - 1, k)
def main():
n = int(input("Enter the number of rows: "))
print("Printing a triangle...")
print_triangle(n)
print("Printing a right triangle...")
print_right_triangle(n)
print("Printing an isosceles triangle...")
print_isosceles_triangle(n)
print("Printing an equilateral triangle...")
print_equilateral_triangle(n)
print("Printing Pascal's triangle...")
print_pascals_triangle(n)
if __name__ == "__main__":
main()
