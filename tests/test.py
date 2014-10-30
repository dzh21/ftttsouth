# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase


class Tasks42Test(LiveServerTestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.close()

    def _test_admin_site_for_person(self):
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        persons_links = self.browser.find_elements_by_link_text('Persons')
        self.assertEquals(len(persons_links), 1)

        persons_links[0].click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Persons', body.text)

        new_person_link = self.browser.find_element_by_link_text('Add person')
        new_person_link.click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Name:', body.text)

        self.browser.find_element_by_name('name').send_keys('Vasya')
        self.browser.find_element_by_name('surname').send_keys('Pupkin')
        self.browser.find_element_by_name('date_of_birth'). \
            send_keys('1983-12-31')
        self.browser.find_element_by_name('bio'). \
            send_keys('Hi. My bio is too poor...')
        self.browser.find_element_by_name('email'). \
            send_keys('Pupkin@gmail.com')
        self.browser.find_element_by_name('jabber'). \
            send_keys('Pupkin@jabber.com')
        self.browser.find_element_by_name('skype').send_keys('Pupkin')
        self.browser.find_element_by_name('other_contacts'). \
            send_keys('phone: none')

        self.browser.find_element_by_css_selector("input[value='Save']"). \
            click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Vasya Pupkin', body.text)

    def _test_home_page(self):
        self.browser.get(self.live_server_url)

        heading = self.browser.find_element_by_tag_name('h3')
        self.assertEquals('42 Coffee Cups Test Assignment', heading.text)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Evhen', body.text)
        self.assertIn('Davliud', body.text)
        self.assertIn('dzh21@tut.by', body.text)

        self.browser.find_element_by_link_text('requests').click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Request #', body.text)

    def _test_requests_page(self):
        self.browser.get(self.live_server_url + '/requests/')

        heading = self.browser.find_element_by_tag_name('h4')
        self.assertIn('Requests', heading.text)

        requests_elems = self.browser.find_elements_by_partial_link_text(
            "Request #"
        )
        self.assertEquals(len(requests_elems) > 0, True)

    def test_admin_requests_page(self):
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('admin')
        password_field.send_keys(Keys.RETURN)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        persons_links = self.browser.find_elements_by_link_text(
            'Request objects'
        )
        self.assertEquals(len(persons_links), 1)

        persons_links[0].click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Remote address', body.text)
        self.assertIn('Event date time', body.text)
