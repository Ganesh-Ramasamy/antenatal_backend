from dynamic_fixtures.fixtures import BaseFixture

from django_keycloak.models import Realm, Client


class Fixture(BaseFixture):

    dependencies = (
        ('app', '0003_realm'),
    )

    def load(self):
        realm = Realm.objects.get(name='example')

        Client.objects.get_or_create(
            realm=realm,
            client_id='resource-provider-api',
            secret='z91J0XCEIcz7qQTfZeY5MbDaiTwLQyy7'
        )
