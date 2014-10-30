from django.test import TestCase
from tasks42.models import Person
from datetime import date


class MainViewTest(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.me = Person(
            name="Evhen",
            surname="Davliud",
            date_of_birth=date(1983, 7, 21),
            bio="I was born in Lubetch Chernigov region Ukraine. In 1995 moved to Belarus. In 2001-2006 studied in The Belarusian State University of Informatics and Radioelectronics.",
            email="dzh21@tut.by",
            jabber="dzh@default.rs",
            skype="dzha21",
            other_contacts="phone +375297602862",
        )

    def test_root_url(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'home.html')

        persons_in_context = response.context['persons']

        self.assertEquals(persons_in_context[0].name, self.me.name)
        self.assertEquals(persons_in_context[0].surname, self.me.surname)
        self.assertEquals(
            persons_in_context[0].date_of_birth,
            self.me.date_of_birth
        )
        self.assertEquals(persons_in_context[0].bio, self.me.bio)
        self.assertEquals(persons_in_context[0].email, self.me.email)
        self.assertEquals(persons_in_context[0].jabber, self.me.jabber)
        self.assertEquals(persons_in_context[0].skype, self.me.skype)
        self.assertEquals(
            persons_in_context[0].other_contacts,
            self.me.other_contacts
        )

        self.assertIn(self.me.name, response.content)
        self.assertIn(self.me.surname, response.content)
        self.assertIn(
            self.me.date_of_birth.strftime('%B %d, %Y'),
            response.content
            )
        self.assertIn(self.me.bio, response.content)
        self.assertIn(self.me.email, response.content)
        self.assertIn(self.me.jabber, response.content)
        self.assertIn(self.me.skype, response.content)
        self.assertIn(self.me.other_contacts, response.content)

        # test requests link
        self.assertIn('requests', response.content)
        response = self.client.get('/requests/')
        self.assertEquals(response.status_code, 200)


class RequestsViewTest(TestCase):

    def test_requests_link(self):
        response = self.client.get('/requests/')
        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'requests.html')

        # context
        requests_in_context = response.context['requests']
        self.assertEquals(len(list(requests_in_context)) > 0, True)

        # content
        self.assertIn('Request #', response.content)
