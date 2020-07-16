import app
import unittest
from PIL import Image
import numpy
from io import BytesIO
from pathlib import Path
import os
import sys
import subprocess
import threading
from io import StringIO
import cv2
from app import emo_recognition


class Test_app(unittest.TestCase):
    def test_stream_video(self):
        with app.app.test_client() as c:
            a = c.get('/music/happy')
        assert a is not None

    def test_cnn(self):
        self.assertEqual(emo_recognition('./39.jpg'), 'Surprise')


if __name__ == "__main__":
    unittest.main()
