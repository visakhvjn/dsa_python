class Cookie:
    def __init__(self, color: str) -> None:
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color: str):
        self.color = color

cookie_one = Cookie('red')

print(cookie_one.get_color())
cookie_one.set_color('green')
print(cookie_one.get_color())
