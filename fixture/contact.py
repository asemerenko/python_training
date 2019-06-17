from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # Go to add contact form
        wd.find_element_by_link_text("add new").click()
        # Fill contact form
        self.change_contact_field_value("firstname", contact.firstname)
        self.change_contact_field_value("lastname", contact.lastname)
        self.change_contact_field_value("nickname", contact.nickname)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("email", contact.email)
        self.select_contact_value("bday", contact.bday)
        self.select_contact_value("bmonth", contact.bmonth)
        self.change_contact_field_value("byear", contact.byear)
        # Submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.go_to_home_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        # Open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # Fill contact form
        self.change_contact_field_value("firstname", contact.firstname)
        self.change_contact_field_value("lastname", contact.lastname)
        self.change_contact_field_value("nickname", contact.nickname)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("email", contact.email)
        self.select_contact_value("bday", contact.bday)
        self.select_contact_value("bmonth", contact.bmonth)
        self.change_contact_field_value("byear", contact.byear)
        # Submit contact modification
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.go_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='selected[]'])[1]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def select_contact_value(self, select_param, select_value):
        wd = self.app.wd
        if select_value is not None:
            wd.find_element_by_name(select_param).click()
            Select(wd.find_element_by_name(select_param)).select_by_visible_text(select_value)
            wd.find_element_by_xpath("//option[@value='" + select_value + "']").click()

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def go_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()