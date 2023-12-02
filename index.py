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
DESTINO = "Punta Cana"

# 2 habitaciones, 1 habitacion doble, 1 habitacion sencilla, 3 pasajeros

def serviceSelect(explorer='chrome'):
    serviceChrome = ServiceChrome('driver/chromedriver.exe')
    serviceEdge = ServiceEdge('driver/msedgedriver.exe')
    if explorer == 'edge':
        return webdriver.Edge(service=serviceEdge)
    return webdriver.Chrome(service=serviceChrome)





def cerrarPublicidad(driver):
    iframePublicidad = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/iframe'))
    )
    driver.switch_to.frame(iframePublicidad)
    time.sleep(1)
    close_modal = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]')
    close_modal.click()
    time.sleep(2)
    driver.switch_to.default_content()
    time.sleep(2)

def cerrarPublicidadPaginaResultados(driver):
    
    iframePublicidad = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/iframe'))
    )
    driver.switch_to.frame(iframePublicidad)
    time.sleep(1)
    close_modal = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]')
    close_modal.click()
    time.sleep(2)
    driver.switch_to.default_content()
    time.sleep(2)

def seleccionarFechas(driver):
    check_ = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/input')
    check_.click()
    time.sleep(2)
    date_checkin = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/div[2]/div[1]')
    date_checkin.click()
    time.sleep(2)
    date_checkout = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[2]/div[2]/div[1]')
    date_checkout.click()
    time.sleep(2)
    aceptar = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[2]/div[3]/button[2]')
    aceptar.click()
    time.sleep(2)

def seleccionarHabitaciones(driver):
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div/div/p').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[4]/div[2]/div[1]/button[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/button').click()
    time.sleep(2)

def inputDestino(driver):
    destino = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/div/div/div/input')
    destino.click()
    time.sleep(2)
    destino = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[5]/div[2]/input')
    time.sleep(2)
    destino.send_keys(DESTINO)
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[5]/ul/li[1]').click()
    time.sleep(2)

def mostrarResultados(driver):
    resultados = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '/html/body/app-root/app-web-layout/div/div[2]/app-search/div/div[2]/div/div[2]/div[2]/hotel-result/div'))
    )
    # imprimir resultados 
    print(resultados.__len__())
    print('-----------------------')
    for resultado in resultados:
        print(resultado.text)
        print('-----------------------')


def __main__():
    driver = serviceSelect(explorer='edge')
    driver.get(SITE)
    time.sleep(2)
    cerrarPublicidad(driver)
    seleccionarFechas(driver)
    seleccionarHabitaciones(driver)
    inputDestino(driver)
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[4]/a').click()
    time.sleep(8)
    # cambio a la ventana de paquetes
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    cerrarPublicidadPaginaResultados(driver)
    mostrarResultados(driver)
    time.sleep(2)
    # Cambio de ventana
    driver.switch_to.window(driver.window_handles[0])
    # whatsapp
    driver.find_element(By.XPATH, '/html/body/form/div[9]/a/img').click()
    time.sleep(20)
    driver.close()
    driver.quit()

__main__()
