

import random
from django.db.models import F
from django.db.models import Q
from cryptography.fernet import Fernet
from django.core.exceptions import ValidationError
from datetime import date, datetime, timedelta, timezone
import hashlib
import json
import os
import uuid

# from src.app.encryptions import string_to_bytes


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - (
        (today.month, today.day) < (birthDate.month, birthDate.day)
    )

    return age

# def save_pdf_pages_attachment(sender, instance, created, **kwargs):

#     if created:
#         instance.save()


def handle_product_attachment_upload(instance, filename):
    return f"products/{instance.product.handle}/attachments/{filename}"


def profile_image_file_path(instance, filename):
    # Generate file path for new recipe image
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/', filename)


def upload_image_file_path(instance, filename):
    # Generate file path for new recipe image
    model = instance._meta.model.__name__.lower()
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join(f'uploads/{model}/', filename)


def upload_file_file_path(instance, filename):
    # Generate file path for new recipe image
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/files/', filename)


# def rate(rate):
#     return int(rate) / 100


# def calculate_expiry_date2(activation_date, trial_days=0, purchase_plan_days=0):
#     # Calculate the end of the trial period
#     trial_expiry = activation_date + timedelta(days=trial_days)

#     # Calculate the end of the purchase plan period (if any)
#     if purchase_plan_days is not None:
#         plan_expiry = datetime.now() + timedelta(days=purchase_plan_days)
#         if plan_expiry > trial_expiry:
#             return plan_expiry
#     return trial_expiry


# def calculate_expiry_date(activation_date, trial_days=0, purchase_plan_days=0):
#     """
#     Calculate the expiry date based on activation date, trial days, and purchase plan days.

#     Parameters:
#     activation_date (datetime): The activation date of the subscription.
#     trial_days (int): The number of trial days for the subscription. Default is 0.
#     purchase_plan_days (int): The number of purchase plan days for the subscription. Default is 0.

#     Returns:
#     datetime: The expiry date of the subscription.
#     """
#     if not activation_date:
#         return None

#     today = datetime.utcnow().date()
#     expiry_date = activation_date + timedelta(days=trial_days)

#     if purchase_plan_days > 0:
#         plan_activation_date = activation_date + timedelta(days=trial_days)
#         plan_expiry_date = plan_activation_date + \
#             timedelta(days=purchase_plan_days)
#         if plan_expiry_date > expiry_date:
#             expiry_date = plan_expiry_date

#     if expiry_date.date() < today:
#         expiry_date = today

#     return expiry_date


# def obfuscate_activation_code(instance):
#     expiry = datetime.now()
#     if instance.expiry is not None:
#         # expiry = datetime.strptime(instance.expiry, '%Y-%m-%d').date()
#         expiry = instance.expiry
#     obfuscated_data = string_to_bytes(json.dumps({
#         'type': instance.plan.plan_type.type,
#         'plan': instance.plan.handle,
#         'is_active': instance.is_active,
#         'expiry': expiry.strftime('%Y-%m-%d %H:%M:%S'),
#     }))
#     return obfuscated_data

# def obfuscate_store_data(store_data):
    
#     obfuscated_data = string_to_bytes(json.dumps(store_data))
#     return obfuscated_data


# def obfuscate2(store, type='free', plan='standalone', active=False, expiry=None):
#     if expiry is None:
#         expiry = date.today()
#     elif expiry == 'never':
#         expiry = date.today() + timedelta(days=3650)
#     elif isinstance(expiry, str):
#         expiry = datetime.strptime(expiry, '%Y-%m-%d').date()
#     else:
#         expiry = date.today()

#     obfuscated_data = {
#         'type': type,
#         'plan': plan,
#         'store': store,
#         'is_active': active,
#         'expiry': expiry.strftime('%Y%m%d'),
#     }
#     return obfuscated_data


# def deobfuscate(obfuscated_data):
#     # Split the string by '|'
#     items = obfuscated_data.split('|')

#     # Create an empty dictionary to store the key-value pairs
#     my_dict = {}

#     # Iterate through the list of items and split each item by ':'
#     for item in items:
#         if ':' in item:
#             key, value = item.split(':')
#             # Remove any single quotes from the value
#             value = value.strip("'")

#             # Special handling for expiry date
#             if key == 'expiry':
#                 if value == 'never':
#                     value = datetime.today() + timedelta(days=3650)
#                 else:
#                     value = datetime.strptime(value, '%y%m%d')

#             # Convert 'is_active' value to boolean
#             elif key == 'is_active':
#                 value = True if value == 'True' else False

#             my_dict[key] = value
#     return my_dict


# def hash_data(data):
#     """
#     Hashes the given binary data using SHA-256.

