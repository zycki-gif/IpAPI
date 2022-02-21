from rest_framework import serializers

class Myserializer(serializers.Serializer):
  query= serializers.CharField()


class MyOutputSerializer(serializers.Serializer):
  query = serializers.CharField()
