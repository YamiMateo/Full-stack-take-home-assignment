from rest_framework import serializers
from .models import TeamMember
import re

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

    def validate_phone(self, value):
        if not re.fullmatch(r'\d{10}', value):
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        return value
