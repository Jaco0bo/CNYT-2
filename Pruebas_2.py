import unittest
import vec_and_mat

class Test_vec_and_mat_functions(unittest.TestCase):

    def test_adicion(self):
        # (2 + 3i) + (4 + i)
        # 6 + 4i
        c1 = [['6', '2'], ['3', '1']]
        resultado = vec_and_mat.adicion_vect(c1)
        resultado_esperado = complex(9, 3)
        self.assertEqual(resultado, resultado_esperado)


if __name__ == '__main__':
    unittest.main()