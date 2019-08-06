from rest_framework import serializers
from custom_profile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "student_id", "class_id", "bio")
