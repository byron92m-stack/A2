import pytest
from polynomials import Polynomial


def test_print():
    p = Polynomial([2, 1, 0, 3])
    assert str(p) == "3x^3 + x + 2"


def test_equality():
    assert Polynomial((0, 1)) == Polynomial((0, 1))


@pytest.mark.parametrize(
    "a, b, sum",
    (
        ((0,), (0, 1), (0, 1)),
        ((2, 0, 3), (1, 2), (3, 2, 3)),
        ((4, 2), (10, 2, 4), (14, 4, 4)),
    ),
)
def test_add(a, b, sum):
    assert Polynomial(a) + Polynomial(b) == Polynomial(sum)


def test_add_scalar():
    assert Polynomial((2, 1)) + 3 == Polynomial((5, 1))


def test_reverse_add_scalar():
    assert 3 + Polynomial((2, 1)) == Polynomial((5, 1))


def test_add_unknown():
    with pytest.raises(TypeError):
        Polynomial((1,)) + "frog"

# ---------- Tests de degree ----------

def test_degree_constante():
    assert Polynomial((5,)).degree() == 0


def test_degree_lineal():
    assert Polynomial((1, 2)).degree() == 1


def test_degree_cubico():
    assert Polynomial((1, 2, 3, 4)).degree() == 3


def test_degree_ignora_ceros_lideres():
    assert Polynomial((1, 2, 0)).degree() == 1
    assert Polynomial((1, 2, 0, 0)).degree() == 1


def test_degree_polinomio_cero():
    assert Polynomial((0,)).degree() == 0
    assert Polynomial((0, 0, 0)).degree() == 0


# ---------- Tests de suma con ceros líderes ----------

def test_add_con_ceros_lideres():
    # (1 + 2x + 0x²) + (3 + 4x) → 4 + 6x
    result = Polynomial((1, 2, 0)) + Polynomial((3, 4))
    assert result == Polynomial((4, 6))


def test_add_simetria():
    # a + b == b + a  (conmutatividad)
    a = Polynomial((1, 2, 0))
    b = Polynomial((3, 4))
    assert a + b == b + a