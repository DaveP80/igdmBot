import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from googleapiclient.errors import HttpError
from selenium.webdriver.common.keys import Keys
import random
from dotenv import load_dotenv
from os import environ, path

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

SECRET_P = environ.get('PASS')

# Set up credentials to access Google Sheets API
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/yourpath/credentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheets spreadsheet and select the first sheet
sheet = client.open('leads_spreadsheet').sheet1

driver_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)
#optional setting
#driver.fullscreen_window()
if driver:
    driver.get('https://www.instagram.com/')
    time.sleep(random.randint(2, 4))
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys('username')
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(SECRET_P)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(random.randint(4, 6))
count = 1
loop = False
for row in sheet.get_all_records():
    count += 1
    if not row['Instagram Account']:
        pass
    elif row['Instagram Account'] != "":
        try:
            greeting = ['Hello', 'Sup :)', 'Howdy', 'Hi!', 'Hola', 'Greetings', 'Hello sir or madame']
            if not loop:
                driver.get('https://www.instagram.com/direct/new/')
                driver.find_element(By.XPATH, "//button[text()='Not Now']").click()
                WebDriverWait(driver=driver, timeout=random.randint(3, 6)).until(EC.visibility_of_element_located((By.NAME, 'queryBox')))
                to_field = driver.find_element(By.NAME, 'queryBox')
            if loop:
                driver.get('https://www.instagram.com/direct/new/')
                WebDriverWait(driver=driver, timeout=random.randint(3, 6)).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]')))
                to_field = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input')
            time.sleep(.5)
            to_field.send_keys(row['Instagram Account'])
            time.sleep(random.randint(3,4))
            if not loop:
                actionf = driver.find_element(By.NAME, 'queryBox')
            if loop:
                actionf = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input')
            a=ActionChains(driver)
            a.send_keys(Keys.TAB).send_keys(Keys.ENTER)
            a.perform()
            time.sleep(random.randint(2,3))
            if not loop:
                actionz = driver.find_element(By.NAME, 'queryBox')
            if loop:
                actionz = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input')
            c=ActionChains(driver)
            c.key_down(Keys.SHIFT).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER)
            c.perform()
            c = None
            time.sleep(random.randint(4,6))
            mssg = driver.find_element(By.TAG_NAME, 'textarea')
            mssg.send_keys(random.choice(greeting))
            time.sleep(.5)
            smssg = driver.find_element(By.TAG_NAME, 'textarea')
            b=ActionChains(driver)
            b.send_keys(Keys.ENTER)
            b.perform()
            date_sent = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sheet.update_cell(count, 4, date_sent) 
            loop = True
        except HttpError as err:
            print(err)
driver.quit()