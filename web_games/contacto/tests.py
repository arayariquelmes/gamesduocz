from django.test import TestCase
from .forms import ContactForm
# Create your tests here.
class ContactoTestCase(TestCase):

    #Se ejecuta una vez antes de cada test
    def setUp(self):
        pass

    def test_formOk(self):
        formulario = ContactForm(data={'nombre':'Seba Araya', 'correo':'test@asd.cl', 'mensaje':'Hola mundo'})
        self.assertTrue(formulario.is_valid())
    def test_nombreNok(self):
        formulario = ContactForm(data={'nombre':'', 'correo':'test@asd.cl', 'mensaje':'Hola mundo'})
        self.assertIn('nombre', formulario.errors.keys())
    #Hacer pruebas de email
    # Email valido
    # Email incorrecto
    # Email no entregado
    # Email ok
    #Hacer pruebas del mensaje
    #Mensaje exita
    #Mensaje no exita
    #Largo del mensaje es correcto
    #Menos del largo del mensaje
    #Mas del largo del mensaje
    #Hacer Pruebas de nombre
    #Nombre entregado
    #Nombre no entregado
    #Nombre con largo menor al correcto
    #Nombre con largo mayor al correcto
    #Se ejecuta una vez despues de cada test
    def tearDown(self):
        pass