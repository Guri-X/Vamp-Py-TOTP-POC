import pyotp
import os

SECRET_KEY = os.getenv("SECRET_KEY")

def gen_url():
    return pyotp.totp.TOTP(SECRET_KEY).provisioning_uri(name="vamp@totp.poc", issuer_name="Vamp TOTP")

def verify_totp(totp):
    return pyotp.TOTP(SECRET_KEY).verify(totp)