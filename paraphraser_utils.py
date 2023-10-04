from selenium import webdriver
from selenium.webdriver.firefox.options import Options as fr_opt 
from selenium.webdriver.chrome.options import Options as chr_opt 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.service import Service as fr_Service
from selenium.webdriver.chrome.service import Service as chr_Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from art import *
import time
driver=None
firstInit=True
def getOptions(configMode):
    WINDOW_SIZE = "1920,1080"

    config = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'
    if configMode=="Firefox":
        nav_options = fr_opt()
    elif configMode=="Chrome":
        nav_options = chr_opt()
        nav_options.add_experimental_option("detach", True)
        
    nav_options.add_argument("--headless")
    nav_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    nav_options.add_argument(f'--user-agent={config}')
    nav_options.add_argument('--no-sandbox')
    return nav_options
    

    
    
def quitCoockies():
    global driver
    try:
        driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        return True
    except:
        return False

def deleteText():
    global driver
    try:
        element = driver.find_element(By.CSS_SELECTOR, "svg[data-testid='DeleteOutlineIcon']")
        element.click()
        time.sleep(2)
        button = driver.find_element(By.XPATH, "//button[text()='Continue']")
        button.click()
        return True
    except :
        return False
        
def selectSpanish(data):
    global firstInit,driver
    try:
        if firstInit:
            driver.find_element(By.XPATH, "//*[text()='Spanish']").click()
            firstInit=False
        else:
            while not deleteText():
                time.sleep(1)
            time.sleep(2)
        textarea = driver.find_element(By.ID, "paraphraser-input-box")
        textarea.send_keys(data)
        time.sleep(2)
        
        action = ActionChains(driver)
        action.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        time.sleep(5)
        content = driver.find_element(By.ID, "paraphraser-output-box").text
        
        return content
    except :
        return None



def runScript(data,configMode):
    global driver,firstInit
    
    if firstInit:
        if configMode=="Firefox":
            service=fr_Service(log_path='/dev/null')
            driver = webdriver.Firefox(options=getOptions(configMode=configMode),service=service)
        elif configMode=="Chrome":
            service=chr_Service(log_path='/dev/null')
            driver = webdriver.Chrome(options=getOptions(configMode=configMode),service=service)
        driver.get("https://quillbot.com/")
        time.sleep(2)
        while not quitCoockies():
            time.sleep(1)
    result = None
    while result is None:
        result = selectSpanish(data=data)
        if result is None:
            time.sleep(1)
    return result


def paraphrase(data,limitWords=125,configMode="Firefox"):
    tprint("\tWelcome...")
    global driver
    from datetime import datetime
    now = datetime.now()
    result=""
    words = data.split(' ')
    total_blocks = (len(words) + limitWords - 1) // limitWords  
    for i in range(0, len(words), limitWords):
        current_block = i // limitWords + 1 
        print(f'working {current_block}/{total_blocks}...')
        batch = ' '.join(words[i:i+limitWords])
        result+=runScript(batch,configMode)
        time.sleep(3)
    with open(f'pf_{now.strftime("%H:%M:%S")}.txt','a', encoding='utf-8') as f:
        f.write(result)
    driver.close()
    tprint("Job is done")

    


