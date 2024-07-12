import allure
# TODO replace test case link to TestOps

@allure.label("issue", "N2-1")
@allure.label("issue", "N2-2")
@allure.epic("Web interface")
@allure.epic("Web interface2")
@allure.issue("N2-2")
def test_sample():
    allure.dynamic.issue("AUTH-123")
    pass


@allure.id(14)
@allure.label("owner", "iAmTheBest")
@allure.title("here we go again with scenario")
def test_here_we_go_again_with_scenario():

    pass


@allure.id(3)
@allure.label("owner", "iAmTheBest")
@allure.title("1")
def test_1():
    with allure.step("Attachment [2]"):
        pass

    with allure.step("fssdgfhg"):
        pass

    with allure.step("hgfj"):
        pass

    with allure.step("gfhgfjh"):
        pass

    with allure.step("dgfdhgfj"):
        pass

    with allure.step("sgfhg"):
        pass

    with allure.step("[yandex](https:\/\/ya.ru)"):
        pass
    pass
