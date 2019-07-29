from .base_page import BasePage
from .locators import CartLocators


class CartPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_element_present(*CartLocators.EMPTY_CART_MESSAGE), "Cart is not empty"

    def should_not_be_product_in_cart(self):
        assert self.is_not_element_present(
            *CartLocators.PRODUCT_NAME), "There is some product in the cart. Cart is not empty"
