def matrix_product(p):
    """Return m and s.

    m[i][j] is the minimum number of scalar multiplications needed to compute the
    product of matrices A(i), A(i + 1), ..., A(j).

    s[i][j] is the index of the matrix after which the product is split in an
    optimal parenthesization of the matrix product.

    p[0... n] is a list such that matrix A(i) has dimensions p[i - 1] x p[i].
    """
    length = len(p) # len(p) = number of matrices + 1

    # m[i][j] is the minimum number of multiplications needed to compute the
    # product of matrices A(i), A(i+1), ..., A(j)
    # s[i][j] is the matrix after which the product is split in the minimum
    # number of multiplications needed
    m = [[-1]*length for _ in range(length)]
    s = [[-1]*length for _ in range(length)]

    for i in range(1, length):
        m[i][i] = 0

    for chain_length in range(2, length):
        for start in range(1, length - chain_length + 1):
            end = start + chain_length - 1
            q = float('inf')
            for k in range(start, end):
                temp = m[start][k] + m[k + 1][end] + p[start - 1]*p[k]*p[end]
                if temp < q:
                    q = temp
                    s[start][end] = k
            m[start][end] = q

    return m, s


def print_parenthesization(s, start, end):
    """Print the optimal parenthesization of the matrix product A(start) x
    A(start + 1) x ... x A(end).

    s[i][j] is the index of the matrix after which the product is split in an
    optimal parenthesization of the matrix product.
    """
    if start == end:
        print('A[{}]'.format(start), end='')
        return

    k = s[start][end]

    print('(', end='')
    print_parenthesization(s, start, k)
    print_parenthesization(s, k + 1, end)
    print(')', end='')


n = int(input('Enter number of matrices: '))
p = []
for i in range(n):
    temp = int(input('Enter number of rows in matrix {}: '.format(i + 1)))
    p.append(temp)
temp = int(input('Enter number of columns in matrix {}: '.format(n)))
p.append(temp)

m, s = matrix_product(p)
print('The number of scalar multiplications needed:', m[1][n])
print('Optimal parenthesization: ', end='')
print_parenthesization(s, 1, n)