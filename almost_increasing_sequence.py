seq = [1, 2, 3, 4]


def validar_sequencia(sequencia: list[int]) -> bool:
    for c in range(1, len(sequencia)):
        if sequencia[c - 1] != (sequencia[c] - 1) or (sequencia[c - 1]) > (sequencia[c] + 1):
            return False
    return True


print(validar_sequencia(seq))
