from django.db import models
from django_ckeditor_5.fields import CKEditor5Field  # WYSIWYG editor support
from django.utils.translation import gettext_lazy as _
from googletrans import Translator
import asyncio
from django.core.cache import cache

translator = Translator()

class FAQ(models.Model):
    question = models.TextField(verbose_name=_("Question"))
    answer = CKEditor5Field(config_name='default')  # WYSIWYG support
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation

    def save(self, *args, **kwargs):
        """Auto-translate question field before saving."""
        loop = asyncio.get_event_loop()
        if not self.question_hi:
            self.question_hi = loop.run_until_complete(self.translate_text(self.question, "hi"))
        if not self.question_bn:
            self.question_bn = loop.run_until_complete(self.translate_text(self.question, "bn"))
        super().save(*args, **kwargs)

    async def translate_text(self, text, dest):
        translation = await translator.translate(text, dest=dest)
        return translation.text

    def get_translated_question(self, lang="en"):
        cache_key = f"faq_{self.id}_question_{lang}"
        translated_question = cache.get(cache_key)
        if not translated_question:
            if lang == 'hi' and self.question_hi:
                translated_question = self.question_hi
            elif lang == 'bn' and self.question_bn:
                translated_question = self.question_bn
            else:
                translated_question = self.question
            cache.set(cache_key, translated_question, timeout=60*60)  
        return translated_question

    def __str__(self):
        return self.question[:50]
