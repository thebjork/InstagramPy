import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from multisocial.packages.instagram import Instagrammer, Instagram
from multisocial.data.models import InstagramUser, InstagramPost
