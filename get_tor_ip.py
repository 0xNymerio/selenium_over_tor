import subprocess
import ssl
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
import warnings

# Configurando para sites com certificado auto assinado
ssl._create_default_https_context = ssl._create_unverified_context

# Remover o warning do Selenium: DeprecationWarning: capabilities and desired_capabilities have been deprecated, please pass in a Service object
warnings.filterwarnings("ignore", category=DeprecationWarning) 

# Modo background - no GUI
options = webdriver.FirefoxOptions()
options.add_argument("--headless")

# Buscando o ip
crawl = ['[GET Original IP]', '[GET Tor IP]']
status = ['start', 'stop']
url = 'https://www.myip.com/'

def get_ip(action):

    # Usa o proxy tor?
    if action == '[GET Tor IP]':
        
        # Sobe o serviço tor
        service_tor(status[0])

        # Configurando o profile para utilizar o proxy SOCKSv5 Tor default
        tor_profile = webdriver.FirefoxProfile()
        tor_profile.set_preference('network.proxy.type', 1)
        tor_profile.set_preference('network.proxy.socks', '127.0.0.1')
        tor_profile.set_preference('network.proxy.socks_port', 9050)
        tor_profile.set_preference('network.proxy.socks_version', 5)

        driver = webdriver.Firefox(firefox_profile=tor_profile, options=options, executable_path='./geckodriver')

    elif action == '[GET Original IP]':
        driver = webdriver.Firefox(options=options, executable_path='./geckodriver')

    else: 
        print('dude, wtf')
        exit()

    driver.get('https://www.myip.com/')

    try:
        ip = driver.find_element(By.XPATH, '//*[@id="ip"]')
        host = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div/div/ul/li[2]/div[2]')
        country = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]')

        r_ip = ip.text
        r_host = host.text
        r_country = country.text

    except:
        r_ip = "Erro ao Coletar o IP"
        r_host = "Erro ao Coletar o HOST"
        r_country = "Erro ao Coletar o COUNTRY"
        
    r_log = action + ': [IP] ' + r_ip + ' [HOST] ' + r_host + ' [COUNTRY] ' + r_country
    driver.close()

    # Stop no serviço Tor
    if action == '[GET Tor IP]':
        service_tor(status[1])
    
    return r_ip, r_host,r_country, r_log
    
def service_tor(status):
    try:
        subprocess.run(["systemctl", str(status), "tor"])
    except:
        print('wtf, no Tor bro')

# 0-NORMAL IP| 1-Tor IP
ip, host, country, log = get_ip(crawl[0])
tor_ip, tor_host, tor_country, tor_log = get_ip(crawl[1])

print(log)
print(tor_log)



