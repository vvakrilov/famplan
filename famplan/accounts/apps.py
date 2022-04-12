from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'famplan.accounts'

    def ready(self):
        import famplan.accounts.signals # noqa
