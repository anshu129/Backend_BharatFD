from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FaqSerializer
from django.utils.translation import activate

class FaqListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')  # Default to English if no language is provided
        activate(lang)  # Activate the language for translation
        
        faqs = FAQ.objects.all()  # Get all FAQs from the database
        # Dynamically translate the questions based on the `lang` parameter
        for faq in faqs:
            faq.question = faq.get_translated_question(lang)  # Use the model's method for translation

        serializer = FaqSerializer(faqs, many=True)  # Serialize the FAQs
        return Response(serializer.data)  # Return the serialized data as JSON
