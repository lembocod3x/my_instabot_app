import os
from dotenv import load_dotenv
from instapy import InstaPy
from instapy.util import smart_run

def run_instabot():
    # Load credentials from .env
    load_dotenv()
    username = os.getenv("INSTA_USERNAME")
    password = os.getenv("INSTA_PASSWORD")

    session = InstaPy(username=username, password=password, headless_browser=True)

    with smart_run(session):
        session.set_relationship_bounds(enabled=True,
                                        max_followers=3000,
                                        min_followers=50)
        session.set_skip_users(skip_private=True)
        session.set_do_follow(True, percentage=40)
        session.set_do_like(True, percentage=85)
        session.set_do_comment(True, percentage=25)
        session.set_comments(["Nice!", "Awesome!", "🔥🔥🔥", "Great post!"])
        session.set_action_delays(enabled=True, like=3, comment=6, follow=10)

        session.like_by_tags(['python', 'coding', 'developer'], amount=10)
