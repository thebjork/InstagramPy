import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import requests
import fake_useragent
import utils.utils as func
from data.models import InstagramUser, InstagramPost

class Instagrammer:
    """
    Scrape Instagram profile(s)

    Instances
    ---------
    self.obj
        Fake User-Agent instance
    self.headers
        Headers for GET request
    """
    def __init__(self):

        self.obj = fake_useragent.UserAgent(verify_ssl = False)
        self.headers = {"User-Agent": str(self.obj.random)}

    def user(self, username: str):
        """
        Scrape basic user information

        Parameters
        ----------
        username
            string
            Instagram user to scrape
        
        Returns
        -------
        InstagramUser
            dataclass
            User information
        """

        try:
            URL = f"https://instagram.com/{username}/channel/?__a=1"
            PROFILE = requests.get(
                url = URL,
                headers = self.headers
            )
            USER = PROFILE.json()

            if USER == {}:
                return False
            
            else:
                USERNAME = USER["graphql"]["user"]["username"]
                FULLNAME = USER["graphql"]["user"]["full_name"]
                BIO = USER["graphql"]["user"]["biography"]
                URL = USER["graphql"]["user"]["external_url"]
                FOLLOWERS = USER["graphql"]["user"]["edge_followed_by"]["count"]
                FOLLOWING = USER["graphql"]["user"]["edge_follow"]["count"]
                POSTS = USER["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]
                HIGHLIGHTS = USER["graphql"]["user"]["highlight_reel_count"]
                IGTV = USER["graphql"]["user"]["edge_felix_video_timeline"]["count"]
                ID = USER["graphql"]["user"]["id"]
                BUSINESS_ACCOUNT = USER["graphql"]["user"]["is_business_account"]
                PROFESSIONAL_ACCOUNT = USER["graphql"]["user"]["is_professional_account"]
                CATEGORY = USER["graphql"]["user"]["category_name"]
                PRIVATE = USER["graphql"]["user"]["is_private"]
                VERIFIED = USER["graphql"]["user"]["is_verified"]
                PROFILE_PICTURE = func.shorten_url(USER["graphql"]["user"]["profile_pic_url_hd"])
                BUSINESS_EMAIL = USER["graphql"]["user"]["business_email"]
                BUSINESS_PHONE = USER["graphql"]["user"]["business_phone_number"]

                DATA = InstagramUser(
                    username = USERNAME,
                    fullname = FULLNAME,
                    bio = BIO,
                    url = URL,
                    followers = FOLLOWERS,
                    following = FOLLOWING,
                    posts = POSTS,
                    highlights = HIGHLIGHTS,
                    igtv = IGTV,
                    _id = ID,
                    business_account = BUSINESS_ACCOUNT,
                    professional_account = PROFESSIONAL_ACCOUNT,
                    category = CATEGORY,
                    private = PRIVATE,
                    verified = VERIFIED,
                    profile_picture = PROFILE_PICTURE,
                    business_email = BUSINESS_EMAIL,
                    business_phone = BUSINESS_PHONE
                )
            
                return DATA
        
        except:
            return False

    def user_from_id(data, id: int):
        """
        Get Instagram username from Instagram User ID

        Parameters
        ----------
        id
            integer
            Instagram User ID
        
        Returns
        -------
        InstagramUser
            class
            User information
        """
        try:
            URL = f"https://i.instagram.com/api/v1/users/{id}/info/"
            HEADERS = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)"}

            RESULT = requests.get(
                url = URL,
                headers = HEADERS
            )
            USER = RESULT.json()

            if USER == {}:
                return False
            
            else:
                USERNAME = USER["user"]["username"]
                DATA = Instagrammer().user(USERNAME)
            
                return DATA
        
        except:
            return False

class Instagram:
    """
    Scrape Instagram post(s)

    Parameters
    ----------
    url
        string
        URL of Instagram post to scrape

    Instances
    ---------
    self.obj
        Fake User-Agent instance
    self.headers
        Headers for GET request
    """
    def __init__(self, url: str):

        self.url = f"{url}?__a=1"
        self.obj = fake_useragent.UserAgent(verify_ssl = False)
        self.headers = {"User-Agent": str(self.obj.random)}

    def post(self) -> dict:
        """
        Scrape basic post information
        
        Returns
        -------
        InstagramPost
            dataclass
            Post information
        """
        try:
            CONTENT = requests.get(
                url = self.url,
                headers = self.headers
            )
            POST = CONTENT.json()

            if POST == {}:
                return False
            
            USERNAME = POST["graphql"]["shortcode_media"]["owner"]["username"]
            USER_ID = POST["graphql"]["shortcode_media"]["owner"]["id"]
            FULLNAME = POST["graphql"]["shortcode_media"]["owner"]["full_name"]
            POST_ID = POST["graphql"]["shortcode_media"]["id"]
            SHORTCODE = POST["graphql"]["shortcode_media"]["shortcode"]
            TIMESTAMP = func.convert_utc(POST["graphql"]["shortcode_media"]["taken_at_timestamp"])
            LIKES = POST["graphql"]["shortcode_media"]["edge_media_preview_like"]["count"]
            COMMENTS = POST["graphql"]["shortcode_media"]["edge_media_to_parent_comment"]["count"]

            if POST["graphql"]["shortcode_media"]["is_video"] == False:
                URL = func.shorten_url(POST["graphql"]["shortcode_media"]["display_url"])
            
            else:
                URL = func.shorten_url(POST["graphql"]["shortcode_media"]["video_url"])

            DATA = InstagramPost(
                username = USERNAME,
                user_id = USER_ID,
                fullname = FULLNAME,
                post_id = POST_ID,
                shortcode = SHORTCODE,
                url = URL,
                timestamp = TIMESTAMP,
                likes = LIKES,
                comments = COMMENTS
            )
            
            return DATA
        
        except:
            return False
