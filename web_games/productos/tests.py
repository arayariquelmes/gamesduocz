from django.test import TestCase
from .models import Producto
# Create your tests here.

class ProductosTestCase(TestCase):

    def setUp(self):
        self.productoEnOferta  = Producto.objects.create(titulo="Test Oferta", precio=2000, estaEnOferta= True)
        self.productoNoOferta = Producto.objects.create(titulo="Test No Oferta", precio=2000,estaEnOferta= False)
    
    #Aqui hare el test de la creacion de un producto
    def test_createProducto(self):
        productoTest = Producto.objects.create(titulo="Test",precio=1000, estaEnOferta=True)
        #productosTestFiltro = Producto.objects.filter(titulo="Test")
        #self.assertEqual(len(productosTestFiltro),1)
        self.assertIsNotNone(productoTest.pk)

    def test_productoSinOferta(self):
        productos = Producto.objects.filter(estaEnOferta=False)
        self.assertEqual(self.productoNoOferta.titulo, productos[0].titulo)
    
    def test_productoConOferta(self):
        productos = Producto.objects.filter(estaEnOferta=True)
        self.assertEqual(len(productos), 1)
        self.assertEqual(self.productoEnOferta.titulo, productos[0].titulo)

