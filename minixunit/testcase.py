class TestCase:
    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self, result):
        result.test_started()
        try:
            self.set_up()
            test_method = getattr(self, self.test_method_name)
            try:
                test_method()
            except AssertionError:
                result.add_failure(self.test_method_name)
            except Exception:
                result.add_error(self.test_method_name)
            finally:
                self.tear_down()
        except Exception:
            result.add_error(self.test_method_name)
            try:
                self.tear_down()
            except Exception:
                pass

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def assert_equal(self, first, second):
        if first != second:
            msg = f'{first} != {second}'
            raise AssertionError(msg)

    def assert_true(self, expr):
        if not expr:
            msg = f'{expr} is not true'
            raise AssertionError(msg)

    def assert_false(self, expr):
        if expr:
            msg = f'{expr} is not false'
            raise AssertionError(msg)

    def assert_in(self, member, container):
        if member not in container:
            msg = f'{member} not found in {container}'
            raise AssertionError(msg)
