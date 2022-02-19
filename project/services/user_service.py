from project.tools.security import generate_password_digest, compare_passwords, create_access_token, create_refresh_token, decode_token
from project.dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao


    def create(self, user_d):
        user_d["password"] = generate_password_digest(user_d.get("password"))
        return self.dao.create(user_d)

    def create_tokens(self, data):

        email = data.get("email", None)
        password = data.get("password", None)

        try:
            data_user = self.dao.get_by_username(email)
            compare_passwords(data_user.password, password)

            data_dict = {
                "email": data_user.email
            }

            access_token = create_access_token(data_dict)
            refresh_token = create_refresh_token(data_dict)


            return {
                "access_token": access_token,
                "refresh_token": refresh_token

            }

        except Exception as e:
            return f"{e} Неверный пользователь или паролль"

    def create_new_tokens(self, data):
        try:
            access_token = data.get("access_token", None)
            refresh_token = data.get("refresh_token", None)

            data_access_token = decode_token(access_token)
            data_refresh_token = decode_token(refresh_token)

            if data_access_token.get("email") == data_refresh_token.get("email"):
                access_token = create_access_token(data_access_token)
                refresh_token = create_refresh_token(data_refresh_token)

                return {
                    "access_token": access_token,
                    "refresh_token": refresh_token

                }
        except Exception as e:
            return f"Неверный токен"

