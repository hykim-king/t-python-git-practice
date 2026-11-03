def login(user_id: str, password: str) -> bool:
    """학습용 로그인 기능"""
    return user_id == "admin" and password == "1234"


if __name__ == "__main__":
    result = login("admin", "1234")

    if result:
        print("로그인 성공")
    else:
        print("로그인 실패")