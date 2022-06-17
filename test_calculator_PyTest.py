import pytest

from calculator import calculator
# def test_plus(self):
#     self.assertEqual(calculator('2+2'), 4)
# Сравни насколько легче это пишеться в PyTest :
def test_plus():
    assert calculator('2+2') == 4

# def test_no_signs(self):
#     with self.assertRaises(ValueError) as e:
#         calculator('abracadabra')
#     self.assertEqual('Выражение должно содержать хотябы один знак (+-/*) !!!', e.exception.args[0])
# это же в PyTest :
def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('abracadabra')
    assert 'Выражение должно содержать хотябы один знак (+-/*) !!!' == error.value.args[0]

def test_two_signs():
    with pytest.raises(ValueError) as error:
        calculator('2+2+2')
    assert 'Выражение должно содержать 2 целых числа и 1 знак !!!' == error.value.args[0]

if __name__ == '__main__':
    pytest.main()
