__author__ = 'asistente'

#from __future__ import absolute_import

from unittest import TestCase
from selenium import webdriver

from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('BuscoAyuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Betzy')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Montanez')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('7')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3135555555')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('ba.montanez@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:\chromedriver\developer.jpg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('ba.montanez')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('prueba123')

        spanIf = self.browser.find_element(By.XPATH, '//span[text()="Betzy Montanez"]')

        if( (self.assertIn('Betzy Montanez',  spanIf.text ))==False ):
            botonGrabar = self.browser.find_element_by_id('id_grabar')
            botonGrabar.click()


        span = self.browser.find_element(By.XPATH, '//span[text()="Betzy Montanez"]')

        self.assertIn('Betzy Montanez', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Betzy Montanez"]')
        span.click()
        self.browser.implicitly_wait(3)
        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Betzy Montanez"]')

        self.assertIn('Betzy Montanez', h2.text)

    def test_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        nombreUsuario = self.browser.find_element_by_id('username')
        nombreUsuario.send_keys('ba.montanez')

        clave = self.browser.find_element_by_id('password')
        clave.send_keys('prueba123')

        botonIngresar = self.browser.find_element_by_id('id_ingresar')
        botonIngresar.click()

        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()=" Logout"]')

        self.assertIn('Logout', span.text)
