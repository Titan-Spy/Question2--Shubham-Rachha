def count_elements_greater_than_k(H, k):
    """Counts the elements in the list H that are greater than k."""

    c = 0
    for j in range(len(H)):
        if H[j] > k:
            c += 1
    return c

# Example usage:
if __name__ == "__main__":
    for i in range(int(input())):
        n, k = map(int, input().split())
        H = list(map(int, input().split(" ")))
        result = count_elements_greater_than_k(H, k)
        print(result)
