# utils.py 工具函数集合
def safe_int(value):
    """
    尝试把 value 转为 int
    如果失败，返回 None
    """
    try:
        return int(value)
    except ValueError:
        return None