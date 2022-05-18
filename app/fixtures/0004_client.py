from dynamic_fixtures.fixtures import BaseFixture

from django_keycloak.models import Realm, Client


class Fixture(BaseFixture):

    dependencies = (
        ('app', '0003_realm'),
    )

    def load(self):
        realm = Realm.objects.get(name='antenatal-realm')

        Client.objects.get_or_create(
            realm=realm,
            client_id='antenatal-back-end',
            secret='145a828b-bbb1-44b0-81f5-d3d669ab59f7'
        )
