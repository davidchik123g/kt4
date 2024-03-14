import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import allure
import logging

from MainPage import MainPage
from ProductPage import ProductPage
from CartPage import CartPage
from RegisterPage import RegisterPage


@allure.feature("First test")
@allure.title("screenshot view")
def test_screenshot(driver,logger):
    main_page = MainPage(driver,logger)
    main_page.go_to_site()
    time.sleep(1)
    product_page = ProductPage(driver,logger)
    time.sleep(1)
    product_page.open_product()
    time.sleep(1)
    product_page.open_thumbnail()
    time.sleep(1)
    product_page.next_lightbox()
    time.sleep(1)
    product_page.next_lightbox()
    time.sleep(1)
    product_page.next_lightbox()
    time.sleep(1)


@allure.feature("Second test")
@allure.title("Cart")
def test_cart(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    time.sleep(2)
    cart_page = CartPage(driver, logger)
    time.sleep(1)
    cart_page.add_to_cart()
    time.sleep(1)
    cart_page.open_cart()
    time.sleep(1)
    cart_items = cart_page.get_cart_items()
    if len(cart_items) <= 1:
        print("Корзина пуста.")
    else:
        print("Корзина не пуста.")

    time.sleep(1)


@allure.feature("Third test")
@allure.title("PC")
def test_pc_category(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    time.sleep(1)
    time.sleep(1)
    main_page.open_pc_category()
    time.sleep(2)
    product_items = main_page.get_product_items()
    if product_items:
        print("Страница категории PC пуста.")
    else:
        print("Страница категории PC не пуста.")


@allure.feature("Fourth test")
@allure.title("Register")
def test_register(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    time.sleep(2)
    register_page = RegisterPage(driver, logger)
    time.sleep(1)
    register_page.open_register_page()
    time.sleep(1)
    register_page.register_user("Да", "Га", "gaga@gmail.com", "12345", "9999")
    time.sleep(1)


@allure.feature("Fifth test")
@allure.title("Search")
def test_search(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    time.sleep(2)
    main_page.search("камеры")
    time.sleep(1)


@allure.feature("Sixth test")
@allure.title("wishlist")
def test_add_to_wishlist(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    time.sleep(1)
    product_page = ProductPage(driver, logger)
    time.sleep(1)
    product_page.add_to_wishlist(2)
    time.sleep(1)


@allure.feature("Seventh test")
@allure.title("Camera")
def test_add_camera_to_cart(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    product_page = ProductPage(driver, logger)
    time.sleep(1)
    product_page.add_to_cart(4)
    time.sleep(1)
    product_page.camera()
    time.sleep(1)


@allure.feature("eight test")
@allure.title("Tablet")
def test_add_tablet_to_cart(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    time.sleep(1)
    main_page.open_category("Планшеты")
    time.sleep(1)
    product_page = ProductPage(driver, logger)
    time.sleep(1)
    product_page.add_to_cart_tablet()
    time.sleep(1)


@allure.feature("Ninth test")
@allure.title("Htc")
def test_add_htc_to_cart(driver, logger):
    main_page = MainPage(driver, logger)
    main_page.go_to_site()
    time.sleep(1)
    main_page.open_category("Телефоны")
    time.sleep(1)
    product_page = ProductPage(driver, logger)
    time.sleep(1)
    product_page.add_to_cart_htc()
    time.sleep(2)


@allure.feature("Teenth test")
@allure.title("Submit")
def test_submit_review(driver, logger):
    main_page = MainPage(driver, logger)
    time.sleep(2)
    main_page.go_to_site()
    time.sleep(2)
    main_page.open_category("Apple Cinema 30")
    product_page = ProductPage(driver, logger)
    time.sleep(1.5)
    product_page.open_review_form()
    time.sleep(1.5)
    product_page.submit_review("Blinchik", "очень хороший товар, но со своими недочетами")
    time.sleep(1.5)
