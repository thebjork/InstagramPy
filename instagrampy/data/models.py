import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from dataclasses import dataclass

@dataclass
class InstagramUser():
    """Class for Instagram User"""
    username: str
    fullname: str
    bio: str
    url: str
    followers: int
    following: int
    posts: int
    highlights: int
    igtv: int
    _id : int
    business_account: bool
    professional_account: bool
    category: str
    private: bool
    verified: bool
    profile_picture: str
    business_email: str
    business_phone: str

@dataclass
class InstagramPost():
    """Class for Instagram Image Post"""
    username: str
    user_id: int
    fullname: str
    post_id: int
    shortcode: str
    url: str
    timestamp: str
    likes: int
    comments: int
