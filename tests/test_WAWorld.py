import pytest
from pages.LoginPage import LoginPage
from pages.assertions import assertionsPage

@pytest.mark.smoke
@pytest.mark.asyncio
async def test_login(page, env_vars):
    url = env_vars['url']
    username = env_vars['username']
    password = env_vars['password']
    await page.goto(url)
    login_page = LoginPage(page)
    
    await login_page.navigate_to_login()
    await login_page.login(username, password)
    # await login_page.logout()

@pytest.mark.smoke
@pytest.mark.asyncio
async def test_about(page, env_vars):
    url = env_vars['url']
    
    login_page = LoginPage(page)
    await login_page.Launching(url)

@pytest.mark.smoke
@pytest.mark.asyncio
async def test_newtabActions(page, context, env_vars):
    url = env_vars['url']
    username = env_vars['username']
    password = env_vars['password']
    
    login_page = LoginPage(page)
    await login_page.Launching(url)
    await login_page.navigate_to_login()
    await login_page.login(username, password)
    await login_page.Click_facebook()

    # Wait for the new tab to open
    new_page = await context.wait_for_event('page')
    # Create an instance of LoginPage for the new tab
    new_tab_facebook_page = LoginPage(new_page)
    # Perform actions on the new tab
    await new_tab_facebook_page.actions_facebooktab()
    # Close the new tab
    await new_page.close()

    # Switch back to the original tab if needed
    await page.bring_to_front()

@pytest.mark.smoke
@pytest.mark.asyncio
async def test_assertions(page, env_vars):
    url = env_vars['url']
    
    login_page = LoginPage(page)
    await login_page.Launching(url)
    assertion_page = assertionsPage(page)
    await assertion_page.verifying_Title()
    await assertion_page.verifying_URL()
    await assertion_page.verifying_Text()
    await assertion_page.verifying_visibility()
    await assertion_page.verifying_textContains()
    await assertion_page.verifying_input()
