def isOdd(param):
    # 检查参数是否为整数类型
    if not isinstance(param, int):
        return False
    # 检查整数是否为奇数
    return param % 2 == 1
