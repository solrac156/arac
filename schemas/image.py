from typing import Any, Optional, Mapping, Union

from marshmallow import Schema, fields
from werkzeug.datastructures import FileStorage


class FileStorageField(fields.Field):
    default_error_messages = {"invalid": "Not a valid image."}

    def _deserialize(
        self,
        value: Any,
        attr: Optional[str],
        data: Optional[Mapping[str, Any]],
        **kwargs
    ) -> Union[FileStorage, None]:
        if value is None:
            return None
        if not isinstance(value, FileStorage):
            self.fail("invalid")
        return value


class ImageSchema(Schema):
    image = FileStorageField(required=True)
