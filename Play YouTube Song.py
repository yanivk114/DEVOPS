from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://youtube.com")
# Write name of song in send_keys("SONG NAME")
song = driver.find_element_by_name("search_query").send_keys("sweet chile omine") #Write name of sone here
driver.find_element_by_id("search-icon-legacy").click()
driver.find_element_by_id("video-title").click()