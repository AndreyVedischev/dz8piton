from view import render_template

from model import Info, User, Phone



def default_controller(data=None, cls=True):    
    render_template(context={}, template="default.jinja2", cls=cls)
    return (input(), None)


def exit_controller(data=None, cls=True):
    render_template(context={}, template="exit.jinja2", cls=cls)
    exit()


def all_users_controller(data=None, cls=True):
    users = User.all()
    render_template(context={'users':users}, template="all_users.jinja2", cls=cls)
    input("Продолжить?")
    return 'main', None 


def add_user_controller(data=None, cls=True):
    render_template(context={}, template="add_user.jinja2", cls=cls)
    username = input()
    user = User.add(username)
    return 20, user 


def del_user_controller(data=None, cls=True):
    render_template(context={}, template="add_user.jinja2", cls=cls)
    username = input()
    user = User.del_user(username)
    return 'main', None 

def add_info_controller(user, cls=True):
    render_template(context={}, template="add_info.jinja2", cls=cls)
    info_user = input()
    info = Info.add(info_user, user)
    return 21, user 

def add_phone_controller(user, cls=True):
    render_template(context={}, template="add_phone.jinja2", cls=cls)
    phone_number = input()
    phone = Phone.add(phone_number, user)
    return 212, user 


def add_more_controller(user, cls=True):
    render_template(context={}, template="add_more.jinja2", cls=cls)
    answer = input()
    if answer == 'Y':
        return 21, user
    return 51, user 

def get_controller(state):
    return controllers_dict.get(state, default_controller)


controllers_dict = { 
    '0': exit_controller,
    '1': all_users_controller,
    '2': add_user_controller,
    '4': del_user_controller,
    20: add_info_controller,
    21: add_phone_controller, 
    212: add_more_controller
}