from rest_framework import serializers 
from .models import Student_reaction

class StudentReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_reaction 
        
        fields = (
            'id',
            'studentName',           
            'existingComorbidites',
            'reaction',
            'severity',
            'remarks'
        )