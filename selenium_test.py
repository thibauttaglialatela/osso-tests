from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
print('Type URL: http://127.0.0.1:8000/')
driver.get('http://127.0.0.1:8000/')
navbar = driver.find_element(By.ID, "navbarDropdown")
assertion(navbar is not None, 'navbar found')

print('click on element : navbarDropdown')
navbar.click()
print('click on element : musicians-orchestra')
driver.find_element(By.ID, 'musicians-orchestra').click()
modal = driver.find_element(By.XPATH, '/html/body/main/section/div/div[3]/div/div/div/button')
modal.click()
modal.find_element(By.XPATH, '//*[@id="exampleModal_99"]/div/div/div[3]/button').click()
driver.back()
contact = driver.find_element(By.XPATH, '//*[@id="navbarOSSO"]/ul/li[5]/a')
contact.click()
full_name = driver.find_element(By.NAME, 'contact[fullName]')
full_name.send_keys('Thibaut Taglialatela')
email = driver.find_element(By.NAME, 'contact[email]')

email.send_keys('toto@test.fr')
subject = driver.find_element(By.ID, 'contact_subject')
subject.send_keys("sujet de test")
contact_message = driver.find_element(By.ID, 'contact_message')
contact_message.send_keys('ceci est un test')
send_message = driver.find_element(By.ID, 'contact_save')
send_message.click()
driver.find_element(By.ID, "navbarDropdown").click()
driver.find_element(By.ID, 'musicians-orchestra').click()
instruments = driver.find_elements(By.CSS_SELECTOR, "body > main > section > div > div:nth-child(1) > div > div > div > button")
for instrument in instruments:
    instrument.click()
    driver.find_element(By.XPATH, '//*[@id="exampleModal_97"]/div/div/div[3]/button').click()