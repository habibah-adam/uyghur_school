import unittest
from school_app import create_app, db

class TestHome(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()
    
    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        db.create_all()
        cls.app_context.pop()

    def register(self, username, email, password, confirm):
        return self.client.post('/register', data=dict(
            username=username,
            email=email,
            password=password,
            confirm=confirm
        ), follow_redirects=True)
    
    def test_register(self):
        data = self.register("admin", "admin@mail.com", "password", "password")
        self.assertEqual(data.status_code, 200)

    def login(self, username, password):
        return self.client.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        data = self.login('admin', 'admin')
        self.assertEqual(data.status_code, 200)

        data = self.logout()
        self.assertEqual(data.status_code, 200)
        

    def test_home(self):
        response = self.client.get("/home")
        self.assertEqual(response.status_code, 200)

    def test_blog(self):
        response = self.client.get("/blog")
        self.assertEqual(response.status_code, 200)
