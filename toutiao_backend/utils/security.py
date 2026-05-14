from passlib.context import CryptContext

# 创建密码加密上下文，用于统一管理密码哈希算法和策略
pwd_context = CryptContext(
    schemes=["bcrypt"],   # 使用 bcrypt 加密算法
    deprecated="auto"     # 自动处理废弃的算法
)

# 加密：将明文密码加密为哈希值
def get_password_hash(password: str) -> str:
    """
    对明文密码进行加密
    :param password: 明文密码
    :return: 加密后的哈希值
    """
    return pwd_context.hash(password)

# 密码校验：验证明文密码是否与哈希值匹配
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    校验明文密码是否正确
    :param plain_password: 用户输入的明文密码
    :param hashed_password: 数据库中存储的哈希密码
    :return: 是否匹配
    """
    return pwd_context.verify(plain_password, hashed_password)