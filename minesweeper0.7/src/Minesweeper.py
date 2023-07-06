import pygame
import random
import subprocess
import csv
from gui import question_window_gui
from pygame import mixer
import os


MUSIC_PATH = os.path.abspath("assets/music")
SPRITES_PATH = os.path.abspath("assets/Sprites")
GUI_SCRIPTS_PATH = os.path.abspath("src/gui")


pygame.init()

bg_color = (192, 192, 192)
grid_color = (128, 128, 128)

game_width = 9  # Change this to increase size
game_height = 9  # Change this to increase size
numMine = 16  # Number of mines
total_time = 200  # total time for session
grid_size = (
    64  # Size of grid (WARNING: macke sure to change the images dimension as well)
)
border = 16  # Top border
top_border = 100  # Left, Right, Bottom border
display_width = grid_size * game_width + border * 2  # Display width
display_height = grid_size * game_height + border + top_border  # Display height
gameDisplay = pygame.display.set_mode((display_width, display_height))  # Create display
timer = pygame.time.Clock()  # Create timer
pygame.display.set_caption("Mayın Tarlası")  # S Set the caption of window

# Import files
temp_tuple = (grid_size, grid_size)
spr_emptyGrid = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/empty.png"), temp_tuple
)
spr_flag = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/flag.png"), temp_tuple
)
spr_grid = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/Grid.png"), temp_tuple
)
spr_grid1 = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/grid1.png"), temp_tuple
)
spr_grid2 = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/grid2.png"), temp_tuple
)
spr_grid3 = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/grid3.png"), temp_tuple
)
spr_grid4 = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/grid4.png"), temp_tuple
)
spr_grid5 = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/grid5.png"), temp_tuple
)
spr_grid6 = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/grid6.png"), temp_tuple
)
spr_grid7 = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/grid7.png"), temp_tuple
)
spr_grid8 = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/grid8.png"), temp_tuple
)
spr_grid7 = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/grid7.png"), temp_tuple
)
spr_mine = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/mine.png"), temp_tuple
)
spr_mineClicked = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/mineClicked.png"), temp_tuple
)
spr_mineFalse = pygame.transform.scale(
    pygame.image.load(f"{SPRITES_PATH}/mineFalse.png"), temp_tuple
)

# Background Music
mixer.music.load(os.path.abspath(f"{MUSIC_PATH}/ballin.mp3"))
mixer.music.play(-1)


