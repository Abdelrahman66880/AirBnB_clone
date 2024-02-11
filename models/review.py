#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    
    user_id = ""
    place_id = ""
    text = ""
