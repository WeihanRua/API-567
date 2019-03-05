from homework_04a import Github
import unittest
from unittest import mock


class TestGithub(unittest.TestCase):
    @mock.patch('urllib.request.urlopen')
    def test_Github(self, mock_return):
        mock_return.side_effect = [
            '[{"name" : "567"}, {"name" : "API-567"}]',
            '[{"1" : "rua"}, {"2" : "rua"}]',
            '[{"1" : "rua"}, {"2" : "rua"}, {"3" : "rua"}]'
        ]
        self.assertEqual(Github('WeihanRua'), ['Repo: 567  Number of commits: 2', 'Repo: API-567  Number of commits: 3'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
