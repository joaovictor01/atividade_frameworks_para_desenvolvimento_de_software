import os

from dotenv import load_dotenv

project_folder = os.path.expanduser("~/mysite/")
load_dotenv(os.path.join(project_folder, ".env"))


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
