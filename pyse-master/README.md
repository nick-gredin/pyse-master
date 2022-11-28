# pyse
WebUI automation testing framework based on Selenium and unittest.

####
* Python 3.5+ : https://www.python.org/
* Selenium 3.12.0 : https://pypi.python.org/pypi/selenium


```
> python setup.py install
```


```python
import pyse

class NickTest(TestCase, Services):

     def test_case_0001_adding_item_into_cart(self):
        """ Nick test"""
        self.open("http://automationpractice.com/index.php")
        Services.click_button(self, "Women", "tabButton")
        Services.click_plus_button_to_expand_category(self, "Tops")
        Services.click_plus_button_to_expand_category(self, "Dresses")
        Services.compare_actual_items_with_heading(self, "There are X products")
        #Services.click_on_item_quickview(self, 1)
        Services.move_to_item_img(self)
        Services.click_activate_quick_menu(self, 1)
        Services.click_button(self, "Add to cart", "button")
        Services.click_button(self, "Close ", "closeWindowButton")
        Services.click_on_cart(self)
        Services.verify_product_in_cart(self, 1)

if __name__ == '__main__':
    runner = pyse.TestRunner()
    runner.run()
```


```python
import pyse

class YouTest(pyse.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")
    
    def test_case(self):
        #……

```

drivers:

```python
cls.driver = Pyse("firefox")   #Firefox
cls.driver = Pyse("chrome")    # Chrome
cls.driver = Pyse("ie")        #IE
cls.driver = Pyse("opera")     #Opera
cls.driver = Pyse("edge")      #Edge
cls.driver = Pyse("chrome_headless")  #Chrome headless模式
```

mozilla：

geckodriver(Firefox):https://github.com/mozilla/geckodriver/releases

Chromedriver(Chrome):https://sites.google.com/a/chromium.org/chromedriver/home

IEDriverServer(IE):http://selenium-release.storage.googleapis.com/index.html

operadriver(Opera):https://github.com/operasoftware/operachromiumdriver/releases

MicrosoftWebDriver(Edge):https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

==========================================================

#### report:


```html
    <form id="form" class="fm" action="/s" name="f">
      <span class="bg s_ipt_wr quickdelete-wrap">
        <input id="kw" class="s_ipt" autocomplete="off" maxlength="255" value="" name="wd">
```

CSS：

```python
#
driver.type(".s_ipt","pyse")     #css
driver.type("#su","pyse")        #css

driver.type("id=>kw", "pyse")  #id

driver.type("class=>s_ipt", "pyse")

driver.type("name=>wd", "pyse")  #name

driver.type("xpath=>//*[@class='s_ipt']","pyse")  #xpath
driver.type("xpath=>//*[@id='kw']","pyse")        #xpath

driver.click_text("link_text=>link") #link text ()

```

==========================================================


  http://www.w3school.com.cn/cssref/css_selectors.asp

####

