from easy_api.tests import *

class TestApiUserController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='api_user', action='index'))
        # Test response...
