import numpy as np


def is_reflexive(R):
    stack = 0
    for i in range(len(R)):
        if R[i][i] == 1:
            stack += 1
        else:
            pass
    if stack == len(R):
        return True
    else:
        return False


def is_symmetric(R):
    R_T = R.T
    return np.array_equal(R_T, R)


def is_transitive(R):
    lst = []
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j] == 1:
                lst.append([i, j])

    stack = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][1] == lst[j][0]:
                arr = [lst[i][0], lst[j][1]]
                print(lst[i], lst[j], "/", arr)
                if arr in lst and lst[i] not in stack:
                    stack.append(lst[i])
                else:
                    pass
            else:
                pass
    print(stack)
    print(lst)
    if stack == lst:
        return True
    else:
        return False


def main():
    R = np.array([[1, 0, 1, 0, 1],
                  [0, 1, 0, 1, 0],
                  [1, 0, 1, 0, 1],
                  [0, 1, 0, 1, 0],
                  [1, 0, 1, 0, 1]])
    
    ref = is_reflexive(R)
    sym = is_symmetric(R)
    trans = is_transitive(R)
    print(ref, sym, trans)
    if ref is True and sym is True and trans is True:
        print(f"R is equivalence!")
    else:
        print(f"R is not equivalence.")

    return 0


if __name__ == "__main__":
    main()