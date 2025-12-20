tasks = []

while True:
    print("\nМеню")
    print("1 - Показать все задачи")
    print("2 - Добавить задачу")
    print("3 - Отметить задачу как выполненную")
    print("4 - Выйти")
    
    choice = input("Выберите действие (1-4): ")

    if choice == "1":
        if not tasks:
            print("\nСписок задач пуст!")
        else:
            print("\nСписок задач")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        new_task = input("\nВведите описание задачи: ")
        tasks.append(new_task)
        print(f"Задача '{new_task}' добавлена")
    
    elif choice == "3":
        if not tasks: 
            print("\nСписок задач пуст!")
        else:
            print("\nВыберите задачу для удаления")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            
            try:
                task_num = int(input("\nВведите номер задачи: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Задача '{removed_task}' удалена!")
                else:
                    print("Неверный номер задачи!")
            except ValueError:
                print("Пожалуйста, введите число!")
    elif choice == "4":
        print("\nДо свидания!")
        break
    else:
        print("\nПожалуйста, выберите действие от 1 до 4")