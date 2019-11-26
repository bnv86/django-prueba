import unittest
from shopping_cart import Item, ShoppingCart, NotExistsItemError

API_VERSION = 17

#pruebas unitarias
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
        self.assertEqual(self.pan.name, "Pan") #compara dos valores (==)
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

    def test_obtener_producto_pan(self):
        item = self.shopping_cart.get_item(self.pan)
        self.assertIs(item, self.pan) #compara dos objetos (is)
        self.assertIsNot(item, self.jugo)
        print("8")

    def test_excepcion_al_obtener_jugo(self):
        with self.assertRaises(NotExistsItemError):
            self.shopping_cart.get_item(self.jugo)
            print("9")

    #operadores relacionales
    def test_total_con_un_producto(self):
        total = self.shopping_cart.total()
        self.assertGreater(total, 0)
        self.assertLess(total, self.pan.price + 1.0)
        self.assertEqual(total, self.pan.price)
        print("10")

    #assertRegex
    def test_codigo_pan(self):
        self.assertRegex(self.pan.code(), self.pan.name)

    #validar de forma manual si una prueba es exitosa o no
    def test_fail(self):
        if 3 > 2:
            self.fail("Dos no es mayor a tres!")

    #Conocemos si que la prueba no va a ejecutarse
    #@unittest.skip("Colocamos nuestros motivos")

    #Desconocemos si la prueba puede o no ejecutarse
    #@unittest.skipIf(True , "Coloramos nuestros motivos")
    #@unittest.skipIf(API_VERSION < 18 , "Version obsoleta")
    @unittest.skipUnless(False, "Colocamos nuestros motivos") #pasa ok si el resultado del bool o comparacion es falso 
    def test_prueba_skip(self):
        pass


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