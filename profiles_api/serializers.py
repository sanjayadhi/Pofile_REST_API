from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
	"""to check the post funtion of the rest_api"""
	name = serializers.CharField(max_length=10)
