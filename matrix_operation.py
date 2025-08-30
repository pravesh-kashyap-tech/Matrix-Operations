import numpy as np

def get_matrix_input(matrix_num):
    rows = int(input(f"Enter number of rows for Matrix {matrix_num}: "))
    cols = int(input(f"Enter number of columns for Matrix {matrix_num}: "))
    
    print(f"Enter elements for Matrix {matrix_num} (row-wise):")
    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        while len(row) != cols:
            print(f"Expected {cols} elements, got {len(row)}. Please re-enter row {i+1}.")
            row = list(map(float, input(f"Row {i+1}: ").split()))
        elements.append(row)
        
    return np.array(elements)

def display_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    for row in matrix:
        formatted_row = ' '.join(
            f"{int(val):>5}" if val == int(val) else f"{val:>5.2f}"
            for val in row
        )
        print(f"|{formatted_row} |")

def matrix_addition(m1, m2):
    if m1.shape != m2.shape:
        return "Addition not possible: Matrices must be of the same dimensions."
    return m1 + m2

def matrix_subtraction(m1, m2):
    if m1.shape != m2.shape:
        return "Subtraction not possible: Matrices must be of the same dimensions."
    return m1 - m2

def matrix_multiplication(m1, m2):
    if m1.shape[1] != m2.shape[0]:
        return "Multiplication not possible: Columns of Matrix 1 must equal rows of Matrix 2."
    return np.dot(m1, m2)

def matrix_transpose(m):
    return m.T

def matrix_determinant(m):
    if m.shape[0] != m.shape[1]:
        return "Determinant not possible: Matrix must be square."
    return np.linalg.det(m)

def main():
    print("=== Matrix Operations Tool ===")
    
    m1 = get_matrix_input(1)
    m2 = get_matrix_input(2)

    display_matrix(m1, "Matrix 1")
    display_matrix(m2, "Matrix 2")

    while True:
        print("\nChoose an operation:")
        print("1. Add Matrices")
        print("2. Subtract Matrices (Matrix1 - Matrix2)")
        print("3. Multiply Matrices (Matrix1 x Matrix2)")
        print("4. Transpose Matrix")
        print("5. Determinant of a Matrix")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            result = matrix_addition(m1, m2)
            if isinstance(result, str):
                print(result)
            else:
                display_matrix(result, "Result (Addition)")
        elif choice == '2':
            result = matrix_subtraction(m1, m2)
            if isinstance(result, str):
                print(result)
            else:
                display_matrix(result, "Result (Subtraction)")
        elif choice == '3':
            result = matrix_multiplication(m1, m2)
            if isinstance(result, str):
                print(result)
            else:
                display_matrix(result, "Result (Multiplication)")
        elif choice == '4':
            sub_choice = input("Transpose which matrix? (1 or 2): ")
            if sub_choice == '1':
                result = matrix_transpose(m1)
                display_matrix(result, "Transpose of Matrix 1")
            elif sub_choice == '2':
                result = matrix_transpose(m2)
                display_matrix(result, "Transpose of Matrix 2")
            else:
                print("Invalid choice.")
        elif choice == '5':
            sub_choice = input("Determinant of which matrix? (1 or 2): ")
            if sub_choice == '1':
                result = matrix_determinant(m1)
                print(f"Determinant of Matrix 1: {result:.2f}")
            elif sub_choice == '2':
                result = matrix_determinant(m2)
                print(f"Determinant of Matrix 2: {result:.2f}")
            else:
                print("Invalid choice.")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    main()
