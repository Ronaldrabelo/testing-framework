from minixunit.testsuite import TestSuite
from minixunit.testresult import TestResult
from tests.stubs import TestStub
from minixunit.testcase import TestCase

class TestSuiteTest(TestCase):
    def test_suite_size(self):
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        suite.add_test(TestStub('test_error'))
        self.assert_equal(len(suite.tests), 3)

    def test_suite_success_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.run(result)
        self.assert_equal(result.summary(), '1 run, 0 failed, 0 error')

    def test_suite_multiple_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        suite.add_test(TestStub('test_error'))
        suite.run(result)
        self.assert_equal(result.summary(), '3 run, 1 failed, 1 error')
