initial_password = "password123"

passwords = ['password123', 'password1234', 'password12345', 'password']

for password in passwords:
    if password == initial_password:
        print("Ви увійшли в систему")
    else:
        print("Неправильний пароль")