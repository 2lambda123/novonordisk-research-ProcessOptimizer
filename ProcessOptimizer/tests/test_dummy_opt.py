import pytest

from ProcessOptimizer import dummy_minimize
from ProcessOptimizer.model_systems.benchmarks import bench1
from ProcessOptimizer.model_systems.benchmarks import bench2
from ProcessOptimizer.model_systems.benchmarks import bench3


def check_minimize(func, y_opt, dimensions, margin, n_calls):
    r = dummy_minimize(func, dimensions, n_calls=n_calls, random_state=1)
    assert r.fun < y_opt + margin


@pytest.mark.slow_test
def test_dummy_minimize():
    check_minimize(bench1, 0., [(-2.0, 2.0)], 0.05, 100)
    check_minimize(bench2, -5, [(-6.0, 6.0)], 0.05, 100)
    check_minimize(bench3, -0.9, [(-2.0, 2.0)], 0.05, 100)
