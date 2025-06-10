# 만약 원본 함수가 인자를 받을 필요가 있다면, *args, **kwargs로 받아 넘겨야 함
def decorator(func):
    def wrapper(*args, **kwargs):
        print(">>> Before")
        result = func(*args, **kwargs)
        print(">>> After")
        return result
    return wrapper

@decorator
def add(a,b):
    return a+b

print(add(3,5))
