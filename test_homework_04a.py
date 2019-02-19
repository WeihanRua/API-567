from homework_04a import Github
import unittest

class TestGithub(unittest.TestCase):
    def test_Github(self):
        self.assertEqual(Github('richkempinski'), ['Repo: hellogitworld  Number of commits: 30', 'Repo: helloworld  Number of commits: 6', 'Repo: Mocks  Number of commits: 9', 'Repo: Project1  Number of commits: 2', 'Repo: threads-of-life  Number of commits: 1'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
