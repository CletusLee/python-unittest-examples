from nose.tools import with_setup

global_a, global_b = 0, 0


def setup_func():
    global global_a, global_b
    global_a, global_b = 1, 1


def teardown_func():
    pass

# note that with_setup is useful only for test functions, not for test methods
# in unittest.TestCase subclasses or other test classes.


@with_setup(setup_func, teardown_func)
def test_fixture():
    assert global_a + global_b == 2

#--------------------------------------
# nose supports test functions and methods that are generators.
# the following test case will generate five test results


def test_evens():
    for i in range(0, 5):
        yield check_even, i


def check_even(n):
    assert n < 5

# We can put with_setup on the method test_events, then the setup and teardown
# functions will only be executed once. If we instead put the functions on the
# method check_even, then setup and teardown functions will be executed five
# times.
