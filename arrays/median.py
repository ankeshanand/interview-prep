from quickselect import quickselect


def median(A):
    return quickselect(A, (len(A) - 1) / 2)

if __name__ == "__main__":
    A = [3, 1, 1, 2, 6, 0]
    med = median(A)
    print med
