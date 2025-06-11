# verificarea valorii cu TVA a unui produs
## daca valoarea e < 50k atunci tva = 5%
### daca valoarea e peste 50k atunci tva = 19%

def suma_cu_tva(valoare):
    if valoare <= 50_000:
        return valoare + valoare * 5 / 100
    return valoare + valoare * 19 / 100

def test_calcul_tva():
    assert suma_cu_tva(10_000) == 10_500, "TVA este de 5%"
    assert suma_cu_tva(100) == 105, "TVA este de 5%"
    assert suma_cu_tva(100_000) == 119_000, "TVA este de 19%"
    assert suma_cu_tva(50_000) == 52_500, "TVA este de 5%"

test_calcul_tva()

