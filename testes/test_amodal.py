import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

def test_amodal(stats_instance):
    assert stats_instance.amodal([1, 2, 3, 4, 5]) == "Existe moda"

def test_amodal_lista_vazia(stats_instance):
    assert stats_instance.amodal([]) == "Não existe moda"

@pytest.mark.xfail
def test_amodal_xfail(stats_instance):
    assert stats_instance.amodal([1, 1, 1, 2, 3, 4, 5]) == "Existe moda"  # Isso falhará
