from app import app
from unittest import TestCase

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']



class SuperheroAppTestCase(TestCase):

    def setUp(self):
        print("inside set up")

    def tearDown(self):
        print("inside tear down")

    def test_home_page(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('WELCOME TO HERO HQ!', html)

    
    def test_search_page(self):
        with app.test_client() as client:
            res = client.get('/search')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('Enter Hero Name Below', html)
            
    def test_login_page(self):
        with app.test_client() as client:
            res = client.get('/login')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('Login', html)

    def test_unauthenticated_favorite(self):
        with app.test_client() as client:
            res = client.post('/favorites/add', data={"hero_id": 1})
        
            self.assertEqual(res.status_code, 302)
            self.assertIn('/login', res.location)


    def test_nonexistent_hero_page(self):
        with app.test_client() as client:
            res = client.get('/heroes/9999')  
            self.assertEqual(res.status_code, 404)
              

    

    