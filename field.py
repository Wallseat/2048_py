import random
import json


class Field:
    def __init__(self, field_type):
        self.field_types = [4, 5, 6, 8]
        self.field_type = field_type
        self.cell = " "

        self.__createFieldGeometry__(field_type)
        self.__createField__()
        self.cellRandomize(3)
        self.is_field_change = False

    def __createFieldGeometry__(self, field_type):
        if field_type == 4:
            self.width, self.height = 4, 4
            self.winCell = 2048
            self.num_of_rand = 1
        elif field_type == 5:
            self.width, self.height = 5, 5
            self.winCell = 16384
            self.num_of_rand = 1
        elif field_type == 6:
            self.width, self.height = 6, 6
            self.winCell = 131072
            self.num_of_rand = 2
        elif field_type == 8:
            self.width, self.height = 8, 8
            self.winCell = 1048576
            self.num_of_rand = 3

    def __createField__(self):
        self.field = []
        for y in range(self.height):
            self.field.append([])
            for x in range(self.width):
                self.field[y].append(self.cell)

    def drawField(self):
        max_spaces = []
        for x in range(self.width):
            max_space = 0
            for y in range(self.height):
                if len(self.field[y][x]) > max_space:
                    max_space = len(self.field[y][x])
            max_spaces.append(max_space)

        for y in range(self.height):
            for x in range(self.width):
                space = max_spaces[x] - len(self.field[y][x])
                print(f" {self.field[y][x]} " + " " * space, end="")

            print("")
        print("\n")

    def cellUpdate(self, x, y, obj):
        self.field[x][y] = obj

    def cellRandomize(self, num):
        for i in range(num):
            k = random.randint(1, 10)
            if k > 9:
                cell = 4
            else:
                cell = 2
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if self.field[y][x] == self.cell:
                    self.cellUpdate(y, x, str(cell))
                    break
                else:
                    continue

    def winLoseChecker(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.field[y][x] == self.cell:
                    return
                elif self.field[y][x] == self.winCell:
                    return True

        return False

    def cellsSum(self, vector):
        self.is_field_change = False

        if vector == "UP":
            for x in range(self.width):
                for ay in range(self.height):
                    if self.field[ay][x] == self.cell:
                        continue
                    elif ay == self.height:
                        break
                    else:
                        for by in range(ay + 1, self.height):
                            if self.field[by][x] == self.cell:
                                continue
                            elif self.field[by][x] == self.field[ay][x]:
                                self.field[ay][x] = str(int(self.field[ay][x]) + int(self.field[by][x]))
                                self.field[by][x] = self.cell
                                self.is_field_change = True
                                break
                            else:
                                break

            for x in range(self.width):
                for ay in range(self.height):
                    if self.field[ay][x] == self.cell:
                        for by in range(ay + 1, self.height):
                            if self.field[by][x] == self.cell:
                                continue
                            else:
                                self.field[ay][x], self.field[by][x] = self.field[by][x], self.cell
                                self.is_field_change = True
                                break
                    else:
                        continue

        elif vector == "DOWN":
            for x in range(self.width):
                for ay in range(self.height - 1, -1, -1):
                    if self.field[ay][x] == self.cell:
                        continue
                    elif ay == self.height:
                        break
                    else:
                        for by in range(ay - 1, -1, -1):
                            if self.field[by][x] == self.cell:
                                continue
                            elif self.field[by][x] == self.field[ay][x]:
                                self.field[ay][x] = str(int(self.field[ay][x]) + int(self.field[by][x]))
                                self.field[by][x] = self.cell
                                self.is_field_change = True
                                break
                            else:
                                break

            for x in range(self.width):
                for ay in range(self.height - 1, -1, -1):
                    if self.field[ay][x] == self.cell:
                        for by in range(ay - 1, -1, -1):
                            if self.field[by][x] == self.cell:
                                continue
                            else:
                                self.field[ay][x], self.field[by][x] = self.field[by][x], self.cell
                                self.is_field_change = True
                                break
                    else:
                        continue

        elif vector == "LEFT":
            for y in range(self.height):
                for ax in range(self.width):
                    if self.field[y][ax] == self.cell:
                        continue
                    elif ax == self.width:
                        break
                    else:
                        for bx in range(ax + 1, self.width):
                            if self.field[y][bx] == self.cell:
                                continue
                            elif self.field[y][bx] == self.field[y][ax]:
                                self.field[y][ax] = str(int(self.field[y][ax]) + int(self.field[y][bx]))
                                self.field[y][bx] = self.cell
                                self.is_field_change = True
                                break
                            else:
                                break

            for y in range(self.height):
                for ax in range(self.width):
                    if self.field[y][ax] == self.cell:
                        for bx in range(ax + 1, self.width):
                            if self.field[y][bx] == self.cell:
                                continue
                            else:
                                self.field[y][ax], self.field[y][bx] = self.field[y][bx], self.cell
                                self.is_field_change = True
                                break
                    else:
                        continue

        elif vector == "RIGHT":
            for y in range(self.height):
                for ax in range(self.width - 1, -1, -1):
                    if self.field[y][ax] == self.cell:
                        continue
                    elif ax == self.width:
                        break
                    else:
                        for bx in range(ax - 1, -1, -1):
                            if self.field[y][bx] == self.cell:
                                continue
                            elif self.field[y][bx] == self.field[y][ax]:
                                self.field[y][ax] = str(int(self.field[y][ax]) + int(self.field[y][bx]))
                                self.field[y][bx] = self.cell
                                self.is_field_change = True
                                break
                            else:
                                break

            for y in range(self.height):
                for ax in range(self.width - 1, -1, -1):
                    if self.field[y][ax] == self.cell:
                        for bx in range(ax - 1, -1, -1):
                            if self.field[y][bx] == self.cell:
                                continue
                            else:
                                self.field[y][ax], self.field[y][bx] = self.field[y][bx], self.cell
                                self.is_field_change = True
                                break
                    else:
                        continue

    def saveField(self, name):
        filedCells = []
        for y in range(self.height):
            for x in range(self.width):
                if self.field[y][x] != self.cell:
                    cell_info = [y, x, self.field[y][x]]
                    filedCells.append(cell_info)
        save = {
            'SaveName': name,
            'FieldType': self.field_type,
            'FiledCells': filedCells
        }
        try:
            with open(f"saves/{name}.json", "w", encoding="utf-8") as F:
                json.dump(save, F)
            print("Успешно сохранено!\n")
        except OSError:
            return "OSError"

    def loadField(self, name):
        with open(f"saves/{name}.json", encoding="utf-8") as F:
            save_data = json.loads(F.readline())
        if save_data.get("FieldType") is not None and save_data.get("FieldType") in self.field_types:
            self.field_type = save_data.get("FieldType")
            self.__createFieldGeometry__(self.field_type)
            self.__createField__()
        else:
            return "BadSave"
        filed_cells = save_data.get("FiledCells")
        for i in range(len(filed_cells)):
            self.cellUpdate(filed_cells[i][0], filed_cells[i][1], filed_cells[i][2])







