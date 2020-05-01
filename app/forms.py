from django import forms

CHOICE_HOUR = [
    ('NIE WYBRANO', 'Preferowana godzina'),
    ('8.00 - 9.00', '8.00 - 9.00'),
    ('9.00 - 10.00', '9.00 - 10.00'),
    ('10.00 - 11.00', '10.00 - 11.00'),
    ('11.00 - 12.00', '11.00 - 12.00'),
    ('12.00 - 13.00', '12.00 - 13.00'),
    ('14.00 - 15.00', '14.00 - 15.00'),
    ('15.00 - 16.00', '15.00 - 16.00'),
    ('16.00 - 17.00', '16.00 - 17.00'),
    ('17.00 - 18.00', '17.00 - 18.00'),
    ('Po 18', 'Po 18'),
]

TYPE_WEBSITE = [
    ('Portal internetowy', 'Portal internetowy'),
    ('Sklep internetowy', 'Sklep internetowy'),
    ('Strona wizytówka', 'Strona wizytówka'),
]

class EmailContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Imię',
                           widget=forms.TextInput(attrs={'placeholder': 'Podaj imię...'}))
    phone = forms.CharField(max_length=20, required=False, label='Numer telefonu',
                            widget=forms.TextInput(attrs={'placeholder': 'Podaj numer telefonu...'}))
    e_mail = forms.EmailField(label='E-mail',
                              widget=forms.TextInput(attrs={'placeholder': 'Podaj adres e-mail...'}))
    context = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Treść wiadomości...',
                                                           'rows': 4,}), label='Treść wiadomości')

class BasicContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Imię',
                           widget=forms.TextInput(attrs={'placeholder': 'Podaj imię...'}))
    e_mail = forms.EmailField(label='E-mail',
                              widget=forms.EmailInput(attrs={'placeholder': 'Podaj e-mail...'}),)
    phone = forms.CharField(max_length=20, required=False, label='Numer telefonu',
                            widget=forms.TextInput(attrs={'placeholder': 'Podaj numer telefonu...'}))
    topic = forms.CharField(max_length=400, label='Temat wiadomosci',
                            widget=forms.TextInput(attrs={'placeholder': 'Temat wiadomości...'}))
    context = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Treść wiadomości...'}), label='Treść wiadomości',
                              )

class PhoneContactForm(forms.Form):
    number = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Numer telefonu...'}))
    data_contact = forms.ChoiceField(choices=CHOICE_HOUR, label='')

class ValuationForm(forms.Form):
    type = forms.ChoiceField(choices=TYPE_WEBSITE, label='Typ strony internetowej')
    context = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Opisz funkcjonalności, co oczekujesz, aby twoja strona posiadała lub w jaki sposób działał...'})
                              , label='Funkcjonalności i opis',)
    name = forms.CharField(max_length=100, label='Imię',
                           widget=forms.TextInput(attrs={'placeholder': 'Podaj imię...'}))
    e_mail = forms.EmailField(label='E-mail',
                              widget=forms.EmailInput(attrs={'placeholder': 'Podaj e-mail...'}),)
    phone = forms.CharField(max_length=20, required=False, label='Numer telefonu',
                            widget=forms.TextInput(attrs={'placeholder': 'Podaj numer telefonu...'}))


