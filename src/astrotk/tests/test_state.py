""" test_state.py
"""
"""
Imports
"""
import pytest

from astrotk.bodies.bodies import Earth
from astrotk.tests.test_state_values import *
from astrotk.twobody.state import vector


def rounding_precision(expected):
    """
    Helper tool for ensuring all equations tested fairly according to given rounding precision.
    """
    return eval('10E-{}'.format(len(str(expected).split('.')[1]) + 1))


def test_rounding_precision():
    """
    Testing the helper tool for expected results.
    :return: None
    """
    assert 10E-4 == rounding_precision(1.00 + 10E-4)


"""
Test Case 1: State-vector International Space Station on June 12, 2014, 12:00:00 hrs [NASA, 2014]
"""
Test1ClassicalState = vector.VectorState(Earth, *Test1Vector)
Test1ClassicalState = Test1ClassicalState.to_classical()
Test1VectorState = Test1ClassicalState.to_vectors()


class Test1Vector2Classical(object):
    """
    Provided state-vector is converted to Classical and tested according to the values provided in AE4878 using pytest.
    [ae4-878: basics, slide 20]
    """

    def setup_method(self, method):
        print("\n%s:%s" % (type(self).__name__, method.__name__))

    def teardown_method(self, method):
        print("{} passed".format(method.__name__))
        pass

    def test_vector2classical_a(self):
        actual = Test1ClassicalState.a.si.value
        expect = Test1Classical[0].si.value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_e(self):
        actual = Test1ClassicalState.e.si.value
        expect = Test1Classical[1].si.value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_inc(self):
        actual = Test1ClassicalState.inc.to('deg').value
        expect = Test1Classical[2].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_raan(self):
        actual = Test1ClassicalState.raan.to('deg').value
        expect = Test1Classical[3].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_argp(self):
        actual = Test1ClassicalState.argp.to('deg').value
        expect = Test1Classical[4].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_theta(self):
        actual = Test1ClassicalState.theta.to('deg').value
        expect = Test1Classical[5].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_E(self):
        actual = Test1ClassicalState.E.to('deg').value
        expect = Test1Classical[6].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_M(self):
        actual = Test1ClassicalState.M.to('deg').value
        expect = Test1Classical[7].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual


class Test1Classical2Vector(object):
    """
    The resulting Classical state is transformed back to vector state in order to verify Classical orbital element
    conversion back to Cartesian vectors.
    """

    def setup_method(self, method):
        print("\n%s:%s" % (type(self).__name__, method.__name__))

    def teardown_method(self, method):
        print("{} passed".format(method.__name__))
        pass

    def test_classical2vector_r_vec(self):
        actual = Test1VectorState.r_vec.si.value
        expect = Test1Vector[0].si.value
        assert pytest.approx(expect, abs=rounding_precision(expect[0])) == actual

    def test_classical2vector_v_vec(self):
        actual = Test1VectorState.v_vec.si.value
        expect = Test1Vector[1].si.value
        assert pytest.approx(expect, abs=rounding_precision(expect[0])) == actual


"""
Test 2: State-vector Cryosat-2 on June 13, 2014, 14:59:21 hrs [NORAD, 2014]
"""
Test2ClassicalState = vector.VectorState(Earth, *Test2Vector).to_classical()
Test2VectorState = Test2ClassicalState.to_vectors()


