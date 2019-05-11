# -*- coding: utf-8 -*-
import scrapy

#
# ALMIGHTY JUMIA CRAWLER 😎
#
#

URLS = {
    "phones": "mobile-phones/",
    "phone_accesories": "mobile-accessories/",
    "televisions": "televisions/",
    "men_clothing": "men-clothing/",
    "women_clothing": "womens-clothing/",
    "women_shoes": "womens-shoes/",
    "women_accessories": "womens-accessories/",
    "women_watches": "women-watches/",
    "men_watches": "mens-watches/",
    "laptops": "laptops/",
    "game_hardware": "game-hardware/",
    "computer_peripherals": "peripherals/",
    "smart_phones": "smartphones/",
    "basic_phones": "basic-phones/",
    "mens_fragrances": "mens-fragrances/",
    "womens_fragrances": "womens-fragrances/",
    "all_fragrances": "fragrances-allgenders/",
    "men_shirts": "mens-shirts/",
    "ios_phones": "ios-phones/",

}
# Example
# ?price_discount=90-100&sort=newest&dir=desc&seller_score=3-5

FILTERS = {
    "discount": "?price_discount=",
    "newest": "&sort=newest&dir=desc",
    "rating": "&seller_score="
}

PLACEHOLDER_PIC = "https://www.jumia.com.ng/images/local/placeholder/placeholder_m_1.jpg"

# all-products/


class JumiaSpider(scrapy.Spider):
    name = 'jumia'
    allowed_domains = ['jumia.com.ng']
    start_urls = ['https://www.jumia.com.ng/', 'https://www.jumia.com.ng/mobile-phones/samsung/',
                  'https://www.jumia.com.ng/phones-tablets/apple/',
                  'https://www.jumia.com.ng/jack-jones/',
                  'https://www.jumia.com.ng/watches-sunglasses/',
                  ]
                  

    def parse(self, response):
        # print("it got here oo")
        items = response.xpath("//*[contains(@class,'sku -gallery')]")
        for item in items:
            sku = item.xpath(".//@data-sku").extract_first()
            name = item.xpath(".//span[@class='name']/text()").extract_first()
            link = item.xpath(".//a[@class='link']/@href").extract_first()
            brand = item.xpath(
                ".//span[contains(@class, 'brand')]/text()").extract_first()
            image = item.xpath(
                ".//div[contains(@class,'image-wrapper')]/noscript/img/@src").extract_first()

            # prices matters
            discount = item.xpath(
                ".//span[@class='sale-flag-percent']/text()").extract_first()
            new_price = item.xpath(
                ".//span[contains(@class,'price')]/span[@dir='ltr']/@data-price").extract()
            if len(new_price) == 3:
                new_price = new_price[1]
            elif len(new_price) > 0:
                new_price = new_price[0]
            else:
                new_price = None

            old_price = item.xpath(
                ".//span[contains(@class, 'price') and contains(@class, 'old')]/span[@dir='ltr']/@data-price").extract_first()

            free_shipping = True if item.xpath(
                ".//span[@class='free-shipping-eligible-container']/text()").extract_first() else False

            is_global = True if item.xpath(
                ".//span[contains(@class,'-jumia-global')]").extract_first() else False

            yield {
                "sku": sku,
                "name": name,
                "brand": brand,
                "image": image,
                "link": link,
                "price": int(new_price) if new_price else 0,
                "discount": int(discount.strip('-%')) if discount else 0,
                "is_global": is_global,
            }

        # from time import sleep
        # import random
        # sleep(random.randrange(1, 5))

        next_page_url = response.xpath(
            "//a[@title='Next']/@href").extract_first()

        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_next_page_url, dont_filter=True)
