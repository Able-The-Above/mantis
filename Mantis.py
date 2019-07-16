import os
import time
import sys
import socket
import pygame
#import pygame.camera
import json

config = ("conf.json")
ver = ("0.0.0")
cos = (os.name)
start_up_message = ("EdenGlass Version "+ver+" has launched."+" Running "+cos)
ui_color=(20,20,20)
c_ui_color = (0,255,255)
try:
    x = open(config, "r")
    y = json.loads(x.read())
    x.close()
    mode = (y["mode"])
    user_id=(y["uid"])
    suit_id=(y["sid"])

except IOError:
    print("File Not Found")


def start():
    pygame.init()
    #pygame.camera.init()
    pygame.font.init()
    pygame.display.set_caption("Mantis")
    pygame.mouse.set_visible(False)
    print(start_up_message)
    cnt_dwn = (3)
    for i in list(range(cnt_dwn))[::-1]:
        print(i+1)
        time.sleep(1)


start()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
w, h = screen.get_size()
# Useful values
# mid_h = h//2
# mid_w = w//2
thr_w = w//3
# find, open and start low-res camera
try:
        cam_list = pygame.camera.list_cameras()
        webcam = pygame.camera.Camera(cam_list[0], (320, 240))
        webcam.start()
except Exception:
        print("No cameras")


def draw_border():
        pygame.draw.line(screen, ui_color, [0, 0], [w, 0], 30)
        pygame.draw.line(screen, ui_color, [0, h], [0, 0], 30)
        pygame.draw.line(screen, ui_color, [w, 0], [w, h], 30)
        pygame.draw.line(screen, ui_color, [0, h], [w, h], 30)


def draw_ui():
        pygame.draw.line(screen, ui_color, [0, h-50], [w/3, h-50], 100)
        pygame.draw.line(screen, ui_color, [w, h-50], [thr_w+thr_w, h-50], 100)


def dev_items():
        if mode == "dev":
            myfont = pygame.font.SysFont('Comic Sans MS', 25)
            textsurface = myfont.render("Mode: "+mode, False, (c_ui_color))
            screen.blit(textsurface, (10, h - 60))


def identification():
        ft = pygame.font.SysFont('Comic Sans MS', 25)
        textsurface = ft.render("IDs: "+"["+user_id+"]"+"["+suit_id+"]", False, (c_ui_color))
        screen.blit(textsurface, (10, h - 80))



def internet_online():
        ft = pygame.font.SysFont('Comic Sans MS', 25)

        def is_connected():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                pass
                return False

        if is_connected():
            status = "Online"
        else:
            status = "Offline"
        textsurface = ft.render("Internet: "+status, False, (c_ui_color))
        screen.blit(textsurface, (10, h - 40))



while True:
        try:
            w_cam = webcam.get_image()
            w_cam = pygame.transform.scale(w_cam, (w, h))
            screen.blit(w_cam, (0, 0))
        except Exception:
            pass

        draw_ui()
        draw_border()
        dev_items()
        internet_online()
        identification()

        # draw all updates to display
        pygame.display.update()
        # check for quit events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print("Mantis was Quit")
                    pygame.quit()
                    sys.exit()
