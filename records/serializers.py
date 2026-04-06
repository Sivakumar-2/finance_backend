from rest_framework import serializers
from .models import Record

class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be positive")
        return value

    def validate_type(self, value):
        if value not in ['income', 'expense']:
            raise serializers.ValidationError("Type must be 'income' or 'expense'")
        return value

    def validate(self, data):
        # Example: prevent future date (optional but strong)
        from datetime import date
        if data.get('date') and data['date'] > date.today():
            raise serializers.ValidationError("Date cannot be in the future")
        return data