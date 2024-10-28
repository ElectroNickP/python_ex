from pipes import stepkinds

import allure
import pytest

# TODO replace test case link to TestOps
@allure.label("issue", "N2-2")
@allure.label("issue", "N2-1")
@allure.epic("Web interface")
@allure.issue("N2-1")
@allure.label('layer', 'api')
@allure.link("https://testops.yourcompany.com/test-cases/1234", name="TestOps Link", link_type="test_case")
def test_sample1():
    allure.dynamic.issue("AUTH-123")
    pass

@allure.label("issue", "N2-1")
@allure.epic("Web interface")
@allure.issue("N2-1")
@allure.label('layer', 'ui')
@allure.step("Step 1")
@allure.link("https://testops.yourcompany.com/test-cases/5678", name="TestOps Link", link_type="test_case")
def test_sample2():
    allure.dynamic.issue("AUTH-123")
    pass
<<<<<<< HEAD
=======

@pytest.fixture()
@allure.title("Prepare for the test")
def my_fixture():
    # set up
    yield
    # tear down
    with open("/home/nick/Pictures/Buggie bug2.png", "rb") as image_file:
        image_data = image_file.read()
        allure.attach(image_data, name="Screenshot", attachment_type=allure.attachment_type.PNG)

def test_with_my_fixture(my_fixture):
    pass
>>>>>>> e90a924 (Added missing files from root directory)
