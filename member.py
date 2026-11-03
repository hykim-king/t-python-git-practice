from dataclasses import dataclass


@dataclass
class Member:
    member_id: str
    name: str
    email: str


def register_member(member: Member) -> None:
    print(f"회원 등록: {member.member_id}, {member.name}")


if __name__ == "__main__":
    member = Member("hong", "홍길동", "hong@example.com")
    register_member(member)