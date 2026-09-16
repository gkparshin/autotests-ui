import pytest

SYSTEM_VERSION = "v1.2.0"

@pytest.mark.skipif(SYSTEM_VERSION == "v1.3.0", reason="Тест не может быть запущен на версии системы v1.3.0")
def test_system_version_valid():
    pass

@pytest.mark.skipif(SYSTEM_VERSION == "v1.2.0", reason="Тест не может быть запущен на версии системы v1.2.0")
def test_system_version_invalid():
    pass

# @pytest.mark.skip(reason="Фича в разработке")
# class TestSuiteSkip:
#     def test_feature_in_development_1(self):
#         pass
#
#     def test_feature_in_development_2(self):
#         pass