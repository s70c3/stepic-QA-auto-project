from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def is_basket_empty_text_present(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text

    def should_not_be_item_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items is presented, but should not be"

    def should_be_item_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items is not presented, but should not be"
