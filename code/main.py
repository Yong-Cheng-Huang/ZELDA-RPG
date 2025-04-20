import pygame
import sys
from settings import *
from level import Level
import time


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Zelda')
        icon = pygame.image.load('graphics/test/player.png')
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.level = None

        # Sound effects
        self.main_sound = pygame.mixer.Sound('audio/main.ogg')
        self.main_sound.set_volume(0.6)
        self.main_sound.play(loops=-1)

        self.start_sound = pygame.mixer.Sound('audio/start.wav')
        self.start_sound.set_volume(0.6)

        self.game_over_sound = pygame.mixer.Sound('audio/gameover.wav')
        self.game_over_sound.set_volume(0.8)

        self.win_sound = pygame.mixer.Sound('audio/win.wav')
        self.win_sound.set_volume(0.8)

        # Fonts
        self.font = pygame.font.Font(UI_FONT, 90)
        self.instruction_font = pygame.font.Font(UI_FONT, 50)

        # Game state flags
        self.game_over = False
        self.game_complete = False
        self.game_started = False
        self.difficulty = None
        self.target_score = 0

        # Instruction screen background
        self.instruction_background = pygame.image.load(
            'graphics/cover.jpg').convert()
        self.instruction_background = pygame.transform.scale(
            self.instruction_background, (WIDTH, HEIGTH))

        # Game over and game complete timers
        self.game_over_timer = None
        self.game_complete_timer = None
        self.game_over_delay = 1
        self.game_complete_delay = 1.5

    def end_game(self):
        pygame.mixer.stop()

    def activate_game_over(self):
        self.game_over = True
        self.end_game()
        self.game_over_timer = None
        self.game_over_sound.play()

    def activate_game_complete(self):
        self.game_complete = True
        self.end_game()
        self.win_sound.play()
        self.game_complete_timer = None

    def display_instructions(self):
        self.screen.blit(self.instruction_background, (0, 0))
        overlay = pygame.Surface((WIDTH, HEIGTH), pygame.SRCALPHA)
        overlay.fill((190, 190, 190, 80))
        self.screen.blit(overlay, (0, 0))

        title_font = pygame.font.Font(UI_FONT, 70)
        instruction_font = pygame.font.Font(UI_FONT, 23)
        start_font = pygame.font.Font(UI_FONT, 20)

        instructions = [
            "Welcome to Zelda",
            "arrow - Move",
            "Space - Attack",
            "M - Menu",
            "W - Magic",
            "Q - Switch Weapon",
            "R - Switch Magic",
            "S - Pause",
            "1 - Easy   2 - Normal   3 - Hard"
        ]

        title_text = title_font.render(instructions[0], True, (255, 255, 255))
        title_rect = title_text.get_rect(
            center=(WIDTH // 2, HEIGTH // 2 - 250))
        self.screen.blit(title_text, title_rect)

        for i, line in enumerate(instructions[1:len(instructions)-1]):
            instruction_text = instruction_font.render(
                line, True, (255, 255, 255))
            text_rect = instruction_text.get_rect(
                center=(WIDTH // 2, HEIGTH // 2 - 120 + i * 60))
            self.screen.blit(instruction_text, text_rect)

        difficulty_text = start_font.render(
            instructions[-1], True, (255, 255, 255))
        difficulty_rect = difficulty_text.get_rect(
            center=(WIDTH // 2, HEIGTH // 2 + 320))
        self.screen.blit(difficulty_text, difficulty_rect)

        pygame.display.update()

    def display_game_over(self):
        overlay = pygame.Surface((WIDTH, HEIGTH), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))
        game_over_text = self.font.render('Game Over', True, (255, 255, 255))
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGTH // 2))
        self.screen.blit(game_over_text, text_rect)
        instruction_font = pygame.font.Font(UI_FONT, 30)
        press_to_quit_text = instruction_font.render(
            'Q - Quit', True, (255, 255, 255))
        press_to_restart_text = instruction_font.render(
            'R - Restart', True, (255, 255, 255))

        quit_text_rect = press_to_quit_text.get_rect(
            left=(WIDTH - press_to_quit_text.get_width()) // 2, top=HEIGTH // 2 + 160)
        restart_text_rect = press_to_restart_text.get_rect(
            left=(WIDTH - press_to_restart_text.get_width()) // 2, top=HEIGTH // 2 + 100)

        self.screen.blit(press_to_restart_text, restart_text_rect)
        self.screen.blit(press_to_quit_text, quit_text_rect)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_r:
                        self.game_started = False
                        self.game_over = False
                        self.difficulty = None
                        self.target_score = 0
                        self.game_complete_timer = None
                        self.main_sound.play(loops=-1)
                        self.run()

    def display_game_complete(self):
        overlay = pygame.Surface((WIDTH, HEIGTH), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))
        game_complete_text = self.font.render(
            'Game Complete', True, (255, 255, 255))
        text_rect = game_complete_text.get_rect(
            center=(WIDTH // 2, HEIGTH // 2))
        self.screen.blit(game_complete_text, text_rect)
        instruction_font = pygame.font.Font(UI_FONT, 30)
        press_to_quit_text = instruction_font.render(
            'Q - Quit', True, (255, 255, 255))
        press_to_restart_text = instruction_font.render(
            'R - Restart', True, (255, 255, 255))

        quit_text_rect = press_to_quit_text.get_rect(
            left=(WIDTH - press_to_quit_text.get_width()) // 2, top=HEIGTH // 2 + 160)
        restart_text_rect = press_to_restart_text.get_rect(
            left=(WIDTH - press_to_restart_text.get_width()) // 2, top=HEIGTH // 2 + 110)

        self.screen.blit(press_to_restart_text, restart_text_rect)
        self.screen.blit(press_to_quit_text, quit_text_rect)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_r:
                        self.game_started = False
                        self.game_complete = False
                        self.difficulty = None
                        self.target_score = 0
                        self.game_complete_timer = None
                        self.main_sound.play(loops=-1)
                        self.run()

    def display_pause_screen(self):
        # Create a transparent surface for the overlay
        overlay = pygame.Surface((WIDTH, HEIGTH), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 0))  # Set the alpha value to 0 for transparency
        self.screen.blit(overlay, (0, 0))
    # Display the pause text
        pause_text = self.font.render('Paused', True, (255, 255, 255))
        text_rect = pause_text.get_rect(center=(WIDTH // 2, HEIGTH // 2))
        self.screen.blit(pause_text, text_rect)
        pygame.display.update()

    def display_difficulty(self):
        difficulty_text_font = pygame.font.Font(UI_FONT, 16)
        difficulty_text = difficulty_text_font.render(
            f"{self.difficulty} {self.target_score} pt", True, (255, 255, 255))
        difficulty_rect = difficulty_text.get_rect(center=(WIDTH // 2, 25))
        self.screen.blit(difficulty_text, difficulty_rect)

    def set_target_score(self):
        scores = {
            'Easy': 100,
            'Normal': 125,
            'Hard': 150
        }
        self.target_score = scores.get(self.difficulty, 200)

    def adjust_monster_stats(self, difficulty):
        factors = {
            'Easy': 0.6,
            'Normal': 1.0,
            'Hard': 1.2
        }
        factor = factors.get(difficulty, 1.0)

        # Adjust monster stats based on difficulty
        for monster in monster_data.values():
            monster['health'] = int(monster['health'] * factor)
            monster['exp'] = int(monster['exp'] * factor)
            monster['damage'] = int(monster['damage'] * factor)
            monster['speed'] = int(monster['speed'] * factor)
            monster['resistance'] = int(monster['resistance'] * factor)
            monster['attack_radius'] = int(
                monster['attack_radius'] * factor * 0.9)
            monster['notice_radius'] = int(
                monster['notice_radius'] * factor)

    def run(self):
        paused = False  # Flag to track if the game is paused
        while True:
            if not self.game_started:
                self.display_instructions()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            self.difficulty = 'Easy'
                        elif event.key == pygame.K_2:
                            self.difficulty = 'Normal'
                        elif event.key == pygame.K_3:
                            self.difficulty = 'Hard'
                        if self.difficulty:
                            self.set_target_score()
                            self.adjust_monster_stats(self.difficulty)
                            self.level = Level(self.difficulty)
                            self.game_started = True
                            self.start_sound.play()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m:
                            self.level.toggle_menu()
                            pygame.mixer.music.load("audio/menu-open.mp3")
                            pygame.mixer.music.set_volume(1.5)
                            pygame.mixer.music.play()

                        # Pause and unpause the game
                        if event.key == pygame.K_s:
                            paused = not paused
                            if paused:
                                pygame.mixer.music.pause()
                            else:
                                pygame.mixer.music.unpause()

                if paused:
                    self.display_pause_screen()
                    continue

                self.screen.fill(WATER_COLOR)
                self.level.run()
                self.display_difficulty()

                if self.level.player.health <= 0 and not self.game_over:
                    if self.game_over_timer is None:
                        self.game_over_timer = time.time()
                    elif time.time() - self.game_over_timer >= self.game_over_delay:
                        self.activate_game_over()

                if self.level.player.score >= self.target_score and not self.game_over:
                    if self.game_complete_timer is None:
                        self.game_complete_timer = time.time()
                    elif time.time() - self.game_complete_timer >= self.game_complete_delay:
                        self.activate_game_complete()

                if self.game_over:
                    self.display_game_over()
                    return

                if self.game_complete:
                    self.display_game_complete()
                    return

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
