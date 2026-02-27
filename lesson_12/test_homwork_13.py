import os.path
import  unittest
from Homework_13_1 import log_event

class TestLogWork(unittest.TestCase):

    def setUp(self):
        open('login_system.log', 'w').close()

    def test_log_success(self):
        log_event('Alex', 'success')

        with open('login_system.log', 'r') as  f:
            lines = f.readlines()
            last_lines = lines[-1]

        self.assertIn("Username: Alex", last_lines)
        self.assertIn("Status: success", last_lines)


    def test_log_expired(self):
        log_event('Anton', 'expired')
        with open('login_system.log', 'r') as  f:
            lines = f.readlines()
            last_lines = lines[-1]

        self.assertIn("Username: Anton", last_lines)
        self.assertIn("Status: expired", last_lines)

    def test_log_failed(self):
        log_event('Ivan', 'failed')
        with open('login_system.log', 'r') as  f:
            lines = f.readlines()
            last_lines = lines[-1]

            self.assertIn("Username: Ivan", last_lines)
            self.assertIn("Status: failed", last_lines)



if __name__ == '__main__':
    unittest.main()