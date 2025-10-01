from minixunit.testcase import TestCase
from minixunit.testresult import TestResult
from tests.stubs import TestStub, TestSpy

class TestCaseTest(TestCase):

    def set_up(self):
        self.result = TestResult()

    def test_result_success_run(self):
        stub = TestStub('test_success')
        stub.run(self.result)
        self.assert_equal(self.result.summary(), '1 run, 0 failed, 0 error')

    def test_result_failure_run(self):
        stub = TestStub('test_failure')
        stub.run(self.result)
        self.assert_equal(self.result.summary(), '1 run, 1 failed, 0 error')

    def test_result_error_run(self):
        stub = TestStub('test_error')
        stub.run(self.result)
        self.assert_equal(self.result.summary(), '1 run, 0 failed, 1 error')

    def test_result_multiple_run(self):
        stub = TestStub('test_success')
        stub.run(self.result)
        stub = TestStub('test_failure')
        stub.run(self.result)
        stub = TestStub('test_error')
        stub.run(self.result)
        self.assert_equal(self.result.summary(), '3 run, 1 failed, 1 error')

    def test_was_set_up(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_true(spy.was_set_up)

    def test_was_run(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_true(spy.was_run)

    def test_was_tear_down(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_true(spy.was_tear_down)

    def test_template_method(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_equal(spy.log, "set_up test_method tear_down")
