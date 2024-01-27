import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pageObjects.main_page import MainPage
import logging


class TestMainPage:
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    @pytest.fixture()
    def test_setup(self):
        global driver
        options = Options()
        #options.add_argument('--headless')
        #options.add_argument('window-size=1400, 600')
        options.add_argument('start-maximized')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        #driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.logger.info("------------------------------------")
        self.logger.info("Test has started!")

        yield
        time.sleep(10)
        driver.quit()
        self.logger.info("Test has finished!")

    #@pytest.mark.test_group
    @pytest.mark.skip
    def test_open_main_page(self, test_setup):
        main_page = MainPage(driver)
        main_page.open()
        assert main_page.check()
        self.logger.info("Main page is opened!")

    #@pytest.mark.test_group
    @pytest.mark.parametrize("from_city, to_city, start_date, end_date", [("Astana", "Almaty", "01.02.2024", "07.02.2024"),("Istanbul", "Dubai", "05.02.2024", "10.02.2024")])
    def test_open_search_flight_page(self, test_setup, from_city, to_city, start_date, end_date):
        self.logger.info("Opening Main page!")
        main_page = MainPage(driver)
        main_page.open()
        self.logger.info("Entering the form data!")
        search_flight_page = main_page.search_flights(from_city, to_city, start_date, end_date)
        self.logger.info("Form data is submitted!")
        assert search_flight_page.is_search_result_found()
        assert search_flight_page.from_city[0].text == from_city
        self.logger.info("Search result page is opened! " + search_flight_page.from_city[0].text)




