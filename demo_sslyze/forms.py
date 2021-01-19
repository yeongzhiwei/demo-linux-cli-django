from django import forms
from django.core.validators import RegexValidator

hostname_validator = RegexValidator(r"^[A-Za-z0-9]+\.([A-Za-z0-9]+\.)*[A-Za-z0-9]+$", "The value is not a valid hostname e.g. a.b.com")
ip_addr_validator = RegexValidator(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", "The value is not a valid IPv4 e.g. 1.1.1.1")

class HostForm(forms.Form):
    hostname = forms.CharField(initial='www.google.com', validators=[hostname_validator], required=True)
    ip_addr = forms.CharField(initial='172.217.194.106', validators=[ip_addr_validator], required=True)
