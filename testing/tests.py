from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from PIL import Image


class PillowTest(TestCase):

    def test_invalid_file(self):
        # An invalid JPEG
        test_file = SimpleUploadedFile('invalid.jpeg', "data", content_type="image/jpeg")
        Image.open(test_file)
