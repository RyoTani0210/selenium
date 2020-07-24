from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Firefox()

# x. Chrome の起動オプションを設定する
options = webdriver.ChromeOptions()
# options.add_argument('--headless')

# x. ブラウザの新規ウィンドウを開く
print('connecting to remote browser...')
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=options.to_capabilities(),
    options=options,
)


driver.get("https://scraping-for-beginner.herokuapp.com/")
print(driver.current_url)
print(driver.title)

if "Webスクレイピング" in driver.title:
    print("Success!!")
else :
    print("Failed...")

driver.close()