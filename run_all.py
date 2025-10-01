from minixunit.testloader import TestLoader
from minixunit.testsuite import TestSuite
from minixunit.testrunner import TestRunner
from tests import test_case_test, test_suite_test, test_loader_test

if __name__ == "__main__":
    loader = TestLoader()

    test_case_suite = loader.make_suite(test_case_test.TestCaseTest)
    test_suite_suite = loader.make_suite(test_loader_test.TestLoaderTest)
    test_load_suite = loader.make_suite(test_suite_test.TestSuiteTest)

    suite = TestSuite()
    suite.add_test(test_case_suite)
    suite.add_test(test_suite_suite)
    suite.add_test(test_load_suite)

    runner = TestRunner()
    runner.run(suite)
