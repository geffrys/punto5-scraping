from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.edge.service import Service as ServiceEdge
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

SITE = "https://www.viajesexito.com/"

CHECK_IN = "16-12-2023"
CHECK_OUT = "26-12-2023"

AEROPUERTO = "JOSE MARIA CORDOBA"

# 2 habitaciones, 1 habitacion doble, 1 habitacion sencilla, 3 pasajeros

def serviceSelect(explorer='chrome'):
    if explorer == 'edge':
        return webdriver.Edge(service=serviceEdge)
    return webdriver.Chrome(service=serviceChrome)

serviceChrome = ServiceChrome('driver/chromedriver.exe')
serviceEdge = ServiceEdge('driver/msedgedriver.exe')


driver = serviceSelect(explorer='edge')

driver.get(SITE)
# cerramos la publicidad
# publicidad = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/svg/path')
# publicidad = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/svg/path')))
# publicidad.click()
time.sleep(5)
modal = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/svg/path')
driver.execute_script("arguments[0].querySelector('button.nombre_de_la_clase_del_boton_de_cierre').click();", modal)

time.sleep(2)
print("Publicidad cerrada")

check_ = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/input')
check_.click()
time.sleep(2)
date_checkin = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/div[2]/div[1]')
date_checkin.click()
time.sleep(2)
date_checkout = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[2]/div[2]/div[1]')
time.sleep(2)