from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


WINDOW_SIZE = "1920,1080"

test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

chorme_options = Options()
#chorme_options.add_argument("--headless")
chorme_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chorme_options.add_argument(f'--user-agent={test_ua}')
chorme_options.add_argument('--no-sandbox')
#chorme_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chorme_options)

driver.get("https://quillbot.com/")
time.sleep(2)
driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

driver.find_element(By.XPATH, "//*[text()='Spanish']").click()

textarea = driver.find_element(By.ID, "paraphraser-input-box")

textarea.send_keys("El oeste de Texas divide la frontera entre Mexico y Nuevo México. Es muy bella pero aspera, llena de cactus, en esta region se encuentran las Davis Mountains. Todo el terreno esta lleno de piedra caliza, torcidos arboles de mezquite y espinosos nopales. Para admirar la verdadera belleza desertica, visite el Parque Nacional de Big Bend, cerca de Brownsville. Es el lugar favorito para los excurcionistas, acampadores y entusiastas de las rocas. Pequeños pueblos y ranchos se encuentran a lo largo de las planicies y cañones de esta region. El area solo tiene dos estaciones, tibia y realmente caliente. La mejor epoca para visitarla es de Diciembre a Marzo cuando los dias son tibios, las noches son frescas y florecen las plantas del desierto con")
textarea.click()

action = ActionChains(driver);
action.key_down(Keys.CONTROL).key_down(Keys.RETURN).key_up(Keys.RETURN).key_up(Keys.CONTROL).perform();
time.sleep(5)
content = driver.find_element(By.ID, "paraphraser-output-box").text

with open('nuevotexto.txt','a', encoding='utf-8') as f:
    f.write(content)

