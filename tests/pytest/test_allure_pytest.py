import allure

@allure.step("Opening browser")
def open_browser():
    with allure.step("Get browser"):
        pass

    with allure.step("Start browser"):
        pass


@allure.step("Creating course with title '{title}'")
def crate_course(title: str):
    pass


@allure.step("Closing")
def close_browser():
    pass

def test_feature():
    open_browser()

    crate_course(title="Locust")
    crate_course(title="Pytest")
    crate_course(title="Python")
    crate_course(title="Playwright")

    close_browser()


