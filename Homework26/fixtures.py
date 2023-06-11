import pytest
from Homework26.api_tests_configs import TestConfigs


@pytest.fixture
def api_test_configs():
    yield TestConfigs()
