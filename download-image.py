import bs4
import requests
from selenium import webdriver
import os
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def download_image(url,folder_name,num):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder_name,str(num)+".jpg"),'wb') as file:
            file.write(response.content)


start = 'https://www.google.com/search?q='
end = '&tbm=isch'
search = input('search what:')

folder_name = search
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

url = start + search + end
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
a = input("waiting...press'1' to continue")

#print how many images we had
driver.execute_script("window.scrollTo(0,0);")
page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html,'html.parser')
containers = pageSoup.findAll('div',{'class':"isv-r PNCib MSM1fd BUooTd"})
len_containers = len(containers)
print(len_containers)

for i in range(1,len_containers+1):
    if i % 25 != 0:
        xpath = """//*[@id="islrg"]/div[1]/div[%s]"""%(i)

        #Grabbing the URL of the small preview image
        previewImageXpath = """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img"""%(i)
        previewImageElement = driver.find_element_by_xpath(previewImageXpath)
        previewImageURL = previewImageElement.get_attribute("src"'')

        #click on the image container
        driver.find_element_by_xpath(xpath).click()
        timeStarted = time.time()
        #//*[@id="islrg"]/div[1]/div[102]/a[1]/div[1]/img
        #//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img
        while True:
            imageElement = driver.find_element_by_xpath("""//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img""")
            imageURL = imageElement.get_attribute('src')
            if imageURL != previewImageURL:
                print("number of image:",i)
                print("actual URL", imageURL)
                break
            else:
                currentTime = time.time()
                if currentTime-timeStarted>10:
                    print("Timeout!")
                    break
        try:
            download_image(imageURL,folder_name,i)
        except:
            print("Couldn't download an image %s "%(i))

exit = input('download is finish,press 1 to exit')
