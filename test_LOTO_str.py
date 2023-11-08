import pytest
from LOTO_str_ import Lotto, C_to_c, C_to_i

@pytest.fixture
def lotto_instance():
    karta = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    rand_90 = [6, 3, 12, 42, 7, 15, 2, 9, 1, 5, 14, 13, 4, 11, 8, 10, ...]  # Дополните значения
    poz1 = [1, 3, 2, 4, 0]  # Дополните значения
    poz2 = [0, 4, 2, 1, 3]  # Дополните значения
    return Lotto(karta, rand_90, poz1, poz2)

def test_def_karta(lotto_instance):
    karta = lotto_instance.def_karta()
    assert len(karta) == 15
    assert all(1 <= val <= 90 for val in karta)

def test_do_replace_c(lotto_instance):
    karta = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    karta, num_x = lotto_instance.do_replace_c(karta, 5)
    assert 'X' in karta  # Проверка, что 'X' есть в списке
    assert num_x == 1

def test_c_to_c_play_cc():
    c_to_c = C_to_c()
    result = c_to_c.play_cc()

    assert isinstance(result, str)  # Проверка, что результат - это строка

    expected_results = ["Выиграл Комп # 1", "Выиграл Комп # 2"]  # Исправлено на "Выиграл Комп # 1"
    assert result in expected_results  # Проверка, что результат содержит одну из ожидаемых фраз

