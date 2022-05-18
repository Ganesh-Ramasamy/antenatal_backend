from dynamic_fixtures.fixtures import BaseFixture

from django_keycloak.models import Server


class Fixture(BaseFixture):

    def load(self):
        Server.objects.get_or_create(
            url='http://localhost:8081'
        )
