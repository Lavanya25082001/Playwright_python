# pages/login_page.py

from playwright.async_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.popup_cancel = "//*[name()='path' and contains(@d,'M6 6L14 14')]"
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

    async def Launching(self, WAurl:str):
        await self.page.goto(WAurl)

    async def navigate_to_login(self):
        await self.page.locator(self.popup_cancel).click()
        await self.page.locator(self.Account_icon).click()

    async def login(self, email: str, password: str):
        await self.page.locator(self.email_field).click()
        await self.page.locator(self.email_field).fill(email)
        await self.page.locator(self.password_field).click()
        await self.page.locator(self.password_field).fill(password)
        await self.page.locator(self.signin_button).click()

    async def about(self, keymsg: str, name: str, mail:str, number: str, msg: str):
        await self.page.locator(self.about_optn).click()
        await self.page.locator(self.contactus_button).click()
        await self.page.locator(self.keymsg_field).click()
        await self.page.locator(self.keymsg_field).fill(keymsg)
        await self.page.locator(self.name_field).click()
        await self.page.locator(self.name_field).fill(name)
        await self.page.locator(self.mail_field).click()
        await self.page.locator(self.mail_field).fill(mail)
        await self.page.locator(self.number_field).click()
        await self.page.locator(self.number_field).fill(number)
        await self.page.locator(self.msg_field).click()
        await self.page.locator(self.msg_field).fill(msg)
        await self.page.locator(self.send_button).click()
    
    async def Click_facebook(self):
        await self.page.locator(self.facebook).click()

    async def actions_facebooktab(self):
        await self.page.locator(self.closefbModel).click()
    
    async def logout(self):
        await self.page.locator(self.Account_icon).click()
        await self.page.locator(self.logout_button).click()
   
    
    

    

