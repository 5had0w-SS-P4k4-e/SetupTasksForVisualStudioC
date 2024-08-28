import json
import sys
import os

# Пути к локальным файлам
TASKS_FILE = os.path.expanduser('~/Library/Application Support/Code/User/tasks.json')
KEYBINDINGS_FILE = os.path.expanduser('~/Library/Application Support/Code/User/keybindings.json')

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def update_json_file(file_path, new_data):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    if isinstance(existing_data, dict):
        existing_data = [existing_data]

    if isinstance(new_data, dict):
        new_data = [new_data]

    updated_data = existing_data.copy()

    for item in new_data:
        if item not in existing_data:
            updated_data.append(item)

    with open(file_path, 'w') as file:
        json.dump(updated_data, file, indent=4)

def main():
    # Получаем пути к временным файлам из аргументов
    tasks_file_path = sys.argv[1]
    keybindings_file_path = sys.argv[2]

    # Загружаем данные из временных файлов
    new_tasks_data = load_json(tasks_file_path)
    new_keybindings_data = load_json(keybindings_file_path)

    # Обновляем локальные файлы
    update_json_file(TASKS_FILE, new_tasks_data)
    update_json_file(KEYBINDINGS_FILE, new_keybindings_data)

    print(f"{TASKS_FILE} успешно обновлён!")
    print(f"{KEYBINDINGS_FILE} успешно обновлён!")


main()
