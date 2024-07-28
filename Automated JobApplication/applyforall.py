from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

ACCOUNT_EMAIL = "yuvasrimanikandan07@gmail.com"
ACCOUNT_PASSWORD = "yuvamani07"
PHONE = "8248171814"


def abort_application():
    try:
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

        time.sleep(2)
        # Click Discard Button
        discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
        discard_button.click()
    except NoSuchElementException as e:
        print(f"Error in aborting application: {e}")


# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3933393735&distance=25&geoId=102713980&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true")

# Click Reject Cookies Button
try:
    reject_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[action-type="DENY"]'))
    )
    reject_button.click()
except (NoSuchElementException, TimeoutException):
    print("Reject cookies button not found or could not be clicked")

# Click Sign in Button
try:
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
    )
    sign_in_button.click()
except (NoSuchElementException, TimeoutException):
    print("Sign in button not found or could not be clicked")

# Sign in
try:
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    email_field.send_keys(ACCOUNT_EMAIL)

    password_field = driver.find_element(by=By.ID, value="password")
    password_field.send_keys(ACCOUNT_PASSWORD)
    password_field.send_keys(Keys.ENTER)
except (NoSuchElementException, TimeoutException):
    print("Error during sign in")

# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Get Listings
try:
    all_listings = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container--clickable"))
    )
except (NoSuchElementException, TimeoutException):
    print("Job listings not found")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-s-apply button"))
        )
        apply_button.click()

        # Insert Phone Number
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.get_attribute("value") == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except (NoSuchElementException, TimeoutException):
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()




