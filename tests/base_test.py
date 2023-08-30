from datetime import datetime
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:
    def generate_random_email_with_timestamp(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "testing_"+timestamp+"@gmail.com"