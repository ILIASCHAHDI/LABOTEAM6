
driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")
assert "Wikipedia" in driver.title
driver.close()
