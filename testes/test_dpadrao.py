import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

def test_dpadrao(stats_instance):
    assert stats_instance.dpadrao(2.5) == 1.5811388300841898

@pytest.mark.xfail
def test_dpadrao_xfail(stats_instance):
    assert stats_instance.dpadrao(2.5) == 0  # Isso falhará
