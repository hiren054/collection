from flask import current_app
from .models import Users
import secrets
from PIL import Image
import os

def get_vendor_name():
    
    names = ['jigarbhai','kartikbhai','mohanbhai']
    
    return names

# split filename and extension and genrate 10 char random hex name for file
def save_photo(photo): 
    if photo:
        rand_hex  = secrets.token_hex(5)
        _, file_extention = os.path.splitext(photo.filename)
        file_name = rand_hex + file_extention
        file_path = os.path.join(current_app.root_path, 'static/img', file_name)
        resized_img = Image.open(photo)
        resized_img.resize((200, 200),Image.ANTIALIAS)
        resized_img.save(file_path,optimize=True)
        return file_name
    
def get_customer_details():
    
    users = Users.query.all()
    
    return users