class Test2Vector2Classical(object):
    """
    Provided state-vector is converted to Classical and tested according to the values provided in AE4878 using pytest.
    [ae4-878: basics, slide 21]
    """

    def setup_method(self, method):
        print("\n%s:%s" % (type(self).__name__, method.__name__))

    def teardown_method(self, method):
        print("{} passed".format(method.__name__))
        pass

    def test_vector2classical_a(self):
        actual = Test2ClassicalState.a.si.value
        expect = Test2Classical[0].si.value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_e(self):
        actual = Test2ClassicalState.e.si.value
        expect = Test2Classical[1].si.value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_inc(self):
        actual = Test2ClassicalState.inc.to('deg').value
        expect = Test2Classical[2].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_raan(self):
        actual = Test2ClassicalState.raan.to('deg').value
        expect = Test2Classical[3].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_argp(self):
        actual = Test2ClassicalState.argp.to('deg').value
        expect = Test2Classical[4].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_theta(self):
        actual = Test2ClassicalState.theta.to('deg').value
        expect = Test2Classical[5].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_E(self):
        actual = Test2ClassicalState.E.to('deg').value
        expect = Test2Classical[6].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual
        # TODO: Derive true reason for assert 239.5991 ± 1.0e-04 == 239.5992045452973 situation.

    def test_vector2classical_M(self):
        actual = Test2ClassicalState.M.to('deg').value
        expect = Test2Classical[7].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual


class Test2Classical2Vector(object):
    """
    The resulting Classical state is transformed back to vector state in order to verify Classical orbital element
    conversion back to Cartesian vectors.
    """

    def setup_method(self, method):
        print("\n%s:%s" % (type(self).__name__, method.__name__))

    def teardown_method(self, method):
        print("{} passed".format(method.__name__))
        pass

    def test_classical2vector_r_vec(self):
        actual = Test2VectorState.r_vec.si.value
        expect = Test2Vector[0].si.value
        assert pytest.approx(expect, abs=rounding_precision(expect[0])) == actual

    def test_classical2vector_v_vec(self):
        actual = Test2VectorState.v_vec.si.value
        expect = Test2Vector[1].si.value
        assert pytest.approx(expect, abs=rounding_precision(expect[0])) == actual


"""
Test 3: Curtis, H. Orbital mechanics for engineering students (p. 108).
"""
Test3ClassicalState = vector.VectorState(Earth, *Test3Vector).to_classical()
Test3VectorState = Test3ClassicalState.to_vectors()


class Test3Vector2Classical(object):
    """
    Provided state-vector is converted to Classical and tested according to the values provided in AE4878 using pytest.
    [ae4-878: basics, slide 21]
    """

    def setup_method(self, method):
        print("\n%s:%s" % (type(self).__name__, method.__name__))

    def teardown_method(self, method):
        print("{} passed".format(method.__name__))
        pass

    def test_vector2classical_a(self):
        actual = Test3ClassicalState.a.si.value
        expect = Test3Classical[0].si.value
        assert pytest.approx(expect, abs=10E2) == actual
        # TODO: Solve Curtis significant figures detection problem.

    def test_vector2classical_e(self):
        actual = Test3ClassicalState.e.si.value
        expect = Test3Classical[1].si.value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_inc(self):
        actual = Test3ClassicalState.inc.to('deg').value
        expect = Test3Classical[2].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_raan(self):
        actual = Test3ClassicalState.raan.to('deg').value
        expect = Test3Classical[3].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_argp(self):
        actual = Test3ClassicalState.argp.to('deg').value
        expect = Test3Classical[4].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual

    def test_vector2classical_theta(self):
        actual = Test3ClassicalState.theta.to('deg').value
        expect = Test3Classical[5].to('deg').value
        assert pytest.approx(expect, abs=rounding_precision(expect)) == actual


class Test3Classical2Vector(object):
    """
    The resulting Classical state is transformed back to vector state in order to verify Classical orbital element
    conversion back to Cartesian vectors.
    """

    def setup_method(self, method):
        print("\n%s:%s" % (type(self).__name__, method.__name__))

    def teardown_method(self, method):
        print("{} passed".format(method.__name__))
        pass

    def test_classical2vector_r_vec(self):
        actual = Test3VectorState.r_vec.si.value
        expect = Test3Vector[0].si.value
        assert pytest.approx(expect, abs=rounding_precision(expect[0])) == actual

    def test_classical2vector_v_vec(self):
        actual = Test3VectorState.v_vec.si.value
        expect = Test3Vector[1].si.value
        assert pytest.approx(expect, abs=rounding_precision(expect[0])) == actual
