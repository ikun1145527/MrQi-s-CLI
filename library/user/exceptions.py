class UserNotFoundError(Exception):
    """用户不存在异常"""
    pass

class DuplicateUserError(Exception):
    """重复用户异常（如用户名或ID已存在）"""
    pass