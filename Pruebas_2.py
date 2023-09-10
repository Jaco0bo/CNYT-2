import unittest
import numpy as np
import vec_and_mat


class Test_vec_and_mat_functions(unittest.TestCase):

    def test_adicion_v(self):
        # v1 = [(8 + 2i),(9 + 2i)]
        # v2 = [(5 - 2i),(-6 - 6i)]
        # v1 + v2 = [(13+0i),(3-4i)]
        v1 = [8 + 2j, 9 + 2j]
        v2 = [5 - 2j, -6 - 6j]
        resultado = vec_and_mat.adicion_v(v1, v2)
        resultado_esperado = [13 + 0j, 3 - 4j]
        for i in range(len(resultado)):
            self.assertEqual(resultado[i], resultado_esperado[i])

        # v1 = [(2 + 2.2i),(3.1 + 2.5i)]
        # v2 = [(5 - 2i),(-6 - 6i)]
        # v1 + v2 = [(7+0.2i),(-2.9-3.5i)]
        v1 = [2 + 2.2j, 3.1 + 2.5j]
        v2 = [5 - 2j, -6 - 6j]
        resultado = vec_and_mat.adicion_v(v1, v2)
        resultado_esperado = [7 + 0.2j, -2.9 - 3.5j]
        for i in range(len(resultado)):
            self.assertAlmostEquals(resultado[i], resultado_esperado[i])

    def test_inverso_avs(self):
        # v1 = [(8 + 2i),(9 + 2i)]
        # v2 = [(5 - 2i),(-6 - 6i)]
        # v1 + v2 = [(13+0i),(3-4i)]
        v1 = [8 + 2j, 9 + 2j]
        v2 = [5 - 2j, -6 - 6j]
        resultado = vec_and_mat.inverso_av(v1, v2)
        resultado_esperado = [3 + 4j, 15 + 8j]
        for i in range(len(resultado)):
            self.assertEqual(resultado[i], resultado_esperado[i])

        # v1 = [(2 + 2.2i),(3.1 + 2.5i)]
        # v2 = [(5 - 2i),(-6 - 6i)]
        # v1 + v2 = [(7+0.2i),(-2.9-3.5i)]
        v1 = [2 + 2.2j, 3.1 + 2.5j]
        v2 = [5 - 2j, -6 - 6j]
        resultado = vec_and_mat.inverso_av(v1, v2)
        resultado_esperado = [-3 + 4.2j, 9.1 + 8.5j]
        for i in range(len(resultado)):
            self.assertAlmostEquals(resultado[i], resultado_esperado[i])

    def test_vec_esc(self):
        # v1 = [(8 + 2i),(9 + 2i)]
        # a = 3
        # a * v1 = [24 + 6j, 27 + 6j]
        v1 = [8 + 2j, 9 + 2j]
        a = 3
        resultado = vec_and_mat.vect_esc(v1, a)
        resultado_esperado = [24 + 6j, 27 + 6j]
        for i in range(len(resultado)):
            self.assertEqual(resultado[i], resultado_esperado[i])

        # v1 = [(2 + 2.2i),(3.1 + 2.5i)]
        # a = -8
        # a * v1 = [-16 - 17.6j, -24.8 - 20j]
        v1 = [2 + 2.2j, 3.1 + 2.5j]
        a = -8
        resultado = vec_and_mat.vect_esc(v1, a)
        resultado_esperado = [-16 - 17.6j, -24.8 - 20j]
        for i in range(len(resultado)):
            self.assertEqual(resultado[i], resultado_esperado[i])

    def test_adicion_m(self):
        # m1 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # m2 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # m1 + m2 = [[16 + 4j, 18 + 4j], [10 - 4j, -12 - 12j]]
        m1 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        m2 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        resultado = vec_and_mat.adicion_m(m1, m2)
        resultado_esperado = np.array([[16 + 4j, 18 + 4j], [10 - 4j, -12 - 12j]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

        # m1 = [[3 + 9j, -2.2 + 2j], [3 + 1j, -5 + 5j]]
        # m2 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # m1 + m2 = [[11 + 11j, 6.8 + 4j], [8 - 1j, -11 - 1j]]
        m1 = np.array([[3 + 9j, -2.2 + 2j], [3 + 1j, -5 + 5j]])
        m2 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        resultado = vec_and_mat.adicion_m(m1, m2)
        resultado_esperado = np.array([[11 + 11j, 6.8 + 4j], [8 - 1j, -11 - 1j]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

    def test_resta_m(self):
        # m1 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # m2 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # m1 - m2 = [[0, 0], [0, 0]]
        m1 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        m2 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        resultado = vec_and_mat.resta_m(m1, m2)
        resultado_esperado = np.array([[0, 0], [0, 0]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

        # m1 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # m2 = [[-8 - 2j, -9 - 2j], [-5 + 2j, 6 + 6j]]
        # m1 - m2 = [[16 + 4j, 18 + 4j], [10 - 4j, -12 - 12j]]
        m1 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        m2 = np.array([[-8 - 2j, -9 - 2j], [-5 + 2j, 6 + 6j]])
        resultado = vec_and_mat.resta_m(m1, m2)
        resultado_esperado = np.array([[16 + 4j, 18 + 4j], [10 - 4j, -12 - 12j]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

    def test_esc_matco(self):
        # m1 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # a = -3
        # m1 * a = [[-24 - 6j, -27 - 6j], [-15 + 6j, 18 + 18j]]
        m1 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        a = -3
        resultado = vec_and_mat.esc_matco(m1, a)
        resultado_esperado = np.array([[-24 - 6j, -27 - 6j], [-15 + 6j, 18 + 18j]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

        # m1 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # a = 0
        # m1 * a = [[0, 0], [0, 0]]
        m1 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        a = 0
        resultado = vec_and_mat.esc_matco(m1, a)
        resultado_esperado = np.array([[0, 0], [0, 0]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

    def test_transpuesta(self):
        # m1 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # transpuesta de m1 = [[8 + 2j, 5 - 2j], [9 + 2j, -6 - 6j]]
        m1 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        resultado = vec_and_mat.transpuesta(m1)
        resultado_esperado = np.array([[8 + 2j, 5 - 2j], [9 + 2j, -6 - 6j]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

        # m1 = [[8 + 2j, 9 + 2j, 4 - 4j], [5 - 2j, -6 - 6j, 1 + 2j],
        # [5 + 6j, 3 + 3j, 4 - 2j]]

        # transpuesta de m1 = [[8 + 2j, 5 - 2j, 5 + 6j], [9 + 2j, -6 - 6j, 3 + 3j],
        # [4 - 4j, 1 + 2j, 4 - 2j]]
        m1 = np.array([[8 + 2j, 9 + 2j, 4 - 4j], [5 - 2j, -6 - 6j, 1 + 2j],
                       [5 + 6j, 3 + 3j, 4 - 2j]])
        resultado = vec_and_mat.transpuesta(m1)
        resultado_esperado = np.array([[8 + 2j, 5 - 2j, 5 + 6j], [9 + 2j, -6 - 6j, 3 + 3j],
                                       [4 - 4j, 1 + 2j, 4 - 2j]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

    def test_conjugada(self):
        # m1 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # conjugada de m1 = [[8 - 2j, 9 - 2j], [5 + 2j, -6 + 6j]]
        m1 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        resultado = vec_and_mat.conjugada(m1)
        resultado_esperado = np.array([[8 - 2j, 9 - 2j], [5 + 2j, -6 + 6j]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

        # m1 = [[8 + 2j, 9 + 2j, 4 - 4j], [5 - 2j, -6 - 6j, 1 + 2j],
        # [5 + 6j, 3 + 3j, 4 - 2j]]

        # conjugada de m1 = [[8 - 2j, 9 - 2j, 4 + 4j], [5 + 2j, -6 + 6j, 1 - 2j],
        # [5 - 6j, 3 - 3j, 4 + 2j]]
        m1 = np.array([[8 + 2j, 9 + 2j, 4 - 4j], [5 - 2j, -6 - 6j, 1 + 2j],
                       [5 + 6j, 3 + 3j, 4 - 2j]])
        resultado = vec_and_mat.conjugada(m1)
        resultado_esperado = np.array([[8 - 2j, 9 - 2j, 4 + 4j], [5 + 2j, -6 + 6j, 1 - 2j],
                                       [5 - 6j, 3 - 3j, 4 + 2j]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

    def test_adjunta(self):
        # m1 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # adjunta de m1 = [[8 - 2j, 5 + 2j], [9 - 2j, -6 + 6j]]
        m1 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        resultado = vec_and_mat.adjunta(m1)
        resultado_esperado = np.array([[8 - 2j, 5 + 2j], [9 - 2j, -6 + 6j]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

        # m1 = [[8 + 2j, 9 + 2j, 4 - 4j], [5 - 2j, -6 - 6j, 1 + 2j],
        # [5 + 6j, 3 + 3j, 4 - 2j]]

        # adjunta de m1 = [[8 - 2j, 9 - 2j, 4 + 4j], [5 + 2j, -6 + 6j, 1 - 2j],
        # [5 - 6j, 3 - 3j, 4 + 2j]]
        m1 = np.array([[8 + 2j, 9 + 2j, 4 - 4j], [5 - 2j, -6 - 6j, 1 + 2j],
                       [5 + 6j, 3 + 3j, 4 - 2j]])
        resultado = vec_and_mat.adjunta(m1)
        resultado_esperado = np.array([[8 - 2j, 5 + 2j, 5 - 6j], [9 - 2j, -6 + 6j, 3 - 3j],
                                       [4 + 4j, 1 - 2j, 4 + 2j]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

    def test_prod_cmat(self):
        # m1 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # m2 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # m1 * m2 = [[109 + 24j, 26 - 32j], [2 - 24j, 49 + 64j]]
        m1 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        m2 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        resultado = vec_and_mat.prod_cmat(m1, m2)
        resultado_esperado = np.array([[109 + 24j, 26 - 32j], [2 - 24j, 49 + 64j]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

        # m1 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # m2 = [[-8 - 2j, -9 - 2j], [-5 + 2j, 6 + 6j]]
        # m1 * m2 = [[-109 - 24j, -26 + 32j], [-2 + 24j, -49 - 64j]]
        m1 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        m2 = np.array([[-8 - 2j, -9 - 2j], [-5 + 2j, 6 + 6j]])
        resultado = vec_and_mat.prod_cmat(m1, m2)
        resultado_esperado = np.array([[-109 - 24j, -26 + 32j], [-2 + 24j, -49 - 64j]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

    def test_accion_mv(self):
        # m1 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # v1 = [8 + 2j, 9 + 2j]
        # m1 * v1 = [137 + 68j, 2 - 72j]
        m1 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        v1 = np.array([8 + 2j, 9 + 2j])
        resultado = vec_and_mat.accion_mv(m1, v1)
        resultado_esperado = np.array([137 + 68j, 2 - 72j])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

        # m1 = [[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]]
        # v1 = [5 - 12j, -9 + 10j]
        # m1 * v1 = [-37 - 14j, 115 - 76j]
        m1 = np.array([[8 + 2j, 9 + 2j], [5 - 2j, -6 - 6j]])
        v1 = np.array([5 - 12j, -9 + 10j])
        resultado = vec_and_mat.accion_mv(m1, v1)
        resultado_esperado = np.array([-37 - 14j, 115 - 76j])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

    def test_prod_int(self):
        # v1 = [1, 2 - 3j, 0 + 6j]
        # v2 = [0, 0 + 1j, 2 + 4j]
        # (v1, v2) = [21 - 10j]
        v1 = np.array([1, 2 - 3j, 0 + 6j])
        v2 = np.array([0, 0 + 1j, 2 + 4j])
        resultado = vec_and_mat.prod_int(v1, v2)
        resultado_esperado = np.array([21 - 10j])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

        # v1 = [0 + 2j, 12 - 3j, 1 + 6j]
        # v2 = [0, 0 + 1j, 2 + 4j]
        # (v1, v2) = [23 + 4j]
        v1 = np.array([0 + 2j, 12 - 3j, 1 + 6j])
        v2 = np.array([0, 0 + 1j, 2 + 4j])
        resultado = vec_and_mat.prod_int(v1, v2)
        resultado_esperado = np.array([23 + 4j])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

    def test_norma_v(self):
        # v1 = [4 + 3j, 6 - 4j, 12 - 7j, 0 + 13j]
        # |v1| = 20.95
        v1 = np.array([4 + 3j, 6 - 4j, 12 - 7j, 0 + 13j])
        resultado = vec_and_mat.norma_v(v1)
        resultado_esperado = np.array(20.95)
        self.assertTrue(np.allclose(resultado, resultado_esperado))

        # v1 = [4 + 3j, 8 + 14j]
        # |v1| = 16.88
        v1 = np.array([4 + 3j, 8 + 14j])
        resultado = vec_and_mat.norma_v(v1)
        resultado_esperado = np.array(16.88)
        self.assertTrue(np.allclose(resultado, resultado_esperado))

    def test_dist_v(self):
        # v1 = [0 + 2j, 3 + 0j, 12 - 7j, 0 + 4j]
        # v2 = [0 + 1j, -3 + 0j, 0 - 5j]
        # d(v1, v2) = 10.86
        v1 = np.array([0 + 2j, 3 + 0j, 0 + 4j])
        v2 = np.array([0 + 1j, -3 + 0j, 0 - 5j])
        resultado = vec_and_mat.dist_v(v1, v2)
        resultado_esperado = np.array(10.86)
        self.assertTrue(np.allclose(resultado, resultado_esperado))

        # v1 = [0 + 2j, 3 + 0j, 12 - 7j, 0 + 4j]
        # v2 = [4 + 10j, 5 + 2j, 2 - 5j]
        # d(v1, v2) = 13.15
        v1 = np.array([0 + 2j, 3 + 0j, 0 + 4j])
        v2 = np.array([4 + 10j, 5 + 2j, 2 - 5j])
        resultado = vec_and_mat.dist_v(v1, v2)
        resultado_esperado = np.array(13.15)
        self.assertTrue(np.allclose(resultado, resultado_esperado))

    def test_val_and_vec(self):
        # matriz = [[1 + 2j, 3 + 3j], [2, 1 + 4j]]
        # valores propios = ([-1.53+1.81j,  3.53+4.19j])
        # vectores propios = [[ 0.86+0.j, 0.79+0.j], [-0.39+0.34j, 0.62-0.05j]]
        m1 = np.array([[1 + 2j, 3 + 3j], [2, 1 + 4j]])
        eigenvalues, eigenvectors = np.linalg.eig(m1)
        eigenvalues = np.round(eigenvalues, 2)
        eigenvectors = np.round(eigenvectors, 2)
        resultado_esperado_valores = np.array([-1.53 + 1.81j, 3.53 + 4.19j])
        resultado_esperado_vectores = np.array([[0.86 + 0.j, 0.79 + 0.j],
                                                [-0.39 + 0.34j, 0.62 - 0.05j]])

        self.assertTrue(np.allclose(eigenvalues, resultado_esperado_valores))
        self.assertTrue(np.allclose(eigenvectors, resultado_esperado_vectores))

        # matriz = [[4 + 1j, 2 + 1j], [0, 3 - 4j]]
        # valores propios = ([4 + 1j, 3 - 4j])
        # vectores propios = [[1 + 0j, -0.25 + 0.32j], [0 + 0j, 0.92 - 0j]]
        m1 = np.array([[4 + 1j, 2 + 1j], [0, 3 - 4j]])
        eigenvalues, eigenvectors = np.linalg.eig(m1)
        eigenvalues = np.round(eigenvalues, 2)
        eigenvectors = np.round(eigenvectors, 2)
        resultado_esperado_valores = np.array([4 + 1j, 3 - 4j])
        resultado_esperado_vectores = np.array([[1 + 0j, -0.25 + 0.32j],
                                                [0 + 0j, 0.92 - 0j]])

        self.assertTrue(np.allclose(eigenvalues, resultado_esperado_valores))
        self.assertTrue(np.allclose(eigenvectors, resultado_esperado_vectores))

    def test_matriz_u(self):
        # m1 = [[4 + 1j, 2 + 1j], [0, 3 - 4j]]
        # False
        m1 = np.array([[4 + 1j, 2 + 1j], [0, 3 - 4j]])
        resultado = vec_and_mat.matriz_u(m1)
        resultado_esperado = False
        self.assertEqual(resultado, resultado_esperado)

        # m1 = [[1, 0], [0, 1]]
        # True
        m1 = np.array([[1, 0], [0, 1]])
        resultado = vec_and_mat.matriz_u(m1)
        resultado_esperado = True
        self.assertEqual(resultado, resultado_esperado)

    def test_matriz_herm(self):
        # m1 = [[4 + 1j, 2 + 1j], [0, 3 - 4j]]
        # False
        m1 = np.array([[4 + 1j, 2 + 1j], [0, 3 - 4j]])
        resultado = vec_and_mat.matriz_herm(m1)
        resultado_esperado = False
        self.assertEqual(resultado, resultado_esperado)

        # m1 = [[7, 6+5j], [6-5j, -3]]
        # True
        m1 = np.array([[7, 6 + 5j], [6 - 5j, -3]])
        resultado = vec_and_mat.matriz_herm(m1)
        resultado_esperado = True
        self.assertEqual(resultado, resultado_esperado)

    def test_prd_ten(self):
        # v1 = [2 + 0j, 0 + 3j]
        # v2 = [0 + 4j, -5 + 2j, -8 + 0j]
        # v1 x v2 = [[0 + 8j, -10 + 4j, -16 + 0j], [-12 + 0j, -6 - 15j, 0 - 24j]]
        v1 = np.array([2 + 0j, 0 + 3j])
        v2 = np.array([0 + 4j, -5 + 2j, -8 + 0j])
        resultado = vec_and_mat.prd_ten(v1, v2)
        resultado_esperado = np.array([[0 + 8j, -10 + 4j, -16 + 0j], [-12 + 0j,
                                                                      -6 - 15j, 0 - 24j]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))

        # m1 = [[2 + 0j, 0 + 3j], [2 + 4j, 3 - 3j]]
        # v2 = [0 + 4j]
        # m1 x v2 = [[[0 + 8j], [-12 + 0j]], [[-16 + 8j], [12 + 12j]]]

        m1 = np.array([[2 + 0j, 0 + 3j], [2 + 4j, 3 - 3j]])
        v2 = np.array([0 + 4j])
        resultado = vec_and_mat.prd_ten(m1, v2)
        resultado_esperado = np.array([[[0 + 8j], [-12 + 0j]],
                                       [[-16 + 8j], [12 + 12j]]])
        self.assertTrue(np.allclose(resultado, resultado_esperado))


if __name__ == '__main__':
    unittest.main()
