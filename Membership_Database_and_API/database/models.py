from django.db import models
from .specifications import TITLE, PROFESSIONS, STAFF_POSITIONS, NATURE_OF_BUSINESS, GENDER, NATIONALITIES, DIRECTOR_POSITIONS, reg_no_validator
from django.contrib.auth.models import AbstractUser, BaseUserManager
from PIL import Image

# CustomManager's model
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("Username cannot be empty!")
        if not email:
            raise ValueError('Email cannot be empty!')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)

# CustomUser's model
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, null=False, blank=False, error_messages={'required': 'Email cannot be empty!'})
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(("last login"), blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()
    
# Staff's model
class Staff(models.Model):
    first_name = models.CharField(max_length=100, error_messages=
                                 {'required': 'first_name cannot be empty!', 'max_length': 'first_name length cannot be more than 100 characters!'}, null=False, blank=False)
    last_name = models.CharField(max_length=100, error_messages=
                                {'required': 'last_name cannot be empty!', 'max_length': 'Latname length cannot be more than 100 characters!'}, null=False, blank=False)
    email = models.EmailField(unique=True, error_messages = 
                              {'required': 'Email cannot be empty!', 'invalid': 'Invalid email address'}, null=False, blank=False)
    address = models.TextField( error_messages=
                               {'required': 'Address cannot be empty!', 'max_length': 'Address cannot be more than 200 characters!'}, null=False, blank=False)
    phonenumber = models.CharField(max_length=15, error_messages=
                                   {'required': 'Phonenumber is required!', 'max_length': 'Phonenumber cannot be more than 15 digits!'}, help_text='Enter a valid phone number e.g "+234 803 5674 908, OR +36 201 2345 67 Or any valid number"', unique=True, null=False, blank=False)
    gender = models.CharField(max_length=7, choices=GENDER, error_messages={'required': 'Gender cannot be empty!'}, null=False, blank=False)
    nationality = models.CharField(max_length=100,choices=NATIONALITIES, default=NATIONALITIES[0], error_messages= {'required': 'Nationality cannot be empty!'}, 
                                   null=False, blank=False)
    position = models.CharField(max_length=100, choices=STAFF_POSITIONS, error_messages={'required': 'Position cannot be empty!'}, null=False, blank=False)
    account_number = models.IntegerField(error_messages={'required': 'Account number cannot be empty!'}, null=False, blank=False, unique=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    date_employed = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    past = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """Override save method to resize image while maintaining aspect ratio and validate format."""
        # Validate image format
        self.validate_image_format()

        # Save the image first before resizing
        super().save(*args, **kwargs)

        # Resize the image after saving
        self.resize_image()

    def validate_image_format(self):
        """Validate image format to allow only JPEG, PNG, GIF, and WEBP"""
        if self.profile_photo:
            try:
                img = Image.open(self.profile_photo)
                valid_formats = ["JPEG", "PNG", "GIF", "WEBP"]
                if img.format not in valid_formats:
                    raise ValueError("Unsupported image format. Please upload a JPEG, PNG, GIF, or WEBP file.")
            except Exception as e:
                raise ValueError(f"Invalid image file: {str(e)}")

    def resize_image(self):
        """Resize image while maintaining aspect ratio to max 300x300"""
        if self.profile_photo:
            img_path = self.profile_photo.path
            img = Image.open(img_path)

            # Resize image while maintaining aspect ratio
            img.thumbnail((200, 400))

            # Save resized image (optimize to reduce file size)
            img.save(img_path, optimize=True, quality=85)
    
    def get_full_name(self):
        """Returns the user's full name."""
        return f"{self.first_name} {self.last_name}".strip()

# Director's model
class Director(models.Model):
    first_name = models.CharField(max_length=100, error_messages=
                                 {'required': 'first_name cannot be empty!', 'max_length': 'first_name length cannot be more than 100 characters!'}, null=False, blank=False)
    last_name = models.CharField(max_length=100, error_messages=
                                {'required': 'last_name cannot be empty!', 'max_length': 'Latname length cannot be more than 100 characters!'}, null=False, blank=False)
    email = models.EmailField(unique=True, error_messages = 
                              {'required': 'Email cannot be empty!', 'invalid': 'Invalid email address'}, null=False, blank=False)
    address = models.TextField( error_messages=
                               {'required': 'Address cannot be empty!', 'max_length': 'Address cannot be more than 200 characters!'}, null=False, blank=False)
    phonenumber = models.CharField(max_length=15, error_messages=
                                   {'required': 'Phonenumber is required!', 'max_length': 'Phonenumber cannot be more than 15 digits!'}, help_text='Enter a valid phone number e.g "+234 803 5674 908, OR +36 201 2345 67 Or any valid number"', unique=True, null=False, blank=False)
    gender = models.CharField(max_length=7, choices=GENDER, error_messages={'required': 'Gender cannot be empty!'}, null=False, blank=False)
    nationality = models.CharField(max_length=100,choices=NATIONALITIES,  error_messages= {'required': 'Nationality cannot be empty!'}, 
                                   null=False, blank=False)
    title = models.CharField(max_length=100, choices=TITLE, default=TITLE[0], error_messages={
        'required': 'Title cannot be empty!'}, 
                                   null=False, blank=False
    )
    profession = models.CharField(max_length=100, choices=PROFESSIONS, error_messages={'required': 'Profession cannot be empty!'}, 
                                   null=True, blank=True)
    
    position_in_chambers = models.CharField(max_length=100, choices=DIRECTOR_POSITIONS, error_messages={'required': 'Position cannot be empty!'}, null=False, blank=False)
    company_name = models.CharField(max_length=150, error_messages={'required': 'Company name cannot be empty!'}, 
                                    null=True, blank=True)
    nature_of_business = models.CharField(max_length=150, choices=NATURE_OF_BUSINESS, error_messages={
        'required': 'Nature of Business cannot be empty!'}, null=True,blank=True)
    company_location = models.CharField(max_length=100, error_messages=
                                        {'required': 'Company Location cannot be empty!'}, null=True, blank=True)
    position_in_company = models.CharField(max_length=100, error_messages=
                                        {'required': 'Position in company cannot be empty!'}, null=True, blank=True)
    date_of_establishment = models.IntegerField(error_messages={'required': 'Date of establishment cannot be empty!'}, null=True, blank=True)
    reg_no = models.CharField(max_length=30, unique=True, validators=[reg_no_validator], null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', 
                                      null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    past = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name} ({self.position_in_chambers})"

# Individual member's model
class IndividualMember(models.Model):
    first_name = models.CharField(max_length=100, error_messages=
                                 {'required': 'first_name cannot be empty!', 'max_length': 'first_name length cannot be more than 100 characters!'}, null=False, blank=False)
    last_name = models.CharField(max_length=100, error_messages=
                                {'required': 'last_name cannot be empty!', 'max_length': 'Latname length cannot be more than 100 characters!'}, null=False, blank=False)
    email = models.EmailField(unique=True, error_messages = 
                              {'required': 'Email cannot be empty!', 'invalid': 'Invalid email address'}, null=False, blank=False)
    address = models.TextField(error_messages=
                               {'required': 'Address cannot be empty!', 'max_length': 'Address cannot be more than 200 characters!'}, null=False, blank=False)
    phonenumber = models.CharField(max_length=15, error_messages=
                                   {'required': 'Phonenumber is required!', 'max_length': 'Phonenumber cannot be more than 15 digits!'}, help_text='Enter a valid phone number e.g "+234 803 5674 908, OR +36 201 2345 67 Or any valid number"', unique=True, null=False, blank=False)
    gender = models.CharField(max_length=7, choices=GENDER, error_messages={'required': 'Gender cannot be empty!'}, null=False, blank=False)
    nationality = models.CharField(max_length=100, choices=NATIONALITIES, error_messages={'required': 'Nationality cannot be empty!'}, 
                                   null=False, blank=False)
    profession = models.CharField(max_length=100, choices=PROFESSIONS, error_messages={'required': 'Profession cannot be empty!'}, 
                                   null=False, blank=False)
    title = models.CharField(max_length=100, choices=TITLE, error_messages={
        'required': 'Title cannot be empty!'}, 
                                   null=False, blank=False)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    sponsor = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='individual_member')
    is_active = models.BooleanField(default=True)
    past = models.BooleanField(default=False)
    creator = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='individual_member')

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"

