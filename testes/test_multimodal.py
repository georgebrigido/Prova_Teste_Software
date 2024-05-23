import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

def test_multimodal(stats_instance):
    assert stats_instance.multimodal([1, 2, 2, 3, 3, 3, 4, 4, 5]) == [3]

def test_multimodal_lista_vazia(stats_instance):
    assert stats_instance.multimodal([]) == "Não é multimodal"

@pytest.mark.xfail
def test_multimodal_xfail(stats_instance):
    assert stats_instance.multimodal([1, 2, 3, 4, 5]) == [1]  # Isso falhará
