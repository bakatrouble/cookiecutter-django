from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'velly_back.users'
    verbose_name = "Users"

    def ready(self):
        pass
