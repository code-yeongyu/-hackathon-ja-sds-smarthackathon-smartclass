from rest_framework import serializers
from custom_profile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "is_admin", "student_id", "school_class", "class_id",
                  "bio")
