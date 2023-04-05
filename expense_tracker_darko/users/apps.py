from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "expense_tracker_darko.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import expense_tracker_darko.users.signals  # noqa: F401
        except ImportError:
            pass
