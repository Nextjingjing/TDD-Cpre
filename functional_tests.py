import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class NoteTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    def tearDown(self):
        self.browser.quit()

    # Sompong heard about a cool new note app
    #he goes to check out it's homepage
    def test_can_start_note_app(self):
        self.browser.get("http://localhost:5173/")

    # he notices the page title and header mention notes
        self.assertIn("notes", self.browser.title)
    #he is invited to enter a note straight away
        self.fail("Finish the test!")

    #he types "Math","https://example.com/ma-notes.pdf" and "calculus"into Name, File URL , Tags into a text box

    #when he hits enter , the page updates, and now the page lists
    #"Math","https://example.com/ma-notes.pdf" and "cacd blculus"
    #after he add note now he want to delete a note
    #he clck delete button ]
    #after he click delete button page have box to confirm delete
    #he confirm to delete note
    #after he delete a note he don't see a note a=name "math2"

    #satisfied, he goes back to sleep
 

class SearchTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()
        # sompong want to test search feature
    # he notices the page title and header mention search

    def test_search_feature(self):
        self.browser.get("http://localhost:5173/")


    # he type "intro" into a text box
        search_input = self.browser.find_element(By.ID, "search-input")
        search_input.send_keys("intro")
        search_input.send_keys(Keys.ENTER)

    # when he hits enter, the page show information about Introduction to Django
        # detail of note math have name "Introduction to Django" 
        click_tag_search = self.browser.find_element(By.ID, "search-tags")
        click_tag_search.click()

        results = self.browser.find_element(By.ID, "notes-list").text
        self.assertIn("Introduction to Django", results)

    # then he fill "z" in search box
        search_input = self.browser.find_element(By.ID, "search-input")
        search_input.clear()
        search_input.send_keys("z")
        search_input.send_keys(Keys.ENTER)


    # then he saw text say "files not found"
        click_name_search = self.browser.find_element(By.ID, "search-name")
        click_name_search.click()


        no_results_text = self.browser.find_element(By.ID, "no-results").text
        self.assertIn("ไม่พบโน้ตที่ค้นหา", no_results_text)


    #satified, he goes back to sleep
if __name__ == "__main__":
    unittest.main()

