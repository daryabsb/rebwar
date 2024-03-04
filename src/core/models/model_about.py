from django.db import models
from src.core.modules import upload_image_file_path
from django.contrib.auth import get_user_model

User = get_user_model()


class About(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=650)
    action = models.CharField(max_length=50)
    link = models.CharField(max_length=100, null=True, blank=True, default='/')
    featured = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True,
                              default='uploads/user/default-user-avatar.png',
                              upload_to=upload_image_file_path)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        from django.conf import settings
        from googletrans import Translator
        from modeltranslation import settings as mt_settings

        try:
            super().save(*args, **kwargs)

            # Get the languages dynamically from settings
            languages = settings.LANGUAGES

            # Initialize translator
            translator = Translator()

            # Fields to translate
            translation_fields = ['title', 'description', 'action']

            # Iterate over each language
            for lang_code, lang_name in languages:
                # Iterate over fields that need translation
                for field_name in translation_fields:
                    # Form the source text from the available fields
                    source_text = getattr(self, f'{field_name}_en', '')

                    # Skip empty fields
                    if not source_text:
                        continue

                    # Perform translation
                    translated_text = translator.translate(
                        source_text, dest=lang_code)

                    # Set the translated text in the corresponding translated field
                    setattr(self, f'{field_name}_{lang_code}',
                            translated_text.text)

            # Save the model again to store the translated values
            super().save(*args, **kwargs)

        except Exception as e:
            print(f"An error occurred during the save operation: {e}")
            # Handle the error as needed
