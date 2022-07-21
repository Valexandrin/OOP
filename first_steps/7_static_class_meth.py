class Point:
    min_val = 0
    max_val = 10


    @classmethod  # работает с атрибутами класса, но не экземпляра класса
    def validate(cls, arg):
        return cls.min_val <= arg <= cls.max_val


    def __init__(self, x, y) -> None:
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y


    def get_coords(self):
        return (self.x, self.y)


    @staticmethod  # работает с переданными при вызове значениями
    def multiply(x, y):
        return x*y + Point.max_val


p1 = Point(3, 40)
p2 = Point(1, 2)
# print(p1.get_coords())
# print(p2.get_coords())
# print(Point.multiply(10, 2))
# print(p1.__dict__)
# print(dir(p1))


# ex_7
from string import ascii_lowercase, digits

class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")
        if not set(name) <= set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10) -> None:
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return "<p class='login'>{name}: <input type='text' size={size} />".format(
            name=self.name,
            size=self.size,
        )


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")
        if not set(name) <= set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10) -> None:
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return "<p class='password'>{name}: <input type='text' size={size} />".format(
            name=self.name,
            size=self.size,
        )


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()


# ex_8
from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    set_chars = set(CHARS_FOR_NAME)

    @classmethod
    def check_card_number(cls, number):
        num_list = number.split()

        if len(num_list) != 4:
            return False

        if not all(map(lambda num: num == 4, num_list)):
            return False

        return all(map(lambda num: num.isdigit(), num_list))


    @classmethod
    def check_name(cls, name):
        word_list = name.split(' ')

        if len(word_list) != 2:
            return False

        return all(map(lambda word: set(word) <= cls.set_chars, word_list))


print(CardCheck.check_card_number("12A4-5678-9012-0000"))
print(CardCheck.check_name("SERGEI BALAKIREV"))


# ex_9
class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos  = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()

v1 = Video()
v2 = Video()

v1.create("Python")
v2.create("Python ООП")

YouTube.add_video(v1)
YouTube.add_video(v2)

[YouTube.play(i) for i in range(len(YouTube.videos))]


# ex_10
class AppStore:

    def __init__(self) -> None:
        self.applications = dict()

    def add_application(self, app):
        self.applications[id(app)] = app

    def remove_application(self, app):
        self.applications.pop(id(app))

    def block_application(self, app):
        app = self.applications.get([id(app)], False)
        if app:
            app.blocked = True

    def total_apps(self):
        return len(self.applications)

class Application:
    def __init__(self, name, blocked=False) -> None:
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)



# ex_11
class Viber:
    msgs = dict()

    @classmethod
    def add_message(cls, msg):
        cls.msgs[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        cls.msgs.pop(id(msg))

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like


    @classmethod
    def show_last_message(cls, number):
        for msg in list(cls.msgs.values())[-number:]:
            print(msg.text)

    @classmethod
    def total_messages(cls):
        return len(cls.msgs)


class Message:
    def __init__(self, text, fl_like=False) -> None:
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.show_last_message(2)
Viber.remove_message(msg)


# final_ex
class Router:
    def __init__(self) -> None:
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server.ip] = server
        server.routers.add(self)

    def unlink(self, server):
        if self.servers.pop(server.ip):
            server.routers.discard(self)

    def send_data(self):
        for package in self.buffer:
            ip = package.receiver_ip
            if ip in self.servers:
                self.servers[ip].buffer.append(package)

        self.buffer.clear()


class Server:
    server_ip = 1

    def __init__(self) -> None:
        self.buffer = []
        self.ip = Server.server_ip
        Server.server_ip += 1
        self.routers = set()

    def send_data(self, data):
        for router in self.routers:
            router.buffer.append(data)

    def get_data(self):
        data = self.buffer[:]
        self.buffer.clear()
        return data

    def get_ip(self):
        return self.ip


class Data:
    def __init__(self, data, receiver_ip) -> None:
        self.data = data
        self.receiver_ip = receiver_ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print(msg_lst_from[0].data, msg_lst_to[0].data)
