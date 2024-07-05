import pytest
import os
import json
from dotenv import load_dotenv
from playwright.async_api import async_playwright

# Load environment variables from .env file
load_dotenv()

# Load data from data.json
data_file = os.path.join('Data', 'data.json')
with open(data_file, 'r') as f:
    data = json.load(f)

@pytest.fixture(scope="session")
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        yield browser
        await browser.close()

@pytest.fixture
async def context(browser):
    context = await browser.new_context()
    yield context
    await context.close()

@pytest.fixture
async def page(context):
    page = await context.new_page()
    yield page
    await page.close()

@pytest.fixture
def test_data():
    return data

@pytest.fixture
def env_vars():
    return {
        'url': os.getenv('WAWorld_URL'),
        'username': os.getenv('WAWorld_username'),
        'password': os.getenv('WAWorld_password')
    }
