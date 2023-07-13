from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait

class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get('https://www.united.com/es/us')

        iniciar_sesion = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[2]/header/div/div/div[1]/div/div/div/div[2]/nav/ul/li[3]/div/div/div/div/div[1]/div/button/span')
        iniciar_sesion.click()
        time.sleep(2)

        nombre = driver.find_element(By.CSS_SELECTOR, '.app-components-Form-Input-styles__input--VLE8M')
        nombre.send_keys('YAA54130')
        time.sleep(2)

        password = driver.find_element(By.CSS_SELECTOR, '.app-components-Form-Input-styles__input--VLE8M[type="password"]')
        password.send_keys('Chesterkira05')
        time.sleep(2)

        boton = driver.find_element(By.CSS_SELECTOR, 'button.app-components-Button-styles__button--LbfHO.app-components-Button-styles__fullWidth--3s3MI.app-components-Button-styles__tertiary--20H47.app-components-Button-styles__contained--2kXyi.app-containers-LoginFormContainer-styles__signInButton--XrlfZ.app-containers-LoginFormContainer-styles__btnDefault--3e0qK')
        boton.click()
        time.sleep(30)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()