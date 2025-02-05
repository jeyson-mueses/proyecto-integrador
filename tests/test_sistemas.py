import pytest
import numpy as np
from core.sistemas import resolver_sistema

def test_resolver_sistema():
    matriz = np.array([[2, -1, 3], [1, 1, -2], [3, -2, 1]])
    vector = np.array([5, -3, 2])
    resultado = resolver_sistema(matriz, vector)
    
    assert isinstance(resultado, list)
    assert len(resultado) == 3
