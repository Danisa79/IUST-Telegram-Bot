import requests
from bs4 import BeautifulSoup
page = requests.get('https://www.time.ir/')
soup = BeautifulSoup(page.text, 'html.parser')
azansobh = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanMorning'})[0] #1
toloo = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunrise'})[0] #2
azanzohr = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNoon'})[0] #3
ghoroob = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanSunset'})[0] #4
azanmaghreb = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblAzanNight'})[0] #5
nimeshabeshari = soup.find_all('span', {'id' : 'ctl00_cphTop_Sampa_Web_View_EphemerisUI_EphemerisByCity12cphTop_3736_lblMidNight'})[0] #6
print(azansobh.text) #1
print(toloo.text) #2
print(azanzohr.text) #3
print(ghoroob.text) #4
print(azanmaghreb.text) #5
print(nimeshabeshari.text) #6