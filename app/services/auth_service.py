from app.core.security import verify_password, create_access_token
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def authenticate_user(self, email: str, password: str):
        user = self.user_repository.get_user_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user

    def create_token(self, email: str):
        access_token = create_access_token(data={"sub": email})
        return access_token
