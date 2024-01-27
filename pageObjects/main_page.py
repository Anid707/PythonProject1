import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pageObjects.base_page import BasePage
from pageObjects.search_flight_page import SearchFlightPage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def header(self):
        return self.driver.find_elements(By.CLASS_NAME, "header__title")

    @property
    def from_input(self):
        return self.wait.until(ec.element_to_be_clickable((By.ID, "avia_form_origin-input")))

    @property
    def to_input(self):
        return self.wait.until(ec.presence_of_element_located((By.ID, "avia_form_destination-input")))

    @property
    def start_date(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@data-test-id='start-date-field']")))

    @property
    def end_date(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@data-test-id='end-date-field']")))

    @property
    def passengers_field(self):
        return self.wait.until(ec.presence_of_element_located((By.XPATH, "//button[@data-test-id='passengers-field']")))

    @property
    def plus_passengers(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, "(//button[@data-test-id='increase-button'])[1]")))

    @property
    def flight_class(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@data-test-id='ragio-group']/label[3]")))

    @property
    def submit_btn(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@data-test-id='form-submit']")))

    def open(self):
        self.driver.get("https://www.aviasales.com/")
        time.sleep(5)

    def check(self):
        return len(self.header) == 1

    def search_flights(self, city1, city2, date1, date2):
        self.from_input.click()
        self.from_input.send_keys(city1)
        self.to_input.click()
        self.to_input.send_keys(city2)
        time.sleep(5)
        self.start_date.click()
        self.start_date.click()
        start_date = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@data-test-id='date-" + date1 + "']")))
        start_date.click()
        start_date.click()
        time.sleep(5)
        self.end_date.click()
        end_date = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@data-test-id='date-" + date2 + "']")))
        self.actions.move_to_element(end_date).double_click().perform()
        time.sleep(10)
        self.passengers_field.click()
        time.sleep(3)
        self.plus_passengers.click()
        self.flight_class.click()
        time.sleep(5)
        self.submit_btn.click()
        time.sleep(5)
        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[1])
        return SearchFlightPage(self.driver)



