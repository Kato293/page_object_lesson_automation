from Pages.main_page import MainPage
from Pages.base_page import BasePage

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPageLocators(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open ()
        page.should_be_login_url()
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage ( browser,link )  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open ()
        page.should_be_login_form()
        #
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage ( browser,link )  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open ()
        should_be_register_form()
        # реализуйте проверку, что есть форма регистрации на странице
        assert True