# 가끔 데코레이터 자체에 옵션을 넣고 싶을 떼 : 데코레이터 팩토리 (데코레이터 반환) 패턴 사용

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello(name):
    print(f"Hello, {name}!")

hello("Alice")
