from base import Setting, SettingSet
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import PasswordInput

EMAIL_SET = SettingSet('email', _('Email settings'), _("Email server and other email related settings."), 50)

EMAIL_HOST = Setting('EMAIL_HOST', '', EMAIL_SET, dict(
label = _("Email Server"),
help_text = _("The SMTP server through which your application will be sending emails."),
required=False))

EMAIL_PORT = Setting('EMAIL_PORT', 25, EMAIL_SET, dict(
label = _("Email Port"),
help_text = _("The port on which your SMTP server is listening to. Usually this is 25, but can be something else."),
required=False))

EMAIL_HOST_USER = Setting('EMAIL_HOST_USER', '', EMAIL_SET, dict(
label = _("Email User"),
help_text = _("The username for your SMTP connection."),
required=False))

EMAIL_HOST_PASSWORD = Setting('EMAIL_HOST_PASSWORD', '', EMAIL_SET, dict(
label = _("Email Password"),
help_text = _("The password for your SMTP connection."),
required=False,
widget=PasswordInput))

EMAIL_USE_TLS = Setting('EMAIL_USE_TLS', False, EMAIL_SET, dict(
label = _("Use TLS"),
help_text = _("Does your SMTP server usFes TLS for authentication."),
required=False))

DEFAULT_FROM_EMAIL = Setting('DEFAULT_FROM_EMAIL', '', EMAIL_SET, dict(
label = _("Site 'from' email address"),
help_text = _("The address that will show up on the 'from' field on emails sent by your website."),
required=False))

EMAIL_SUBJECT_PREFIX = Setting('EMAIL_SUBJECT_PREFIX', '', EMAIL_SET, dict(
label = _("Email subject prefix"),
help_text = _("Every email sent through your website will have the subject prefixed by this string. It's usually a good idea to have such a prefix so your users can easilly set up a filter on theyr email clients."),
required=False))

EMAIL_FOOTER_TEXT = Setting(u'EMAIL_FOOTER_TEXT', '', EMAIL_SET, dict(
label = _("Email Footer Text"),
help_text = _("Email footer text, usually \"CAN SPAM\" compliance, or the physical address of the organization running the website. See <a href=\"http://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003\">this Wikipedia article</a> for more info."),
required=False))

EMAIL_DIGEST_CONTROL = Setting('EMAIL_DIGEST_CONTROL', None)
