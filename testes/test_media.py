import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

@pytest.mark.parametrize("dados, resultado_esperado", [
    ([1, 2, 3, 4, 5], 3),
    ([10, 20, 30, 40, 50], 30),
])
def test_media(dados, resultado_esperado, stats_instance):
    assert stats_instance.media(dados) == resultado_esperado

def test_media_lista_vazia(stats_instance):
    assert stats_instance.media([]) == 0

@pytest.mark.xfail
def test_media_xfail(stats_instance):
    assert stats_instance.media([1, 2, 3, 4, 5]) == 0  # Isso falhará
