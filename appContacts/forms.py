from django.forms import ModelForm
from .models import BusinessContact, PersonalContact, ChildContact


class BusinessContactForm(ModelForm):
    class Meta:
        model = BusinessContact

        fields = ('businessType', 'businessName', 'contactName', 'contactPosition', 'email', 'skype', 'website',
                  'facebook', 'address1', 'address2', 'postalCode', 'country', 'country_code', 'city', 'state', 'officePhone',
                  'officePhoneExt', 'mobilePhone', 'tollPhone', 'tollPhoneExt', 'fax', 'note')


class PersonalContactForm(ModelForm):
    class Meta:
        model = PersonalContact

        fields = ('contactType', 'firstName', 'middleName', 'lastName',
                  'birthday', 'emailPersonal', 'emailWork', 'skype',
                  'company', 'website',  'facebook',
                  'address1', 'address2',
                  'country_code', 'country', 'city', 'state', 'postalCode',
                  'homePhone', 'mobilePhone', 'workPhone', 'workPhoneExt',
                  'spouseBirthday', 'spouseFirstName', 'spouseMiddleName', 'spouseLastName',
                  'spouseMobilePhone', 'spouseWorkPhone', 'spouseworkPhoneExt',
                  'spouseEmailPersonal', 'spouseEmailBusiness', 'note')


class ChildForm(ModelForm):
    class Meta:
        model = ChildContact

        fields = ('firstName',  'lastName', 'birthday')
