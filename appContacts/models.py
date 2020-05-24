import uuid
from django.db import models
from datetime import datetime, timedelta
from appContacts.choices import COUNTRYCODE, STATECODE, CONTACTTYPE


class PersonalContact(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contactType = models.CharField(
        max_length=50, choices=CONTACTTYPE, default='Family')
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100, blank=True)
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    postalCode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True,
                             choices=STATECODE, default='Ontario')
    country = models.CharField(
        max_length=50, blank=True, choices=COUNTRYCODE, default='Canada')
    country_code = models.CharField(max_length=20, blank=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    company = models.CharField(max_length=100, blank=True)
    emailPersonal = models.EmailField(max_length=100, blank=True)
    emailWork = models.EmailField(max_length=100, blank=True)
    skype = models.CharField(max_length=25, blank=True)
    website = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(null=True, blank=True)
    homePhone = models.CharField(max_length=25, blank=True)
    mobilePhone = models.CharField(max_length=25, blank=True)
    workPhone = models.CharField(max_length=25, blank=True)
    workPhoneExt = models.CharField(max_length=5, blank=True)
    spouseFirstName = models.CharField(max_length=100, blank=True)
    spouseLastName = models.CharField(max_length=100, blank=True)
    spouseMiddleName = models.CharField(max_length=100, blank=True)
    spouseEmailPersonal = models.EmailField(max_length=100, blank=True)
    spouseEmailBusiness = models.EmailField(max_length=100, blank=True)
    spouseMobilePhone = models.CharField(max_length=25, blank=True)
    spouseWorkPhone = models.CharField(max_length=25, blank=True)
    spouseworkPhoneExt = models.CharField(max_length=5, blank=True)
    spouseBirthday = models.DateField(null=True, blank=True)
    note = models.CharField(max_length=500, blank=True)
    create_date = models.DateTimeField(default=datetime.now)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "personal_contacts"
        ordering = ["lastName"]

    def __str__(self):
        return self.lastName


class ChildContact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey(PersonalContact, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100, blank=True)
    middleName = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "child_contacts"

    def __str__(self):
        return (self.firstName) + ' ' + (self.lastName)


class BusinesType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "business_type"

    def __str__(self):
        return self.name


class BusinessContact(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    businessName = models.CharField(max_length=100)
    businessType = models.ForeignKey(BusinesType, on_delete=models.CASCADE)
    contactName = models.CharField(max_length=150, blank=True)
    contactPosition = models.CharField(max_length=100, blank=True)
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    postalCode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True, choices=STATECODE)
    country = models.CharField(max_length=50, blank=True, choices=COUNTRYCODE)
    country_code = models.CharField(max_length=20, blank=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    officePhone = models.CharField(max_length=25, blank=True)
    officePhoneExt = models.CharField(max_length=10, blank=True)
    mobilePhone = models.CharField(max_length=25, blank=True)
    tollPhone = models.CharField(max_length=25, blank=True)
    tollPhoneExt = models.CharField(max_length=10, blank=True)
    fax = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    skype = models.CharField(max_length=25, blank=True)
    website = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    note = models.CharField(max_length=500, blank=True)
    create_date = models.DateTimeField(default=datetime.now)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "business_contacts"
        ordering = ["businessName"]

    def __str__(self):
        return self.businessName
