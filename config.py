from environs import Env
import os
env: Env = Env()
env.read_env()

API_TOKEN = env('API_KEY')
SECRET_KEY = env('SECRET_KEY')
