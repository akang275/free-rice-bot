from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')

#this line works outside of remote wsl
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

driver.get("https://freerice.com/categories/multiplication-table")

save_button = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))

save_button.click()

WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'card-title')))

def check_for_new_problem(driver):
    global problem

    new_problem_element = driver.find_element(By.CLASS_NAME, 'card-title')
    new_problem = new_problem_element.text.split(' x ')

    #print(new_problem)
    if new_problem != ['']and new_problem != problem:
        return True
    else:
        return False

while True:

    problem_element = driver.find_element(By.CLASS_NAME, 'card-title')
    problem = problem_element.text.split(' x ')

    #print(problem)

    answer = int(problem[0]) * int(problem[1])

    choices = driver.find_elements(By.CLASS_NAME, 'card-button')

    for c in choices:
        if int(c.text) == answer:
            c.click()

    WebDriverWait(driver, timeout=10).until(check_for_new_problem)