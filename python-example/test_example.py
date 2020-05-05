import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://yandex.ru/")
    driver.find_element_by_name("text").send_keys("webdriver")
    driver.find_element_by_tag_name("button").click()
    WebDriverWait(driver, 10).until(EC.title_contains("webdriver — Яндекс"))