from support.assertion_errors import AssertionErrors
class Assertions:
    @staticmethod
    def check_equal(actual_result, expected_result):
        assert actual_result == expected_result, AssertionErrors.EQUAL_ERROR.format(expected_result, actual_result)