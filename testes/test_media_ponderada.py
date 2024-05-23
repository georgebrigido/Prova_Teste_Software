import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats_instance():
    return StatsN2()

@pytest.mark.parametrize("data, weights, expected_result", [
    ([1, 2, 3, 4, 5], [1, 1, 1, 1, 1], 3),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 3.6666666666666665),
])
def test_media_ponderada(data, weights, expected_result, stats_instance):
    assert stats_instance.media_ponderada(data, weights) == expected_result
