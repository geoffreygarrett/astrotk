if __name__ == "__main__":
    # Imports ---------------------------------------------------------------------------------------------------------#
    from astrotk.AE4878.bodies import Earth
    from astrotk.twobody.state import vector
    from astrotk.twobody.state import classical
    from astrotk.tests.test_state_values import *

    # Test 1 ----------------------------------------------------------------------------------------------------------#
    from astrotk.tests.test_state_values import Test1Classical
    Kev_test = classical.ClassicalState(Earth(),
                                        *Test1Classical[:-3],
                                        M=Test1Classical[-1])

    test = Kev_test.to_vectors()
    test = test.to_classical()
    print(test.latex(10))

