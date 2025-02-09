import pygame
from Task import Task
# from pygame.examples.video import answer

import global_variables
# from game import main


def _remove_one_symbol(string):
    return string[:-2]+'_'


window_w = 1066
window_h = 600
left_margin = 15

def ask_puzzle():
    main_screen = pygame.display.set_mode((window_w, window_h),  flags=pygame.NOFRAME)
    clock = pygame.time.Clock()
    running = True
    got_answer = False

    task_font = pygame.font.SysFont("Arial", 36, bold=True)
    result_font = pygame.font.SysFont("Arial", 60, bold=True)
    text_font = pygame.font.SysFont("Arial", 28)
    header_font = pygame.font.SysFont("Arial", 42, bold=True)
    answer_font = pygame.font.SysFont("Arial", 28, italic=True)
    hint_font = pygame.font.SysFont("Arial", 22, italic=True)
    result = "_"
    frame = 0
    backspace_pressed = False
    time_when_backspace_pressed = None
    any_symbol_pressed = False
    symbol = ""
    time_when_any_symbol_pressed = None
    task = Task()

    while running and not got_answer:
        frame += 1
        clock.tick(30)
        pygame.display.flip()
        main_screen.fill("black")
        pygame.draw.rect(main_screen, (33,) * 3,
                         (text_font.size("Введите ответ:")[0]+2*left_margin, int(window_h*2/3), window_w, 46))
        text_width = answer_font.size(result)[0]
        if frame % 24 <= 24 / 2:
            pygame.draw.rect(main_screen, "black", (text_width, int(window_h*2/3), 0, 46), 1)
        if task_font.size(task.text)[0] > window_w*.8:
            subtexts = task.text.split('\n')
            for i in range(len(subtexts)):
                main_screen.blit(
                task_font.render(subtexts[i], False, "white"),
                (window_w // 2 - task_font.size(subtexts[i])[0] // 2, 200+task_font.size(subtexts[i])[1]*i)
            )
        else:
            main_screen.blit(
            task_font.render(task.text, False, "white"),
            (window_w // 2 - task_font.size(task.text)[0] // 2, 200)
            )

        main_screen.blit(
            task_font.render('Решите задачу для начала игры', False, "white"),
            (window_w // 2 - task_font.size('Решите задачу для начала игры')[0] // 2,
             50)
        )
        main_screen.blit(
            text_font.render("Введите ответ:", False, "white"),
            (left_margin, int(window_h*2/3))
        )
        main_screen.blit(
            answer_font.render(result, False, "white"),
            (left_margin+text_font.size("Введите ответ:")[0]+left_margin, int(window_h*2/3))
        )
        main_screen.blit(
            hint_font.render('Округлите ответ до двух знаков после запятой', False, "white"),
            (left_margin + hint_font.size("Округлите ответ до двух знаков после запятой")[0],
             int(window_h * 2 / 3)+text_font.size("Введите ответ:")[1]+left_margin)
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # result = result.strip()
                if event.key == pygame.K_ESCAPE:
                    running = False
                if  event.key == pygame.K_RETURN:
                    got_answer = True
                elif event.key == pygame.K_BACKSPACE:
                    result = _remove_one_symbol(result)
                    backspace_pressed = True
                    time_when_backspace_pressed = pygame.time.get_ticks()
                else:
                    symbol = event.unicode
                    if symbol in '0123456789.':
                        result = result.strip('_')
                        result += symbol + '_'
                        any_symbol_pressed = True
                        time_when_any_symbol_pressed = pygame.time.get_ticks()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    backspace_pressed = False
                if event.unicode == symbol:
                    any_symbol_pressed = False
                    symbol = ""

        if backspace_pressed and pygame.time.get_ticks() - time_when_backspace_pressed >= 500:
            if frame % 2 == 0:
                result = _remove_one_symbol(result)
        if any_symbol_pressed and pygame.time.get_ticks() - time_when_any_symbol_pressed >= 500:
            if frame % 2 == 0:
                result += symbol

    frame = 0
    if len(result.replace('_', ''))>0:
        correct_result = round(float(result.replace('_', '')), 2) == float(task.answer)
    else:
        correct_result = False
    false_text = 'Ошибка'
    correct_text = 'Правильно'
    correct_answer_text = f"Правильный ответ: {task.answer}"
    while running:
        frame += 1
        clock.tick(30)
        pygame.display.flip()
        main_screen.fill("black")
        if correct_result:
            main_screen.blit(
                result_font.render(correct_text, False, "green"),
                (window_w // 2 - result_font.size(correct_text)[0] // 2,
                 window_h//2-result_font.size(correct_text)[1] // 2)
            )
            main_screen.blit(
                text_font.render(correct_answer_text, False, "green"),
                (window_w // 2 - text_font.size(correct_answer_text)[0] // 2,
                 window_h//2+result_font.size(correct_text)[1]+answer_font.size(correct_answer_text)[1] // 2)
            )
        else:
            main_screen.blit(
                result_font.render(false_text, False, "red"),
                (window_w // 2 - result_font.size(false_text)[0] // 2,
                 window_h//2-result_font.size(false_text)[1] // 2)
            )
            main_screen.blit(
                text_font.render(correct_answer_text, False, "red"),
                (window_w // 2 - text_font.size(correct_answer_text)[0] // 2,
                 window_h//2+result_font.size(false_text)[1]+answer_font.size(correct_answer_text)[1] // 2)
            )
        if frame >= 150:
            running=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # result = result.strip()
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    running = False
    return correct_result