from nose.plugins.skip import SkipTest
from nose.tools import nottest


def test_skip_plugin():
    raise SkipTest


@nottest
def test_not_a_test():
    pass
