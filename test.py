import pytest
import sumaABigualC

@pytest.mark.parametrize("w", [
"abcc", 
"aabccc", 
"aaabcccc",
"aaabbccccc"
])
def test_acepta(w):
    assert sumaABigualC.evaluar(w)

@pytest.mark.parametrize("w", [
"aa#",
"#aa",
"a#aaaa",
"aaa#a",
"hola"
])
def test_rechaza(w):
    assert not sumaABigualC.evaluar(w)
