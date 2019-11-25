import unittest
from shopping_cart import Item, ShoppingCart

class TestShoppingCart(unittest.TestCase):

    #se ejecuta antes de cada prueba unitaria
    def setUp(self):
        #print("Metodo setUp antes de la prueba")
        self.pan = Item("Pan", 7.0)
        self.jugo = Item("Jugo", 5.0)
        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)

    #se ejecuta despues de cada prueba unitaria
    def tearDown(self):
        #print("Metodo tearDown despues de la prueba")
        pass


    def test_cinco_mas_cinco_igual_diez(self):
        assert 5 + 5 == 10
        print("1")

    #test para setUp
    def test_nombre_producto_igual_pan(self):
        #item = Item("Manzana", 12.0)
        #palabra reservada assert o un metodo de la clase TestCase
        self.assertEqual(self.pan.name, "Pan")
        print("4")

    #test para setUp
    def test_nombre_producto_diferente_manzana(self):
        #item = Item("Pan blanco", 15.0)
        #palabra reservada assert o un metodo de la clase TestCase
        self.assertNotEqual(self.jugo.name, "Manzana") #diferente a manzana
        print("5")

    def test_contiene_productos(self):
        self.assertTrue(self.shopping_cart.contains_items())
        print("6")

    def test_no_contiene_productos(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains_items())
        print("7")

if __name__ == '__main__':
    unittest.main()

"""
    def test_nombre_producto_igual_manzana(self):
        item = Item("Manzana", 12.0)
        print("2")
        self.assertEqual(item.name, "Manzana")
        
    def test_nombre_producto_diferente_manzana(self):
        item = Item("Pan blanco", 15.0)
        self.assertNotEqual(item.name, "Manzana") #diferente a manzana
        print("3")
"""