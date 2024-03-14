import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from BasePage import BasePage



class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(4) div.product-thumb.transition div.caption h4:nth-child(1) > a:nth-child(1)")
    THUMBNAILS = (By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row div.col-sm-8 ul.thumbnails li > a.thumbnail")
    LIGHTBOX_NEXT = (By.CSS_SELECTOR, "body:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-s-ready.mfp-image-holder > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close:nth-child(4)")

    def open_product(self):
        product_name = self.find_element(self.PRODUCT_NAME)
        product_name.click()

    def open_thumbnail(self):
        thumbnail = self.find_elements(self.THUMBNAILS)[0]
        thumbnail.click()

    def next_lightbox(self):
        next_button = self.find_element(self.LIGHTBOX_NEXT)
        next_button.click()

    def add_to_cart(self, product_number):
        add_to_cart_button = self.find_element((By.CSS_SELECTOR,
                                                f"div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child("
                                                f"4) "
                                                f"div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child("
                                                f"{product_number}) div.product-thumb.transition div.button-group > "
                                                f"button:nth-child(1)"))
        add_to_cart_button.click()

    def add_to_cart_tablet(self):
        add_to_cart_button = self.find_element((By.XPATH,
                                                "//body/div[@id='product-category']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]/i[1]"))
        add_to_cart_button.click()

    def add_to_cart_htc(self):
        add_to_cart_button = self.find_element((By.XPATH, "//body/div[@id='product-category']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]"))
        add_to_cart_button.click()

    def add_to_wishlist(self, product_number):
        add_to_wishlist_button = self.find_element((By.CSS_SELECTOR,
                                                    f"div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child({product_number}) div.product-thumb.transition div.button-group button:nth-child(2) > i.fa.fa-heart"))
        add_to_wishlist_button.click()

    def open_product_images(self, product_number):
        product_link = self.find_element((By.CSS_SELECTOR,
                                          f"div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child({product_number}) div.product-thumb.transition div.caption h4:nth-child(1) > a:nth-child(1)"))
        product_link.click()
        product_image = self.find_element((By.CSS_SELECTOR, "div.col-sm-8 ul.thumbnails li:nth-child(1) > a.thumbnail"))
        product_image.click()

    def switch_product_images(self):
        next_image_button = self.find_element((By.CSS_SELECTOR,
                                               "body:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-s-ready.mfp-image-holder > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close:nth-child(4)"))
        next_image_button.click()

    def open_review_form(self):
        review_link = self.find_element((By.XPATH, "//a[contains(text(),'Отзывов (0)')]"))
        review_link.click()

    def submit_review(self, name, review_text):
        name_input = self.find_element((By.ID, "input-name"))
        time.sleep(1.5)
        name_input.send_keys(name)
        time.sleep(1)
        review_input = self.find_element((By.ID, "input-review"))
        time.sleep(1.5)
        review_input.send_keys(review_text)
        time.sleep(1)
        rating_input = self.find_element((By.XPATH,
                                          "//body/div[@id='product-product']/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/form[1]/div[4]/div[1]/input[3]"))
        rating_input.click()
        time.sleep(1)
        submit_button = self.find_element((By.ID, "button-review"))
        time.sleep(1.5)
        submit_button.click()

    def camera(self):
        camera_option = self.find_element((By.ID, "input-option226"))
        camera_option.click()
        camera_option.send_keys(Keys.ARROW_DOWN)
        add_to_cart_button = self.find_element((By.ID, "button-cart"))
        add_to_cart_button.click()
