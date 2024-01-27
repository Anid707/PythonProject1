from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pageObjects.base_page import BasePage
import time


class SearchFlightPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def from_city(self):
        return self.wait.until(ec.visibility_of_any_elements_located((By.XPATH, "//*[@data-test-id='origin-endpoint']/div[2]/span")))

    @property
    def cheapest_lbl(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text()='Cheapest']")))

    def is_search_result_found(self):
        time.sleep(5)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.cheapest_lbl)
        print(len(self.from_city))
        return len(self.from_city) >= 1

