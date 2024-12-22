import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_post_success(self):
        response = self.app.post('/add', data=dict(title='Test Title', content='Test Content'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Title', response.data)
        self.assertIn(b'Test Content', response.data)

    def test_add_post_failure(self):
        response = self.app.post('/add', data=dict(title='', content=''), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Title and Content cannot be empty', response.data)

if __name__ == '__main__':
    unittest.main()