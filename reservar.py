from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_reservar(self):
        driver = self.driver
        driver.get('https://www.united.com/es/es')

        desde = driver.find_element(By.XPATH, '//*[@id="bookFlightOriginInput"]')
        desde.click()
        boton = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[3]/div[2]/div/div[1]/div/main/section/div/div/div[1]/div/div/div[2]/section[1]/div/div/div[2]/form/div[2]/div/div[1]/div/div/div[1]/div/div/button')
        boton.click()
        desde.send_keys('Managua')
        time.sleep(2)

        opcion = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[3]/div[2]/div/div[1]/div/main/section/div/div/div[1]/div/div/div[2]/section[1]/div/div/div[2]/form/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div/ul/li[2]/button')
        opcion.click()
        time.sleep(3)

        hacia = driver.find_element(By.XPATH, '//*[@id="bookFlightDestinationInput"]')
        hacia.click()
        hacia.send_keys('Miami')
        time.sleep(3)

        opcion1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[3]/div[2]/div/div[1]/div/main/section/div/div/div[1]/div/div/div[2]/section[1]/div/div/div[2]/form/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/ul/li[3]/button')
        opcion1.click()
        time.sleep(3)

        fecha_salida = driver.find_element(By.XPATH, '//*[@id="DepartDate"]')
        fecha_salida.click()
        delete_fecha = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[3]/div[2]/div/div[1]/div/main/section/div/div/div[1]/div/div/div[2]/section[1]/div/div/div[2]/form/div[3]/div[1]/div/button')
        delete_fecha.click()
        time.sleep(3)
        fecha_salida.click()
        time.sleep(2)
        
        elegir_salida = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[3]/div[2]/div/div[1]/div/main/section/div/div/div[1]/div/div/div[2]/section[1]/div/div/div[2]/form/div[3]/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[4]')
        elegir_salida.click()
        time.sleep(2)

        elegir_vuelta = driver.find_element(By.XPATH, '//*[@id="ReturnDate"]')
        elegir_vuelta.click()
        time.sleep(2)
        elegir_vuelta2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[3]/div[2]/div/div[1]/div/main/section/div/div/div[1]/div/div/div[2]/section[1]/div/div/div[2]/form/div[3]/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[3]/div/table/tbody/tr[1]/td[2]')
        elegir_vuelta2.click()
        time.sleep(2)

        driver.execute_script("window.scrollBy(0, 200);")

        buscar_vuelos = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[3]/div[2]/div/div[1]/div/main/section/div/div/div[1]/div/div/div[2]/section[1]/div/div/div[2]/form/div[5]/div/div[1]/div/div/div[2]/button[1]')
        buscar_vuelos.click()
        time.sleep(8)

        precio = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div/div/div[3]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/button/div[1]/div[3]')
        precio.click()
        time.sleep(4)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()