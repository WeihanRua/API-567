from homework_04a import Github
import unittest

class TestGithub(unittest.TestCase):
    def test_Github(self):
        self.assertEqual(Github('WeihanRua'), ['Repo: 567-assignment-week1  Number of commits: 2', 'Repo: API-567  Number of commits: 9', 'Repo: HW10  Number of commits: 2', 'Repo: Trangle567  Number of commits: 7'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
