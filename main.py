from typing import List

def even_list(int_list: List[int]) -> List[int]:
    return [num for num in int_list if num % 2 == 0]

def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    return sum(num**2 for num in even_int_list)

def main():
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

if __name__ == "__main__":
    main()
