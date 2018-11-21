if __name__ == "__main__":
    # Imports ---------------------------------------------------------------------------------------------------------#
    from astrotk.AE4878.bodies import Earth
    from astrotk.twobody.state import vector
    from astrotk.twobody.state import classical
    from astrotk.tests.test_state_values import *

    # Test 1 ----------------------------------------------------------------------------------------------------------#
    # Test1ClassicalState = vector.VectorState(Earth(), *Test1Vector).to_classical()
    #
    # Test1ClassicalState.prettyprint()
    #
    # M_test = Test1ClassicalState.M
    #
    # Tata = classical.ClassicalState(Earth(), Test1ClassicalState.a, Test1ClassicalState.e, Test1ClassicalState.inc, Test1ClassicalState.raan, Test1ClassicalState.argp, M=Test1Classical[-1])
    #
    # Tata.prettyprint()
    #
    # Test1ClassicalState.to_spherical().prettyprint()
    #
    # Test1VectorState = Test1ClassicalState.to_vectors()
    #
    # TestISS = classical.ClassicalState(attractor=Earth(),
    #                                    a=(408 + 2 * 6378 + 408)/2 * u.km,
    #                                    e=0.0005141 * u.dimensionless_unscaled,
    #                                    inc=51.6375 * u.deg,
    #                                    raan=319.5570 * u.deg,
    #                                    argp=64.6272 * u.deg,
    #                                    M=-53.32196822163303 * u.rad)

    # TestISS.to_vectors().prettyprint()
    # TestISS.to_classical().prettyprint()
    #
    # TestISS = TestISS.to_spherical()
    # TestISS.to_vectors().prettyprint()

    from astrotk.tests.test_state_values import Test1Classical
    # print(Test1Classical)
    # print(Test1Classical[:-3])
    Kev_test = classical.ClassicalState(Earth(),
                                        *Test1Classical[:-3],
                                        M=Test1Classical[-1])

    print(vars(Kev_test))

