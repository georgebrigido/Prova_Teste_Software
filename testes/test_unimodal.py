import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

def test_unimodal(stats_instance):
    assert stats_instance.unimodal([1, 1, 1, 2, 3, 4, 5]) == 1

def test_unimodal_lista_vazia(stats_instance):
    assert stats_instance.unimodal([]) == "Não é unimodal"

@pytest.mark.xfail
def test_unimodal_xfail(stats_instance):
    assert stats_instance.unimodal([1, 2, 3, 4, 5]) == 0  # Isso falhará
