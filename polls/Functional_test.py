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
        nombre.send_keys('Rafael')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Medrano')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('7')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3135555555')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('re.medrano@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:\chromedriver\developer.jpg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('re.medrano')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('prueba123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)

        span = self.browser.find_element(By.XPATH, '//span[text()="Rafael Medrano"]')
        self.assertIn('Rafael Medrano', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Betzy Editado Montanez Editado"]')
        span.click()
        self.browser.implicitly_wait(3)
        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Betzy Editado Montanez Editado"]')

        self.assertIn('Betzy Editado Montanez Editado', h2.text)

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


    def test_Editar(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        nombreUsuario = self.browser.find_element_by_id('username')
        nombreUsuario.send_keys('ba.montanez')

        claveIngreso = self.browser.find_element_by_id('password')
        claveIngreso.send_keys('prueba123')

        botonIngresar = self.browser.find_element_by_id('id_ingresar')
        botonIngresar.click()

        self.browser.implicitly_wait(3)

        linkEditar = self.browser.find_element_by_id('id_editar')
        linkEditar.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear()
        nombre.send_keys('Betzy Editado')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.clear()
        apellidos.send_keys('Montanez Editado')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.clear()
        experiencia.send_keys('10')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.clear()
        telefono.send_keys('313555666')

        correo = self.browser.find_element_by_id('id_correo')
        correo.clear()
        correo.send_keys('ba.montanez01@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:\chromedriver\developer.jpg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.clear()
        nombreUsuario.send_keys('ba.montanez2')

        clave = self.browser.find_element_by_id('id_password')
        clave.clear()
        clave.send_keys('prueba1234')

        botonGrabar = self.browser.find_element_by_id('id_editar')
        botonGrabar.click()

        self.browser.implicitly_wait(3)

        span = self.browser.find_element(By.XPATH, '//span[text()="Betzy Editado Montanez Editado"]')
        self.assertIn('Betzy Editado Montanez Editado', span.text)

    def test_Comentar(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Betzy Editado Montanez Editado"]')
        span.click()
        self.browser.implicitly_wait(3)
        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Betzy Editado Montanez Editado"]')

        correo = self.browser.find_element_by_id('correo')
        correo.send_keys('prueba@prueba.com')

        comentario = self.browser.find_element_by_id('comentario')
        comentario.send_keys('Comentario Prueba')

        botonAceptar = self.browser.find_element_by_id('id_comentar')
        botonAceptar.click()
        self.browser.implicitly_wait(6)

        span = self.browser.find_element(By.XPATH, '//p[text()="Comentario Prueba"]')
        self.assertIn('Comentario Prueba', span.text)
