from django.db import models
from src.core.modules import upload_image_file_path
from django.contrib.auth import get_user_model

from django.dispatch import receiver
from django.db.models.signals import post_save

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
        print("save called!!")
        

# @receiver(post_save, sender=About)
def translate_about_model(sender, instance, **kwargs):
    from django.conf import settings
    from googletrans import Translator
    print("signal trigered")
    try:
        # Get the languages dynamically from settings
        languages = settings.LANGUAGES

        # Initialize translator
        translator = Translator()

        # Fields to translate
        translation_fields = ['title', 'description', 'action']

        for lang_code, lang_name in languages:
            # Initialize source text as None
            source_text = None

            # Iterate over fields that need translation
            for field_name in translation_fields:
                # Try to get the source text for the current language
                source_text_candidate = getattr(instance, f'{field_name}_{lang_code}', '')

                # If the source text is not empty, use it
                if source_text_candidate:
                    source_text = source_text_candidate
                    break

            # If no source text is found, skip this language
            if not source_text:
                continue

            # Perform translation
            translated_text = translator.translate(source_text, dest=lang_code)
            print("translated_text: ", translated_text)

            # Set the translated text in the corresponding translated field
            setattr(instance, f'{field_name}_{lang_code}', translated_text.text)

        # Save the model again to store the translated values
        instance.save()

    except Exception as e:
        print(f"An error occurred during the save operation: {e}")
        # Handle the error as needed