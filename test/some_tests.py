import allure
# TODO replace test case link to TestOps

@allure.label("issue", "N2-1")
@allure.epic("Web interface")
@allure.issue("N2-1")
@allure.label('layer', 'api')
def test_sample1():
    allure.dynamic.issue("AUTH-123")
    pass

@allure.label("issue", "N2-1")
@allure.epic("Web interface")
@allure.issue("N2-1")
@allure.label('layer', 'ui')
def test_sample2():
    allure.dynamic.issue("AUTH-123")
    pass