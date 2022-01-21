"""
Завдання: за допомогою браузера (Selenium) відкрити форму за наступним посиланням:

https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link

заповнити і відправити її.
Зберегти два скріншоти: заповненої форми і повідомлення про відправлення форми.
В репозиторії скріншоти зберегти.


Корисні посилання:
https://www.selenium.dev/documentation/
https://chromedriver.chromium.org/downloads

"""

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chr = Chrome(executable_path="./chromedriver", service=Service(ChromeDriverManager().install()))
chr.get(
    "https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link")
nameInput = chr.find_element(By.CSS_SELECTOR, ".quantumWizTextinputPaperinputInput.exportInput")
nameInput.click()
nameInput.send_keys("Sergey Berezhnoy")
chr.save_screenshot("commit.jpg")
chr.find_element(
    By.CSS_SELECTOR, ".appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel").click()
chr.save_screenshot("push.jpg")
chr.close()

