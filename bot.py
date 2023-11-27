from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1000,800', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(options=chrome_options)
    
    return driver


driver = iniciar_driver()
driver.get('https://www.facebook.com')
sleep(4)

barra_de_email = driver.find_element(By.ID,'email')
barra_de_email.send_keys('')
sleep(2)

barra_da_senha = driver.find_element(By.ID,'pass')
barra_da_senha.send_keys('')
sleep(2)

caixa_de_login = driver.find_element(By.XPATH,'//button[@name="login"]')
caixa_de_login.click()
sleep(5)

caixa_de_status = driver.find_element(By.XPATH,'//div[@class="xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe"]')
caixa_de_status.click()
sleep(5)

caixa_dentro_status = driver.find_element(By.XPATH,"//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
caixa_dentro_status.click()
sleep(4)
caixa_dentro_status.send_keys('Ola pessoal')


input('')
driver.close()