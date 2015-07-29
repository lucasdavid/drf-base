from rest_framework import serializers
from rest_framework import exceptions


class DynamicFieldsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'context' in kwargs and 'request' in kwargs['context']:
            fields = kwargs['context']['request'].query_params.get('fields')

            if fields:
                requested = set(fields.split(','))
                allowed = set(self.fields.keys())
                unknown = requested - allowed

                if unknown:
                    raise exceptions.ValidationError(
                        'INVALID_FIELDS. The following fields do not exist and/or cannot be projected: (%s)'
                        % ', '.join(unknown))

                for f in allowed - requested:
                    self.fields.pop(f)
