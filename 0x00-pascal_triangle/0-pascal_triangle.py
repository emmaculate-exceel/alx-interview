#!/usr/bin/python3
""" A script for pascal's triangle for any possible number or digit"""


def pascal_triangle(n):
    """
    list of integers
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize with the first row
    
    for i in range(1, n):
        prev_row = triangle[i - 1]
        curr_row = [1]  # Start each row with 1
        
        for j in range(1, i):
            curr_row.append(prev_row[j - 1] + prev_row[j])
        
        curr_row.append(1)  # End each row with 1
        triangle.append(curr_row)
    
    return triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

# Example usage:
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)