# Create global values
grid = []  # The main grid
mines = []  # Pos of the mines
questions = []  # List of questions to be asked
with open("assets/questions.csv", "r", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        questions.append(line)


# Create funtion to draw texts
def drawText(txt, s, yOff=0):
    screen_text = pygame.font.SysFont("Calibri", s, True).render(txt, True, (0, 0, 0))
    rect = screen_text.get_rect()
    rect.center = (
        game_width * grid_size / 2 + border,
        game_height * grid_size / 2 + top_border + yOff,
    )
    gameDisplay.blit(screen_text, rect)


# Create class grid
class Grid:
    def __init__(self, xGrid, yGrid, type):
        self.xGrid = xGrid  # X pos of grid
        self.yGrid = yGrid  # Y pos of grid
        self.clicked = False  # Boolean var to check if the grid has been clicked
        self.mineClicked = (
            False  # Bool var to check if the grid is clicked and its a mine
        )
        self.mineFalse = False  # Bool var to check if the player flagged the wrong grid
        self.flag = False  # Bool var to check if player flagged the grid
        # Create rectObject to handle drawing and collisions
        self.rect = pygame.Rect(
            border + self.xGrid * grid_size,
            top_border + self.yGrid * grid_size,
            grid_size,
            grid_size,
        )
        self.val = type  # Value of the grid, -1 is mine

    def drawGrid(self):
        # Draw the grid according to bool variables and value of grid
        if self.mineFalse:
            gameDisplay.blit(spr_mineFalse, self.rect)
        else:
            if self.clicked:
                if self.val == -1:
                    if self.mineClicked:
                        gameDisplay.blit(spr_mineClicked, self.rect)
                    else:
                        gameDisplay.blit(spr_mine, self.rect)
                else:
                    if self.val == 0:
                        gameDisplay.blit(spr_emptyGrid, self.rect)
                    elif self.val == 1:
                        gameDisplay.blit(spr_grid1, self.rect)
                    elif self.val == 2:
                        gameDisplay.blit(spr_grid2, self.rect)
                    elif self.val == 3:
                        gameDisplay.blit(spr_grid3, self.rect)
                    elif self.val == 4:
                        gameDisplay.blit(spr_grid4, self.rect)
                    elif self.val == 5:
                        gameDisplay.blit(spr_grid5, self.rect)
                    elif self.val == 6:
                        gameDisplay.blit(spr_grid6, self.rect)
                    elif self.val == 7:
                        gameDisplay.blit(spr_grid7, self.rect)
                    elif self.val == 8:
                        gameDisplay.blit(spr_grid8, self.rect)

            else:
                if self.flag:
                    gameDisplay.blit(spr_flag, self.rect)
                else:
                    gameDisplay.blit(spr_grid, self.rect)

    def revealGrid(self):
        self.clicked = True
        # Auto reveal if it's a 0
        if self.val == 0:
            for x in range(-1, 2):
                if self.xGrid + x >= 0 and self.xGrid + x < game_width:
                    for y in range(-1, 2):
                        if self.yGrid + y >= 0 and self.yGrid + y < game_height:
                            if not grid[self.yGrid + y][self.xGrid + x].clicked:
                                grid[self.yGrid + y][self.xGrid + x].revealGrid()

    def updateValue(self):
        # Update the value when all grid is generated
        if self.val != -1:
            for x in range(-1, 2):
                if self.xGrid + x >= 0 and self.xGrid + x < game_width:
                    for y in range(-1, 2):
                        if self.yGrid + y >= 0 and self.yGrid + y < game_height:
                            if grid[self.yGrid + y][self.xGrid + x].val == -1:
                                self.val += 1


def get_rand_question():  # returns dict
    q = questions[random.randrange(0, len(questions))]
    questions.pop(questions.index(q))
    return q


def ask_question(clicked: list):
    if clicked in mines:
        mines.pop(mines.index(clicked))
        frame = question_window_gui.question_frame(get_rand_question())
        return frame.answer
    return


def gameLoop():
    gameState = "Playing"  # Game state
    mineLeft = numMine  # Number of mine left
    global grid  # Access global var
    grid = []
    global mines
    t = 0  # Set time to 0
    cleared_mines = 0

    # Generating mines
    mines = [[random.randrange(0, game_width), random.randrange(0, game_height)]]

    for c in range(numMine - 1):
        pos = [random.randrange(0, game_width), random.randrange(0, game_height)]
        same = True
        while same:
            for i in range(len(mines)):
                if pos == mines[i]:
                    pos = [
                        random.randrange(0, game_width),
                        random.randrange(0, game_height),
                    ]
                    break
                if i == len(mines) - 1:
                    same = False
        mines.append(pos)

    # Generating entire grid
    for j in range(game_height):
        line = []
        for i in range(game_width):
            if [i, j] in mines:
                line.append(Grid(i, j, -1))
            else:
                line.append(Grid(i, j, 0))
        grid.append(line)

    # Update of the grid
    for i in grid:
        for j in i:
            j.updateValue()

    # Main Loop
    while gameState != "Exit":
        # Reset screen
        gameDisplay.fill(bg_color)

        # User inputs
        for event in pygame.event.get():
            # Check if player close window
            if event.type == pygame.QUIT:
                subprocess.Popen(["python", f"{GUI_SCRIPTS_PATH}/menu_gui.py"])
                pygame.display.quit()
                pygame.quit()
            # Check if play restart
            if gameState == "Game Over" or gameState == "Win":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        gameState = "Exit"
                        subprocess.Popen(
                            ["python", os.path.abspath("src/Minesweeper.py")]
                        )
                        pygame.display.quit()
                        pygame.quit()

            else:
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in grid:
                        for j in i:
                            if j.rect.collidepoint(event.pos):
                                if event.button == 1:
                                    # If player left clicked of the grid
                                    j.revealGrid()
                                    # Toggle flag off
                                    if j.flag:
                                        mineLeft += 1
                                        j.falg = False
                                    # If it's a mine
                                    if j.val == -1:
                                        if (random.randrange(0, 10) < 6 and cleared_mines > 1) or len(questions) < 1:
                                            gameState = "Game Over"
                                            j.mineClicked = True

                                        else:
                                            if [j.xGrid, j.yGrid] in mines:
                                                mineLeft -= 1

                                            ans = ask_question([j.xGrid, j.yGrid])
                                            if ans == -1:
                                                gameState = "Game Over"
                                                j.mineClicked = True
                                            elif ans == 1:
                                                gameState = "Playing"
                                                cleared_mines += 1

                                elif event.button == 3:
                                    # If the player right clicked
                                    if not j.clicked:
                                        if j.flag:  # deflag
                                            j.flag = False
                                            mineLeft += 1
                                            if j.val == -1:
                                                cleared_mines -= 1

                                        else:  # flag
                                            j.flag = True
                                            mineLeft -= 1
                                            if j.val == -1:
                                                cleared_mines += 1

        # Check if won
        w = True
        for i in grid:
            for j in i:
                j.drawGrid()
                if j.val != -1 and not j.clicked:
                    w = False
        if w and gameState != "Exit":
            gameState = "Win"

        def count_mineFalse():
            false_mine_num = 0
            for i in grid:
                for j in i:
                    if j.flag and j.val != -1:
                        false_mine_num += 1
            return false_mine_num

        misclicked_mines = (
            count_mineFalse()
        )  # misclicked mines to subtract from the totalscore

        def calculate_score(cleared_mines, remaining_time):
            return round(
                cleared_mines * 100 + remaining_time * 0.3 - misclicked_mines * 100
            )

        text_font = pygame.font.SysFont("Calibri", 50)

        def display_score(cleared_mines):
            remaining_time = total_time - t // 15
            total_score = calculate_score(cleared_mines, remaining_time)
            score = f"Skor: {total_score * 10}"
            score_text = text_font.render(score, True, (0, 0, 0))

            gameDisplay.blit(
                score_text,
                (round(display_width / 2 - text_font.size(score)[0] / 2), border),
            )

        # Draw Texts
        if gameState != "Game Over" and gameState != "Win":
            t += 1
        elif gameState == "Game Over":
            drawText("Oyun bitti!", 50)
            drawText('Tekrar başlamak için "R"', 35, 50)
            count_mineFalse()
            display_score(cleared_mines)
            for i in grid:
                for j in i:
                    if j.flag and j.val != -1:
                        j.mineFalse = True
        else:
            drawText("KAZANDIN!", 50)
            drawText('Tekrar başlamak için "R"', 35, 50)
            count_mineFalse()
            display_score(cleared_mines)
        # Draw time
        s = str(total_time - t // 15)
        if s == "0":
            gameState = "Game Over"
        screen_text = text_font.render(s, True, (0, 0, 0))
        gameDisplay.blit(screen_text, (border, border))

        # Draw mine left
        screen_text = text_font.render(mineLeft.__str__(), True, (0, 0, 0))
        gameDisplay.blit(screen_text, (display_width - border - 50, border))

        pygame.display.update()  # Update screen

        timer.tick(15)  # Tick fps


gameLoop()
pygame.display.quit()
pygame.quit()
quit()
