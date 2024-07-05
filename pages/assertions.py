# pages/login_page.py
import asyncio
from playwright.async_api import Page, expect


class assertionsPage:
    def __init__(self, page: Page):
        self.page = page
        self.popup_cancel = "//*[name()='path' and contains(@d,'M6 6L14 14')]"
        self.cart_bag =".icon-bag"
        self.cartPageText= ".section-header__title"
        self.search_icon='(//a[@href="/search"])[1]'
        self.search_field=".site-header__search-input"
        # placeholder="Search our store"
        self.launchingPage_text="//h3[text()='Custom Amenities']"

        self.Account_icon = "//a[@class='site-nav__link site-nav__link--icon small--hide']//*[name()='svg']"
        self.email_field = "#CustomerEmail"
        self.password_field = "#CustomerPassword"
        self.signin_button = "//button[normalize-space()='Sign In']"
        self.about_optn = "//a[text()='About']"
        self.contactus_button="//input[@value='Contact Us']"
        self.keymsg_field="#ContactFormSubject"
        self.name_field="//input[@id='ContactFormName-contact-form-alt']"
        self.mail_field="//input[@id='ContactFormEmail-contact-form-alt']"
        self.number_field="//input[@name='contact[phone]']"
        self.msg_field="//textarea[@name='contact[body]']"
        self.send_button="//button[normalize-space()='Send']"
        self.facebook='(//a[@title="World Amenities on Facebook"])[2]'
        self.closefbModel='//div[@aria-label="Close"]'
        self.twitter='(//a[@title="World Amenities on Twitter"])[2]'
        self.insta='(//a[@title="World Amenities on Instagram"])[2]'
        self.linkedin='(//a[@title="World Amenities on LinkedIn"])[2]'
        self.logout_button="//a[normalize-space()='Log out']"


    async def verifying_Title(self, ):
       await self.page.locator(self.popup_cancel).click()
       expected_title = "World Amenities®"
       actual_title = await self.page.title()
       assert actual_title == expected_title 

    async def verifying_URL(self):
        await self.page.locator(self.cart_bag).click()
        await asyncio.sleep(5)
        expected_URL = "https://worldamenities.com/cart"
        actual_URL= self.page.url
        assert actual_URL == expected_URL

    async def verifying_Text(self):
        expected_text= 'Cart'
        actual_text = await self.page.locator(self.cartPageText).text_content() 
        assert actual_text == expected_text

    async def verifying_visibility(self):
        await self.page.locator(self.search_icon).wait_for(state="visible")

    async def verifying_textContains(self):
        actual_text=await self.page.locator(self.launchingPage_text).text_content()
        expected_text='Amenities'
        assert expected_text in actual_text

    async def verifying_input(self):
        await self.page.locator(self.search_icon).click()
        await expect(self.page.locator(self.search_field)).to_be_empty()


    
    

    

