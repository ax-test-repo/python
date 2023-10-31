import re
from playwright.sync_api import Playwright, Page, Route, sync_playwright, expect

def test_generator(playwright: Playwright) -> None:
    # c playwright codegen https://demoqa.com/books
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/books")
    page.locator("span").filter(has_text="Elements").locator("div").first.click()
    page.locator("li").filter(has_text="Text Box").click()
    page.get_by_placeholder("Full Name").click()
    page.get_by_placeholder("Full Name").fill("1")
    page.get_by_role("button", name="Submit").click()
    context.close()
    browser.close()


def test_buttons(playwright: Playwright) -> None:
    # с headless=False и firefox
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/books")
    page.locator("span").filter(has_text="Elements").click()
    page.locator("li").filter(has_text="Buttons").click()
    page.get_by_role("button", name="Double Click Me").dblclick()
    expect(page.get_by_text("You have done a double click")).to_be_visible()
    page.get_by_role("button", name="Right Click Me").click(button="right")
    expect(page.get_by_text("You have done a right click")).to_be_visible()
    page.get_by_role("button", name="Click Me", exact=True).click()
    expect(page.get_by_text("You have done a dynamic click")).to_be_visible()
    context.close()
    browser.close()

def test_dynamic_elements(page: Page):
    # с ожиданием элементов и опцией  
    # pytest --tracing on  -v -s .\playwright\test_ui.py::test_dynamic_elements
    # playwright show-trace .\test-results\playwright-test-ui-py-test-dynamic-elements-chromium\trace.zip
    page.goto("https://demoqa.com/books")
    page.get_by_text("Elements").click()
    page.get_by_text("Dynamic Properties").click()
    page.get_by_role("button", name="Will enable 5 seconds").click()
    page.get_by_role("button", name="Visible After 5 Seconds").click()

def test_book_store_with_rout(playwright: Playwright):
    # с подменой и остановкой
    def handle(route: Route):
        json = {"books" : [
        {
            "isbn": "111111",
            "title": "Test",
            "subTitle": "Test test",
            "author": "Test Test",
            "publish_date": "2020-06-04T08:48:39.000Z",
            "publisher": "O'Reilly Media",
            "pages": 234,
            "description": "Test test test test",
            "website": "http://index.html"
        }
		]}
        route.fulfill(json=json)
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.route("https://demoqa.com/BookStore/v1/Books", handle)
    page.goto("https://demoqa.com/books")
    page.pause()
    context.close()
    browser.close()

def test_book_store_request(playwright: Playwright): 
    #   с ожидание ответа api его проверкой
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    with page.expect_response("https://demoqa.com/BookStore/v1/Boks") as response_info:
        page.goto("https://demoqa.com/books")
    response = response_info.value
    assert response.ok
    browser.close()
    