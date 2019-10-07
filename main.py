import field
import messages as m
import os

# Game consts
F = field.Field(4)
is_game = True
num_of_rand = F.num_of_rand


def getSaveList(silent=False):
    if not os.path.isdir("saves"):
        os.makedirs("saves")
    else:
        save_list = os.listdir("saves")
        if not silent:
            print("Доступные сохранения:")
            if not save_list:
                print("Пусто! Нет доступных сохранений.")
            else:
                for save in save_list:
                    print("- " + save.replace(".json", ""))
        return save_list


def start_handler():
    global F
    global is_game
    print(m.start_text)
    while True:
        command = input()
        if command == "/newgame":
            print(m.field_select_text)
            while True:
                command = input()
                if command == "4":
                    F = field.Field(4)
                    return
                elif command == "5":
                    F = field.Field(5)
                    return
                elif command == "6":
                    F = field.Field(6)
                    return
                elif command == "8":
                    F = field.Field(8)
                    return
                elif command == "/back":
                    print(m.start_text)
                    break
                else:
                    print(m.w_command_err)

        elif command == "/load":
            save_list = getSaveList(silent=True)
            if not save_list:
                getSaveList()
                input("Чтобы вернуться назад нажмите enter...\n")
                print(m.start_text)
            else:
                while True:
                    getSaveList()
                    name = input("Введите название сохранения или напишите /back для выхода в меню.\n")
                    if name == "/back":
                        print(m.start_text)
                        break
                    else:
                        for save in save_list:
                            if name == save.replace(".json", ""):
                                if F.loadField(name) == "BadSave":
                                    print("Упс... Что-то не так с вашим сохранением.\n")
                                    break
                                else:
                                    return
                        else:
                            print("Нет такого имени сохранения.\n")

        elif command == "/help":
            print(m.help_text)
            input("Нажмите enter для возврата в меню...\n")
            print(m.start_text)

        elif command == "/exit":
            is_game = False
            return

        else:
            print(m.w_command_err)


def game_handler():
    global is_game
    print(m.start_help_text)
    F.drawField()
    while is_game:
        command = input()

        if command == "/esc":
            while True:
                print(m.esc_text)
                command = input()
                if command == "/help":
                    print(m.help_text)
                    input("Нажмите enter для возврата в меню\n")

                elif command == "/savegame":
                    save_list = getSaveList()
                    while True:
                        name = input("Введите название сохранения:\n")
                        if save_list:
                            for save_name in save_list:
                                if name == save_name.replace(".json", ""):
                                    print("Такое сохранение уже существует, вы уверены, что хотите перезаписать его ?")
                                    while True:
                                        command = input("y/n\n")
                                        if command == "y" or command == "yes":
                                            F.saveField(name)
                                            break
                                        elif command == "n" or command == "no":
                                            break
                                        else:
                                            print(m.w_command_err)
                                    break
                            else:
                                f_return = F.saveField(name)
                                if f_return == "OSError":
                                    print("Недопустимое имя сохранения.\n")
                                else:
                                    break
                        else:
                            f_return = F.saveField(name)
                            if f_return == "OSError":
                                print("Недопустимое имя сохранения\n")
                            else:
                                break

                elif command == "/exit":
                    return

                elif command == "/esc" or command == "/back":
                    F.drawField()
                    break

                else:
                    print(m.w_command_err)
                    continue

        elif command == "w":
            F.cellsSum("UP")
            if F.is_field_change:
                F.cellRandomize(num_of_rand)
                F.drawField()
            if F.winLoseChecker() is True:
                print(m.win_text)
                break
            elif F.winLoseChecker() is False:
                print(m.lose_text)
                break

        elif command == "s":
            F.cellsSum("DOWN")
            if F.is_field_change:
                F.cellRandomize(num_of_rand)
                F.drawField()
            if F.winLoseChecker() is True:
                print(m.win_text)
                break
            elif F.winLoseChecker() is False:
                print(m.lose_text)
                break

        elif command == "a":
            F.cellsSum("LEFT")
            if F.is_field_change:
                F.cellRandomize(num_of_rand)
                F.drawField()
            if F.winLoseChecker() is True:
                print(m.win_text)
                break
            elif F.winLoseChecker() is False:
                print(m.lose_text)
                break

        elif command == "d":
            F.cellsSum("RIGHT")
            if F.is_field_change:
                F.cellRandomize(num_of_rand)
                F.drawField()
            if F.winLoseChecker() is True:
                print(m.win_text)
                break
            elif F.winLoseChecker() is False:
                print(m.lose_text)
                break

        else:
            print(m.w_command_err)
            continue


if __name__ == "__main__":
    while is_game:
        start_handler()
        if not is_game:
            break
        game_handler()
