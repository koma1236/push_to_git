import os
from github import Github

# Получаем путь к текущей папке
current_folder = os.path.basename(os.getcwd())

# Ваш логин и пароль для GitHub
username = "koma1236"
password = "uvodip99"

# Создаем экземпляр класса Github
g = Github('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')

# Получаем пользователя
user = g.get_user()
print(user)
# Проверяем, существует ли репозиторий с именем текущей папки
try:
    repo = user.get_repo(current_folder)
    print("Репозиторий уже существует. Обновляем его...")
except:
    # Если репозиторий не существует, создаем его
    repo = user.create_repo(current_folder)
    print("Репозиторий успешно создан.")

# Добавляем все файлы из текущей папки в репозиторий

files = os.listdir()
for file_name in files:
    try:
        with open(file_name, "rb") as file:
            content = file.read()
            try:
                # Пытаемся получить содержимое файла из репозитория
                existing_file = repo.get_contents(file_name)
                # Если файл уже существует, обновляем его содержимое
                repo.update_file(existing_file.path, "Update", content, existing_file.sha)
                print(f"Файл '{file_name}' успешно обновлен.")
            
            except:
                # Если файла нет в репозитории, создаем его
                repo.create_file(file_name, "Initial commit", content)
                print(f"Файл '{file_name}' успешно добавлен в репозиторий.")
    except PermissionError as e:
            # Игнорируем исключение PermissionError и продолжаем выполнение
            print(f"Произошла ошибка при обновлении файла '{file_name}': {str(e)}. Продолжаем выполнение.")

print("Проект успешно отправлен на GitHub!")