from Auth import login
from Teacher import Teacher
from Principal import Principal
from Admin import Admin
from Menus import teacher_menu, principal_menu, admin_menu


if __name__ == '__main__':
    user = login()
    if user:
        user.display()
        if isinstance(user, Teacher):
            teacher_menu(user)
        elif isinstance(user, Principal):
            principal_menu(user)
        elif isinstance(user, Admin):
            admin_menu(user)