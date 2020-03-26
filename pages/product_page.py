from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_same_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        alert_item_name = self.browser.find_element(*ProductPageLocators.ALERT_ITEM_NAME).text
        assert item_name == alert_item_name, "Items name are not same"

    def should_be_same_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        alert_item_price = self.browser.find_element(*ProductPageLocators.ALERT_ITEM_PRICE).text
        assert item_price == alert_item_price, "Prices are not same"
