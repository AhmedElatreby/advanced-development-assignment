# Advanced development assignment

## Ahmed El-Atreby

### Unit test


- test register page

```
class FlaskTestCase(unittest.TestCase):
    def test_register(self):
        tester = app.test_client(self)
        response = tester.get("/register", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Sign Up" in response.data)
```

- test login page

```
    def test_login(self):
        tester = app.test_client(self)
        response = tester.get("login", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Sign In" in response.data)
```


- test about page

```
    def test_about(self):
        tester = app.test_client(self)
        response = tester.get("/about", content_type="html/text")
        self.assertEqual(response.status_code, 200)
```


- test correct login page

```
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            "/login",
            data=dict(username="a@a.com", password="123456"),
            follow_redirects=True,
        )
        self.assertIn(b"H", response.data)
```
- test create profile page

```
    def test_create_profile(self):
        tester = app.test_client(self)
        response = tester.get("/form", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Create and add your profile here" in response.data)
```
- test item page page

```
    def test_item_page(self):
        tester = app.test_client(self)
        response = tester.get("/items/single/123456", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"2 seater" in response.data)
```
- test logout page

```
    def test_logout(self):
        tester = app.test_client(self)
        tester.post(
            "/login",
            data=dict(username="a@a.com", password="123456"),
            follow_redirects=True,
        )
        response = tester.get("/logout", follow_redirects=True)
        self.assertIn(b"", response.data)

```