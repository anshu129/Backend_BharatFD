from rest_framework import serializers
from .models import FAQ

class FaqSerializer(serializers.ModelSerializer):
    # You can add translated fields here, for example, `question_hi`, `question_bn`
    
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_hi', 'question_bn']
