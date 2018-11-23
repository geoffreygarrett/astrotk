if __name__ == "__main__":
    # Imports ---------------------------------------------------------------------------------------------------------#
    from astrotk.AE4878.bodies import Earth
    from astrotk.twobody.state import vector
    from astrotk.twobody.state import classical
    from astrotk.tests.test_state_values import *

    # Test 1 ----------------------------------------------------------------------------------------------------------#
    from astrotk.tests.test_state_values import Test1Classical, Test1Vector, Test2Vector
    # Kev_test = classical.ClassicalState(Earth(),
    #                                     *Test2Classical[:-2])
    #
    # print(Kev_test.to_vectors().latex())
    ta = vector.VectorState(Earth(),
                            *Test2Vector)
    #
    print(ta.latex(10))
    print(ta.to_classical().latex(10))
    # print(ta.E.to(u.deg))
    # print(ta.M.to(u.deg))
    # ta = Kev_test.to_vectors()
    # test = test.to_classical()