#     Args:
#         data (bytes): The binary data to hash.

#     Returns:
#         str: The hex-encoded hash digest.
#     """
#     hash_object = hashlib.sha256(data)
#     hex_digest = hash_object.hexdigest()
#     return hex_digest


# def obfuscate(store_plan):
#     try:
#         expiry = store_plan.expiry.strftime('%Y-%m-%d')
#     except:
#         expiry = date.today().strftime('%Y-%m-%d')

#     obfuscated_data = {
#         "store": store_plan.store.handle,
#         "type": store_plan.plan.plan_type.handle,
#         "plan": store_plan.plan.handle,
#         "active": store_plan.is_active,
#         "expiry": expiry
#     }
#     return obfuscated_data


# def encrypt(data, key):
#     """Encrypt the license data."""
#     f = Fernet(key.encode())
#     return f.encrypt(json.dumps(data).encode())


# def decrypt(data, key):
#     """Decrypt the license data."""
#     f = Fernet(key.encode())
#     return json.loads(f.decrypt(data).decode())


# def validate_license(license):
#     """Validate the license."""
#     try:
#         obfuscated_data = decrypt(license.encrypted_data, license.key)
#     except Exception:
#         raise ValidationError("Invalid license key or encrypted data.")

#     if hashlib.sha256(license.encrypted_data).hexdigest() != license.hashed_data:
#         raise ValidationError("Invalid license data hash.")

#     if not obfuscated_data["a"]:
#         raise ValidationError("License is not active.")

#     expiry_str = obfuscated_data["e"]
#     if expiry_str == "never":
#         expiry_date = None
#     else:
#         expiry_date = timezone.datetime.strptime(expiry_str, "%Y%m%d").date()
#     if expiry_date and expiry_date < timezone.now().date():
#         raise ValidationError("License has expired.")

#     return expiry_date


'''
def some_function_to_obfuscate(name, store, version, expiry):

    # Free                   = "type:'free'|plan:'standalone'|store:'nare-market'|is_active:False|expiry:'never'"
    # Free(activated)        = "type:'free'|plan:'standalone'|store:'nare-market'|is_active:True|expiry:'never'"
    # Trial                  = "type:'trial'|plan:'my-logo'|store:'nare-market'|is_active:False|expiry:'free'"
    # Trial(activated)       = "type:'trial'|plan:'my-logo'|store:'nare-market'|is_active:True|expiry:expiry:'23-05-08'"
    # Premeium               = "type:'premeium'|plan:'my-logo'|store:'nare-market'|is_active:False|expiry:'free'"
    # Premeium(activated)    = "type:'premeium'|plan:'my-logo'|store:'nare-market'|is_active:True|expiry:expiry:'23-05-08'"

    if not expiry:
        expiry = date.today() + timedelta(days=365)
    obfuscated_data = f"{name}-{store}-v{version}-{expiry.strftime('%Y%m%d')}"
    return obfuscated_data
'''

# def pdf_page_count(link):
#     # Load the pdf to the PdfFileReader object with default settings
#     with open(link, "rb") as pdf_file:
#         pdf_reader = PdfFileReader(pdf_file)
#         num = pdf_reader.numPages
#         print(
#             f"The total number of pages in the pdf document is {pdf_reader.numPages}")
#     return num

# import asyncio
# import websockets

# async def send_messages(websocket, path):
#     count = 0
#     while True:
#         message = f"Message {count}"
#         await websocket.send(message)
#         print(f"Sent: {message}")
#         count += 1
#         await asyncio.sleep(2)

# start_server = websockets.serve(send_messages, "localhost", 8765)

# # Enable CORS by adding the necessary headers
# async def on_accept(websocket, path):
#     if "upgrade" not in websocket.headers.get("Connection", "").lower():
#         await websocket.close(code=1000, reason="WebSocket connection upgrade required")
#     else:
#         await start_server.ws_handler(websocket, path)

# start_server.ws_handler = send_messages
# start_server.on_accept = on_accept

# # Add CORS headers to the response
# def add_cors_headers(response):
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     response.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
#     return response

# start_server.on_upgrade = add_cors_headers

# def run_sockets():
#     asyncio.get_event_loop().run_until_complete(start_server)
#     asyncio.get_event_loop().run_forever()


# def generate_activation_code():
#     random_digits = [random.randint(0, 9) for _ in range(19)]
#     # Convert the list of digits into a string
#     unique_code = "".join(map(str, random_digits))
#     # Insert spaces every 4 digits
#     formatted_code = " ".join(
#         [unique_code[i: i + 4] for i in range(0, len(unique_code), 4)]
#     )

#     return formatted_code[:24]