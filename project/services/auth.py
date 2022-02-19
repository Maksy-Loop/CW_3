import base64
import hashlib
import hmac
import datetime
import calendar
import jwt
from constants import PWD_HASH_ITERATIONS, PWD_HASH_SALT
from config import Config
from dao.user import UserDAO


class AuthService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def create_tokens(self, data):

        username = data.get("username", None)
        password = data.get("password", None)

        try:
            data_user = self.dao.get_by_username(username)
            self.compare_passwords(data_user.password, password)

            data_dict = {
                "username" : data_user.username,
                "role": data_user.role
            }

            mins30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            data_dict["exp"] = calendar.timegm(mins30.timetuple())
            access_token = jwt.encode(data_dict, Config.SECRET_HERE, algorithm=Config.ALGO)


            days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
            data_dict["exp"] = calendar.timegm(days130.timetuple())
            refresh_token = jwt.encode(data_dict, Config.SECRET_HERE, algorithm=Config.ALGO)

            self.dao.update_tokens(access_token, refresh_token, data_user.id)

            return {
                "access_token" : access_token,
                "refresh_token" : refresh_token

            }


        except Exception as e:
            return f"Неверный пользователь или паролль"

    def create_tokens_with_rt(self, data):
        try:
            refresh_token = data.get("refresh_token", None)

            data_dict = jwt.decode(refresh_token, Config.SECRET_HERE, algorithms=[Config.ALGO])

            data_user = self.dao.get_by_username(data_dict["username"])


            mins30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            data_dict["exp"] = calendar.timegm(mins30.timetuple())
            access_token = jwt.encode(data_dict, Config.SECRET_HERE, algorithm=Config.ALGO)

            days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
            data_dict["exp"] = calendar.timegm(days130.timetuple())
            refresh_token = jwt.encode(data_dict, Config.SECRET_HERE, algorithm=Config.ALGO)

            self.dao.update_tokens(access_token, refresh_token, data_user.id)

            return {
                "access_token": access_token,
                "refresh_token": refresh_token

            }
        except Exception as e:
            return f"Неверный токен"








    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac('sha256', other_password.encode(), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        )
