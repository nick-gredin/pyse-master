from pyse import Pyse, TestCase, TestRunner, Services


class NickTest(TestCase, Services):

    @classmethod
    def setUpClass(cls):
        """ Setting browser driver, Using chrome by default."""
        cls.driver = Pyse("chrome")
        cls.timeout = 15  # You can customize timeout time
        cls.driver.maximize_window()

    """
    A simple test
    """

    def test_case_0001_adding_item_into_cart(self):
        """ Nick test"""
        self.open("http://automationpractice.com/index.php")
        Services.verify_cart_is_impty(self)
        Services.click_button(self, "Women", "tabButton")
        Services.click_plus_button_to_expand_category(self, "Tops")
        Services.click_plus_button_to_expand_category(self, "Dresses")
        Services.compare_actual_items_with_heading(self, "There are X products")
        Services.move_to_item_img(self)
        Services.click_activate_quick_menu(self, 1)
        Services.click_button(self, "Add to cart", "button")
        Services.click_button(self, "Close ", "closeWindowButton")
        Services.click_on_cart(self)
        Services.verify_product_in_cart(self, 1)

if __name__ == '__main__':
    runner = TestRunner('./', 'Error', 'No：Firefox')
    runner.debug()
