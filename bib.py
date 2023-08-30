def elevado(vetor: list[int], valor: int) -> list[int]:
    for c in range(len(vetor)):
        vetor[c] = ((vetor[c] ** c) + (valor ** 2))
    return vetor
