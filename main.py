from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://teoria.on.ge/exam")
element = driver.find_element_by_id("start")
autonext = driver.find_element_by_id("auto-next-step")
print("TRYING TO START THE GAME")
element.click()
print("WAITING...")
time.sleep(7) # increase time if it isnt working properly
print("STARTED!")
autonext.click()
start = 0
end = 30
for start in range(end):
 driver.execute_script("document.querySelectorAll('[data-is-correct-list]')[0].click();")
 time.sleep(0.5) # LOW = MORE CHANCE TO CLICK WRONGLY (RECOMMENDED: 0.5 FOR THE FASTEST ONE, 1/0.7/0.8 FOR SLOWEST ONE OR )
print("DONE ))")