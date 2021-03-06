from utils import SeleniumTestCase
from fuauth.models import User


class LoginTest(SeleniumTestCase):

    def test_successful_login(self):
        password = 'testpants'
        user = User.objects.create_user('Melanie', '6192222222', User.ATT, User.HAWAII, email='test@gmail.com', password=password)
        self.browser.get(self.live_server_url + "/login/")
        self.browser.find_element_by_name('username').send_keys(user.email)
        self.browser.find_element_by_name('password').send_keys(password)
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector('*[type=submit]').click()
        text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Hi ' + user.name + ".", text)
