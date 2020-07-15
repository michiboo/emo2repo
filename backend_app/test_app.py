import app
import unittest
from PIL import Image
import numpy
from io import BytesIO
from pathlib import Path
import os, sys, subprocess
import threading
from io import StringIO
import cv2

class Test_app(unittest.TestCase):
    def test_stream_video(self):
        with app.app.test_client() as c:
            a = c.get('/music/happy')
        print(a.data)
    
if __name__ == "__main__":
    unittest.main()
