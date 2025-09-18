import uuid
from io import BytesIO
from typing import Any

import qrcode
from django.core.files.base import ContentFile
from django.db import models


class QRCode(models.Model):
    """Class that holds generated QR Codes."""

    guid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False, primary_key=True
    )
    data = models.TextField(max_length=250)
    qr_code = models.ImageField(upload_to="qr_codes/", null=True, blank=True)

    def generate_qr_code(self):
        """Generate a QR Code."""
        img = qrcode.make(self.data)

        # save to BytesIO
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # create ContentFile for Django
        file_name = f"qr_{self.guid}.png"
        self.qr_code.save(file_name, ContentFile(buffer.read()), save=False)
        buffer.close()

    def save(self, *args: Any, **kwargs: Any) -> None:
        """Validate fields before saving."""
        if self._state.adding:
            self.generate_qr_code()
        super().save()

    def _str_(self):
        return self.title
