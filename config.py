import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') \
        or 'b6099382f118f397d6108665e919bba4f90b1614'
