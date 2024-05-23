import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

@pytest.fixture
def dados_exemplo():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def dados_multimodal():
    return [1, 2, 2, 3, 3, 3, 4, 4, 5]

@pytest.fixture
def dados_unimodal():
    return [1, 1, 1, 2, 3, 4, 5]

@pytest.fixture
def dados_amodal():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def pesos():
    return [1, 2, 3, 4, 5]
