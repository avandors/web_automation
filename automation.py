from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.youtube.com/index')

searchBox = driver.find_element_by_xpath('//*[@id="search"]')
searchBox.send_keys('Jonas Blue - Mama ft. William Singe (Official Video)')

#find search icon
searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()

searchSong = driver.find_element_by_xpath('//*[@id="dismissible"]/div')
searchSong.click()
