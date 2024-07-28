from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ACCOUNT_EMAIL = "yuvasrimanikandan07@gmail.com"
ACCOUNT_PASSWORD = "yuvamani07"
PHONE = "8248171814"
# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3933393735&distance=25&geoId=102713980&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true"
)

# Click Reject Cookies Button
try:
    reject_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[action-type="DENY"]'))
    )
    reject_button.click()
except Exception as e:
    print("Reject button not found or could not be clicked:", e)

# Click Sign in Button
try:
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
    )
    sign_in_button.click()
except Exception as e:
    print("Sign in button not found or could not be clicked:", e)

# Sign in
try:
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    email_field.send_keys(ACCOUNT_EMAIL)

    password_field = driver.find_element(by=By.ID, value="password")
    password_field.send_keys(ACCOUNT_PASSWORD)
    password_field.send_keys(Keys.ENTER)
except Exception as e:
    print("Error during sign in:", e)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Locate the apply button
try:
    apply_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-s-apply button"))
    )
    apply_button.click()
except Exception as e:
    print("Apply button not found or could not be clicked:", e)

# If application requires phone number and the field is empty, then fill in the number.
try:
    phone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[id*=phoneNumber]"))
    )
    if not phone.get_attribute("value"):
        phone.send_keys(PHONE)
except Exception as e:
    print("Phone number field not found or could not be filled:", e)

# Submit the application
try:
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "footer button"))
    )
    submit_button.click()
except Exception as e:
    print("Submit button not found or could not be clicked:", e)
