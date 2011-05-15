from easy_api.tests import *

class TestRequestController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='request', action='index'))
        # Test response...
