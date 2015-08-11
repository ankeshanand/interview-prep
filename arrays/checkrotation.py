BASE_PRIME = 101

def check_rotation(a1, a2):
    """
    Check wheather a2 is a rotation of a1.
    """
    if len(a1) != len(a2):
        return False

    double_a2 = a2 + a2
    if is_subarray(a1, double_a2):
        return True
    return False


def rabin_fingerprint(a):
    hash = 0

    for index, degree in enumerate(reversed(xrange(0, len(a)))):
        hash += a[index] * (BASE_PRIME ** degree)

    return hash


def is_subarray(a1, a2):
    """
    Check wheather a1 is a subarray of a2.
    """
    if len(a2) < len(a1):
        return False

    hash_a1 = rabin_fingerprint(a1)
    degree = len(a1) - 1

    for i in xrange(0, len(a2)-len(a1)+1):
        if i == 0:
            hash_current = rabin_fingerprint(a2[:len(a1)])
        else:
            hash_current = BASE_PRIME * (
                    hash_current - (a2[i-1] * (BASE_PRIME ** degree))
                    ) + a2[i+len(a1)-1]

        if hash_a1 == hash_current and a1 == a2[i:i+len(a1)]:
            return True

    return False


A1 = [1, 2, 3, 5, 6, 7, 8]
A2 = [5, 6, 7, 8, 1, 2, 3]

print check_rotation(A1, A2)
