import unittest
from selenium import webdriver

class NoteTest(unittest,Testcase):
    def setup(self):
        self.browser = webdriver.Chrome()
    def teardown(self):
        self.browser.quit()
    # Sompong heard about a cool new note app
    #he goes to check out it's homepage
    def test_can_start_note_app(self):
        self.browser.get("http://localhost:8000")

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

    #satified, he goes back to sleep

    if __name__ == "__main__":  
      unittest.main()  