# Corperate member's model
class CorporateMember(models.Model):
    first_name = models.CharField(max_length=100, error_messages=
                                 {'required': 'first_name cannot be empty!', 'max_length': 'first_name length cannot be more than 100 characters!'}, null=False, blank=False)
    last_name = models.CharField(max_length=100, error_messages=
                                {'required': 'last_name cannot be empty!', 'max_length': 'Latname length cannot be more than 100 characters!'}, null=False, blank=False)
    email = models.EmailField(unique=True, error_messages = 
                              {'required': 'Email cannot be empty!', 'invalid': 'Invalid email address'}, null=False, blank=False)
    address = models.TextField(error_messages=
                               {'required': 'Address cannot be empty!', 'max_length': 'Address cannot be more than 200 characters!'}, null=False, blank=False)
    phonenumber = models.CharField(max_length=15, error_messages=
                                   {'required': 'Phonenumber is required!', 'max_length': 'Phonenumber cannot be more than 15 digits!'}, help_text='Enter a valid phone number e.g "+234 803 5674 908, OR +36 201 2345 67 Or any valid number"', unique=True, null=False, blank=False)
    gender = models.CharField(max_length=7, choices=GENDER, error_messages={'required': 'Gender cannot be empty!'}, null=False, blank=False)
    nationality = models.CharField(max_length=100, choices=NATIONALITIES, error_messages={'required': 'Nationality cannot be empty!'}, 
                                   null=False, blank=False)
    title = models.CharField(max_length=100, choices=TITLE, error_messages={
        'required': 'Title cannot be empty!'}, 
                                   null=False, blank=False
    )
    company_name = models.CharField(max_length=150, error_messages={'required': 'Company name cannot be empty!'}, 
                                    null=False, blank=False)
    core_line_of_business = models.CharField(max_length=150, choices=NATURE_OF_BUSINESS, error_messages={
        'required': 'Nature of Business cannot be empty!'}, null=False,blank=False)
    company_interest_in_hungary = models.TextField(null=True, blank=True)
    company_location = models.CharField(max_length=100, error_messages=
                                        {'required': 'Company Location cannot be empty!'}, null=False, blank=False)
    position_in_company = models.CharField(max_length=100, error_messages=
                                        {'required': 'Position in company cannot be empty!'}, null=False, blank=False)
    date_of_establishment = models.DateField(error_messages={'required': 'Date of establishment cannot be empty!'}, null=False, blank=False)
    reg_no = models.CharField(max_length=30, unique=True, null=True, blank=True, validators=[reg_no_validator])
    profile_photo = models.ImageField(upload_to='profile_photos/', 
                                      null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    sponsor = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='cooperate_member')
    is_active = models.BooleanField(default=True)
    past = models.BooleanField(default=False)
    creator = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='corporate_member')

    def clean_reg_no(self):
        reg_no = self.cleaned_data['reg_no']
        return reg_no.strip().upper()  # Removes spaces & converts to uppercase
    
    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"