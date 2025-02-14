from wagtail.tests.utils import WagtailPageTests

from ..models import People, Person
from ...home.models import HomePage
from ...content.models import ContentPage


class PersonTests(WagtailPageTests):
    """Tests for the Person model."""

    def test_person_parent_pages(self):
        self.assertAllowedParentPageTypes(Person, {People})

    def test_person_subpages(self):
        self.assertAllowedSubpageTypes(Person, {})


class PeopleTests(WagtailPageTests):
    """Tests for the People model."""

    def test_people_parent_pages(self):
        self.assertAllowedParentPageTypes(People, {HomePage, ContentPage})

    def test_people_subpages(self):
        self.assertAllowedSubpageTypes(People, {Person})
