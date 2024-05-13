from rest_framework.serializers import Serializer


class RetrieveSerializedMixin:
    def get_serializer(self: Serializer, instance):
        raise NotImplementedError("Implement this method in subclasses")

    def get_serialized_object(self, instance):
        serializer = self.get_serializer(instance)
        return serializer.data
