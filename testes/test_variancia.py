import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

def test_variancia(stats_instance):
    assert stats_instance.variancia([1, 2, 3, 4, 5]) == 2.5

def test_variancia_lista_vazia(stats_instance):
    assert stats_instance.variancia([]) == 0

@pytest.mark.xfail
def test_variancia_xfail(stats_instance):
    assert stats_instance.variancia([1, 2, 3, 4, 5]) == 0  # Isso falhará
