from selenium import webdriver

browser = webdriver.Firefox()

#edith has heard about a cool new online to-do app. She goes 
#to check out its homepage

browser.get('http://localhost:8000')

#she notices the page title ahd header mention to-do lists

assert 'To-Do' in browser.title

#she is invited to enter a to-do item straight away

#she types "Buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)


#when she hits enter, the page updates, and now the page lists 
# "1: Buy peacock feathers" as an item in a to-do list

#There is still a text box inviting her to add another item. She
#enters "Use peacock feathers to make fly" (Edith is very methodical)

#The page updates again, and now shows both items on her list
#Edith wonders whether the site will remember her list. Then she sees 
#that site has generated a unique URL for her --- ther is one
#explanatory text to that effects.

#she visits that URL - her to-do list is still there.

#Satisfied, she goes back to sleep

browser.quit()


