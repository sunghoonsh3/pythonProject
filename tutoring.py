from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from random import randint
import subprocess

# Function to perform random waits
def random_wait():
    time.sleep(randint(5, 7))

# Configure Chrome options for incognito mode
options = Options()
options.add_argument("--incognito")
options.add_experimental_option("detach", True)

# Using WebDriverManager to handle ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

web = "https://kimstudy.com/main"
driver.maximize_window()
driver.get(web)

# Handle first 리뉴얼 공지사랑 alert
wait = WebDriverWait(driver, 10)
try:
    first_alert_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div/div/div/div/div[2]/button[1]")))
    first_alert_button.click()
except Exception as e:
    print(f"Failed to click the second alert button: {e}")
random_wait()

# Log in
log_in = driver.find_element(By.XPATH, "/html/body/header/div/div[1]/div/div[2]/div[3]")
log_in.click()
#driver.find_element(By.ID, "id").send_keys("") Type your ID
#driver.find_element(By.ID, "pw").send_keys("") Type your password
driver.find_element(By.ID, "loginById").click()
random_wait()

#Handle second alert
wait = WebDriverWait(driver, 10)
try:
    alert_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[2]/button[1]")))
    alert_button.click()
except:
    pass
random_wait()

# Click the 만남수업/온라인수업 button
try:
    button1 = driver.find_element(By.XPATH, "/html/body/div[16]/div[2]/div[4]/div[1]/div[1]")
    button1.click()
except:
    # Handle exception if the button is not found or clickable
    pass

# Wait for a few seconds (you can adjust this duration as needed)
random_wait()

# Select 온라인/만남 과외
try:
    pop_up_button = driver.find_element(By.XPATH, "/html/body/div[8]/div/div/div[2]/div[2]/label/div")
    pop_up_button.click()
except:
    # Handle exception if the pop-up button is not found or clickable
    pass

# Wait for a few seconds (you can adjust this duration as needed)
random_wait()

# Click the search button
try:
    additional_button = driver.find_element(By.XPATH, "/html/body/div[8]/div/div/div[3]/div[2]/button")
    additional_button.click()
except:
    # Handle exception if the additional button is not found or clickable
    pass

# Wait for a few seconds (you can adjust this duration as needed)
random_wait()

# Define number extraction function
def extract_number(element):
    text = element.get_attribute("textContent")
    number = int(''.join(filter(str.isdigit, text)))
    return number

# Loop through 'a' elements
for i in range(2, 50):  
    try:
        a_element = driver.find_element(By.XPATH, f"//a[{i}]")
        a_element.click()

        # Perform actions after clicking 'a' element
        try:
            number_element = driver.find_element(By.XPATH, "/html/body/div[8]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[3]")
            number = extract_number(number_element)
        
            if number < 200:
                suggest_element = driver.find_element(By.XPATH, "/html/body/div[8]/div[2]/div/div/div[2]/div/div[2]/div")
                suggest_element.click()
                random_wait()
            
                # 복붙도구
                additional_button = driver.find_element(By.XPATH, "/html/body/div[12]/div/div/div[1]/div[2]/div[2]/div")
                additional_button.click()
                random_wait()

                # 복붙 프롬트 버튼
                next_button = driver.find_element(By.XPATH, "/html/body/div[14]/div/div/div[4]/div[1]/div[1]/div[2]")
                next_button.click()
                random_wait()

                # 제안서 보내기 버튼
                another_button = driver.find_element(By.XPATH, "/html/body/div[12]/div/div/div[2]/div[1]/button")
                another_button.click()
                random_wait()

                first_alert = driver.switch_to.alert
                first_alert.accept()
                time.sleep(5)

                second_alert = driver.switch_to.alert
                second_alert.accept()

        except:
            pass

        driver.back()

    except:
        pass

# Execute the shell script using subprocess
# try:
#     subprocess.run(["/Users/tristanshin/Desktop/pythonProject/shutdown_script.sh"], check=True)
# except subprocess.CalledProcessError as e:
#     print("Error:", e)





