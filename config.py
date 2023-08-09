from environs import Env
env: Env = Env()
env.read_env()

API_TOKEN = env('API_KEY')
SECRET_KEY = env('SECRET_KEY')
