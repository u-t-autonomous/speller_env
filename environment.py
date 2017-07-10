# speller_env
import pygame
import csv

class P300:
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    pygame.display.set_caption("P300 Speller")
    pygame.init()

    def __init__(self, s_x=650, s_y=480):
        self.s_x = s_x
        self.s_y = s_y
        self.l = int(round(s_x / 10) - 33)
        self.w = int(round(s_y / 2))
        self.x_1 = int(round(3 * ((s_x / 10) - (s_x / 19.1176))))
        self.y_1 = int(round(s_y / 5) - (s_y / 12))
        self.l_1 = int(round(s_x / 10) - 33)
        self.w_1 = int(round(s_y / 2))
        self.screen = pygame.display.set_mode((s_x, s_y))
        self.x = int(round(3 * ((s_x / 10) - (s_x / 19.1176))))
        self.y = int(round(s_y / 5) - (s_y / 12))
        self.x1 = int(round(3 * ((s_x / 10) - (s_x / 19.1176))))
        self.y1 = int(round(self.s_y / 4) - (self.s_x / 30))
        self.ci = ((s_x / 1000) + 0.4) * int(round(s_x / 15.11627907))
        self.ri = int(round(s_y / 9.056603774))
        self.col_rect = (self.x, self.y, self.l, self.w)
        self.map_rect = (self.x_1, self.y_1, self.l_1, self.w_1)
        sf = int(round((s_y + s_x) / 28.25))
        self.font = pygame.font.Font(None, sf)
        self.font_2 = pygame.font.Font(None, sf - 7)
        pygame.display.set_caption("P300 Speller")
        self.rx = (s_x / 5) + (s_y / 6)
        self.ry = (s_y / 6.4)
        self.xf = self.x1 + (6 * self.ci)
        self.yf = self.y1 + (3 * self.ri)
        self.spce = (25 * (s_y / 240))
        self.done = False
        self.row_1 = self.font.render("1     A   B   C   D   E    F   G", True, (255, 255, 255))
        self.row_2 = self.font.render("2     H    I   J    K   L    M   N", True, (255, 255, 255))
        self.row_3 = self.font.render("3     O   P   Q   R   S    T   U", True, (255, 255, 255))
        self.row_4 = self.font.render("4     V   W   X   Y   Z      ", True, (255, 255, 255))
        self.header = self.font.render("       1   2    3    4    5    6    7", True, (255, 250, 255))
        self.delete = self.font_2.render("                                                   del  ", True,
                                         (255, 255, 255))
        self.col_num = 0
        self.row_num = 0
        self.row_col = (self.row_num, self.col_num)
        self.output_string = ""
        self.output = self.font.render(self.output_string, True, (255, 255, 255))
        self.col_mapping = {self.x1: 1, round(self.x1 + (1 * self.ci), 1): 2, round(self.x1 + (2 * self.ci), 1): 3,
                            round(self.x1 + (3 * self.ci), 1): 4,
                            round(self.x1 + (4 * self.ci), 1): 5, round(self.x1 + (5 * self.ci), 1): 6,
                            round((self.x1 + (6 * self.ci)), 1): 7}
        self.row_mapping = {self.y1: 1, round(self.y1 + (1 * self.ri), 1): 2, round(self.y1 + (2 * self.ri), 1): 3,
                            round(self.y1 + (3 * self.ri), 1): 4}
        self.out = {(1, 1): "A", (1, 2): "B", (1, 3): "C", (1, 4): "D", (1, 5): "E", (1, 6): "F", (1, 7): "G",
                    (2, 1): "H",
                    (2, 2): "I", (2, 3): "J", (2, 4): "K", (2, 5): "L", (2, 6): "M", (2, 7): "N", (3, 1): "O",
                    (3, 2): "P",
                    (3, 3): "Q", (3, 4): "R", (3, 5): "S", (3, 6): "T", (3, 7): "U", (4, 1): "V", (4, 2): "W",
                    (4, 3): "X",
                    (4, 4): "Y", (4, 5): "Z", (4, 6): " ", (4, 7): ""}
        self.output_string = ""
        # Rendering Table
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.row_1,
                         (self.rx - self.row_1.get_width() // 2, (self.ry + self.spce) - self.row_1.get_height() // 2))
        self.screen.blit(self.row_2, (
            self.rx - self.row_1.get_width() // 2, (self.ry + (2 * self.spce)) - self.row_1.get_height() // 2))
        self.screen.blit(self.row_3, (
            self.rx - self.row_1.get_width() // 2, (self.ry + (3 * self.spce)) - self.row_1.get_height() // 2))
        self.screen.blit(self.row_4, (
            self.rx - self.row_1.get_width() // 2, (self.ry + (4 * self.spce)) - self.row_1.get_height() // 2))
        self.screen.blit(self.header, (self.rx - self.header.get_width() // 2, self.ry - self.row_1.get_height() // 2))
        self.screen.blit(self.output, (
            self.rx - self.row_1.get_width() // 2, (self.ry + (6 * self.spce)) - self.row_1.get_height() // 2))
        self.screen.blit(self.delete, (
            self.rx - self.row_1.get_width() // 2, (self.ry + (4 * self.spce)) - self.row_1.get_height() // 2))
        pygame.draw.rect(self.screen, (255, 255, 255), self.col_rect, 2)
        self.stage = 1
        self.log = ["(Log Number, Action, Selecting Column, Selecting Row, Output)"]
        self.iteration = 0
        self.selecting_col = 0
        self.str_so_far = self.output_string
        self.selecting_row = 0
        self.num = 0
        self.action_var = (self.num, self.stage)
        self.data = [['Log Number', 'Action', 'Selecting Column', 'Selecting Row', 'Letter Coordinate', 'Output']]
        self.action = {(1, 1): "Right", (2, 1): "Left", (0, 1): "Column Select", (1, 2): "Up", (2, 2): "Down",
                       (0, 2): "Row Select"}
        pygame.display.flip()

    def display_original_table(self):
        output = self.font.render(self.output_string, True, (255, 255, 255))
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.row_1, (
            self.rx - self.row_1.get_width() // 2, (self.ry + self.spce) - self.row_1.get_height() // 2))
        self.screen.blit(self.row_2, (
            self.rx - self.row_1.get_width() // 2, (self.ry + (2 * self.spce)) - self.row_1.get_height() // 2))
        self.screen.blit(self.row_3, (
            self.rx - self.row_1.get_width() // 2, (self.ry + (3 * self.spce)) - self.row_1.get_height() // 2))
        self.screen.blit(self.row_4, (
            self.rx - self.row_1.get_width() // 2, (self.ry + (4 * self.spce)) - self.row_1.get_height() // 2))
        self.screen.blit(self.header,
                         (self.rx - self.header.get_width() // 2, self.ry - self.row_1.get_height() // 2))
        self.screen.blit(output, (
            self.rx - self.row_1.get_width() // 2, (self.ry + (7 * self.spce)) - self.row_1.get_height() // 2))
        self.screen.blit(self.delete, (
            self.rx - self.row_1.get_width() // 2, (self.ry + (4 * self.spce)) - self.row_1.get_height() // 2))

    def rect_dim(self):
        if self.stage == 1:
            self.y = int(round(self.s_y / 5) - (self.s_y / 12))
            self.l = int(round(self.s_x / 10) - 33)
            self.w = int(round(self.s_y / 2))
        elif self.stage == 2:
            self.x = int(round(self.s_x / 26))
            self.l = int(round((self.s_x / 13) * 9))
            self.w = int(round(self.s_y / 15))

    def map_rect_dim(self):
        self.y_1 = int(round(self.s_y / 5) - (self.s_y / 12))
        self.l_1 = int(round(self.s_x / 10) - 33)
        self.w_1 = int(round(self.s_y / 2))

    def logging(self):
        self.iteration += 1
        self.action_var = (self.num, self.stage)
        if self.stage == 1:
            self.selecting_col = self.col_mapping[self.x]
        elif self.stage == 2:
            self.selecting_row = self.row_mapping[self.y]
        action = self.action[self.action_var]
        log_output = "(" + str(self.iteration) + ", " + action + ", " + str(self.selecting_col) + ", " + str(
            self.selecting_row) + ', ' + str(self.row_col) + ", " + self.output_string + ")"
        self.log.append(log_output)

    def store_log(self):
        self.log_output = []
        self.iteration += 1
        self.action_var = (self.num, self.stage)
        if self.stage == 1:
            self.selecting_col = self.col_mapping[self.x]
        elif self.stage == 2:
            self.selecting_row = self.row_mapping[self.y]
        action = self.action[self.action_var]
        if self.num != 1 and self.num != 2 and self.num != 0:
             action = "Quit"
        self.log_output = [str(self.iteration), action, str(self.selecting_col), str(
            self.selecting_row), self.output_string]
        self.data.append(self.log_output)

    def get_state(self):
        self.state = [str(self.iteration), str(self.selecting_col), str(
            self.selecting_row), self.output_string]
        print( self.state)

    def show_log(self, filename='log.csv'):
        with open(filename, 'w', newline='') as fp:
            self.a = csv.writer(fp, delimiter=',')
            self.a.writerows(self.data)
        print(self.data)

    def horizontal_move(self):

        self.display_original_table()
        self.store_log()
        # Code for Move Right
        if self.num == 1 and  self.x != self.xf:
            self.x = round(self.x + self.ci, 1)
            self.x_1 = round(self.x_1 + self.ci, 1)
        # Code for Move Left
        elif self.num == 2 and self.x != self.x1:
            self.x = round(self.x - self.ci, 1)
            self.x_1 = round(self.x_1 - self.ci, 1)
        self.rect_dim()
        self.col_rect = (self.x, self.y, self.l, self.w)
        self.map_rect = (self.x_1, self.y_1, self.l_1, self.w_1)
        pygame.draw.rect(self.screen, (255, 255, 255), self.col_rect, 2)
        pygame.display.flip()

    def choose_col(self):
        self.col_num = self.col_mapping[self.x]
        self.row_col = (self.row_num, self.col_num)
        self.store_log()
        self.display_original_table()
        self.y = int(round(self.s_y / 4) - (self.s_x / 30))
        self.stage = 2
        self.rect_dim()
        self.col_rect = (self.x, self.y, self.l, self.w)
        self.map_rect_dim()
        self.map_rect = (self.x_1, self.y_1, self.l_1, self.w_1)
        self.row_col = (self.row_num, self.col_num)
        pygame.draw.rect(self.screen, (255, 0, 0), self.map_rect, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), self.col_rect, 2)
        print(self.row_col)
        pygame.display.flip()

    def choose_row(self):
        self.row_num = self.row_mapping[self.y]
        self.row_col = (self.row_num, self.col_num)
        self.store_log()
        self.display_original_table()
        self.stage = 1
        self.rect_dim()
        self.x = self.x1
        self.x_1 = int(round(3 * ((self.s_x / 10) - (self.s_x / 19.1176))))
        self.map_rect_dim()
        self.x1 = int(round(3 * ((self.s_x / 10) - (self.s_x / 19.1176))))
        self.y1 = int(round(self.s_y / 4) - (self.s_x / 30))
        self.ci = ((self.s_x / 1000) + 0.4) * int(round(self.s_x / 15.11627907))
        self.ri = int(round(self.s_y / 9.056603774))
        self.col_rect = (self.x, self.y, self.l, self.w)
        self.map_rect = (self.x_1, self.y_1, self.l_1, self.w_1)
        pygame.draw.rect(self.screen, (255, 255, 255), self.col_rect, 2)
        print(self.row_col)
        pygame.display.flip()

    def vertical_move(self):
        self.display_original_table()
        self.store_log()
        if self.num == 1 and self.y != self.y1:
            self.y -= self.ri
        if self.num == 2 and self.y != self.yf:
            self.y += self.ri
        self.rect_dim()
        self.x1 = int(round(3 * ((self.s_x / 10) - (self.s_x / 19.1176))))
        self.ci = ((self.s_x / 1000) + 0.4) * int(round(self.s_x / 15.11627907))
        self.ri = int(round(self.s_y / 9.056603774))
        self.col_rect = (self.x, self.y, self.l, self.w)
        self.map_rect = (self.x_1, self.y_1, self.l_1, self.w_1)
        pygame.draw.rect(self.screen, (255, 0, 0), self.map_rect, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), self.col_rect, 2)
        print(self.row_mapping[self.y])
        pygame.display.flip()

    def choose_letter(self):
        str_1 = self.out[self.row_col]
        self.output_string += str_1
        if self.row_col == (4, 7):
            self.output_string = self.output_string[:-1]
        self.display_original_table()
        self.stage = 1
        self.rect_dim()
        self.x1 = int(round(3 * ((self.s_x / 10) - (self.s_x / 19.1176))))
        self.y_1 = int(round(3 * ((self.s_x / 10) - (self.s_x / 19.1176))))
        self.ci = ((self.s_x / 1000) + 0.4) * int(round(self.s_x / 15.11627907))
        self.ri = int(round(self.s_y / 9.056603774))
        self.col_rect = (self.x, self.y, self.l, self.w)
        self.map_rect = (self.x_1, self.y_1, self.l_1, self.w_1)
        pygame.draw.rect(self.screen, (255, 0, 0), self.map_rect, 2)
        pygame.draw.rect(self.screen, (255, 255, 255), self.col_rect, 2)
        self.row_num = 0
        self.col_num = 0
        self.row_col = (self.row_num, self.col_num)
        print(self.output_string)
        pygame.display.flip()
    # Move Command chooses one action from the methods above
    def move(self, num):
        self.num = num
        if self.num !=0 and self.stage == 1:
            self.horizontal_move()
        elif num == 0 and self.stage == 2:
            self.choose_row()
            self.stage = 1
        elif num == 0 and self.stage == 1:
            self.choose_col()
            self.stage = 2
        elif self.num !=0 and self.stage == 2:
            self.vertical_move()
        if self.col_num != 0 and self.row_num != 0:
            self.choose_letter()
        self.num = 0
