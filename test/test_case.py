import pytest
from pages.login_page import LoginPage
from utils.logger_po import get_logger

logger=get_logger(__name__)

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce")
])
def test_login(driver,username,password):
    login=LoginPage(driver)
    logger.info("Starting TestCase now")
    login.websites(url="https://saucedemo.com")
    login.login(username,password,want="https://www.saucedemo.com/inventory.html")
    logger.info("test Passes Successfully")
