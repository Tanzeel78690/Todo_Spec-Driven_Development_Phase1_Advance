def authenticate_user(session: Session, email: str, password: str) -> Optional[User]:
    user = get_user_by_email(session, email)
    if not user or not Hasher.verify_password(password, user.hashed_password):
        return None
    return user
