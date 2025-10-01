from minixunit.testloader import TestLoader
from minixunit.testsuite import TestSuite
from tests.stubs import TestStub, TestSpy
from minixunit.testcase import TestCase

class TestLoaderTest(TestCase):

    def test_create_suite(self):
        loader = TestLoader()
        suite = loader.make_suite(TestStub)
        self.assert_equal(len(suite.tests), 3)

    def test_create_suite_of_suites(self):
        loader = TestLoader()
        stub_suite = loader.make_suite(TestStub)
        spy_suite = loader.make_suite(TestSpy)
        suite = TestSuite()
        suite.add_test(stub_suite)
        suite.add_test(spy_suite)
        self.assert_equal(len(suite.tests), 2)

    def test_get_multiple_test_case_names(self):
        loader = TestLoader()
        names = loader.get_test_case_names(TestStub)
        self.assert_equal(names, ['test_error', 'test_failure', 'test_success'])

    def test_get_no_test_case_names(self):
        class Test(TestCase):
            def foobar(self):
                pass
        loader = TestLoader()
        names = loader.get_test_case_names(Test)
        self.assert_equal(names, [])
