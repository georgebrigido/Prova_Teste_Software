import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

@pytest.mark.parametrize("dados, resultado_esperado", [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4], 2.5),
    ([10, 20, 30, 40, 50], 30),
])
def test_mediana(dados, resultado_esperado, stats_instance):
    assert stats_instance.mediana(dados) == resultado_esperado

def test_mediana_lista_vazia(stats_instance):
    assert stats_instance.mediana([]) == 0

@pytest.mark.xfail
def test_mediana_xfail(stats_instance):
    assert stats_instance.mediana([1, 2, 3, 4, 5]) == 0  # Isso falhará
