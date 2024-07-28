from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ACCOUNT_EMAIL = "yuvasrimanikandan07@gmail.com"
ACCOUNT_PASSWORD = 'yuvamani07'

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3933393735&distance=25&geoId=102713980&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true"
)

# Wait for the Reject Cookies Button and click it


try:
    reject_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[action-type="DENY"]'))
    )
    reject_button.click()
except Exception as e:
    print("Reject button not found:", e)

# Click Sign in Button
try:
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
    )
    sign_in_button.click()
except Exception as e:
    print("Sign in button not found:", e)

# Sign in
try:
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    email_field.send_keys(ACCOUNT_EMAIL)

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_field.send_keys(ACCOUNT_PASSWORD)
    password_field.send_keys(Keys.ENTER)
except Exception as e:
    print("Error during sign in:", e)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Continue with the rest of your script...

# Close the driver after completing your task
time.sleep(5)
driver.quit()


