import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

def test_skew(stats_instance):
    assert stats_instance.skew([1, 2, 3, 4, 5]) == "Distribuição positiva"

def test_skew_lista_vazia(stats_instance):
    assert stats_instance.skew([]) == "Distribuição normal"

@pytest.mark.xfail
def test_skew_xfail(stats_instance):
    assert stats_instance.skew([1, 1, 1, 1, 1]) == "Distribuição normal"  # Isso falhará
