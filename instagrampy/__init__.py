import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from instagrampy.packages.instagram import Instagrammer, Instagram
from instagrampy.data.models import InstagramUser, InstagramPost
