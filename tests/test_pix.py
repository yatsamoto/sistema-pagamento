import pytest
import os
import sys
sys.path.append("../")
from payments.pix import Pix

def test_pix_create_payment():
    pix_instance = Pix()

    payment_info = pix_instance.create_payment()

