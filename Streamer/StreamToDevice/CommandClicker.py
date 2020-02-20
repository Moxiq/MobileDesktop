import ctypes


class CommandClicker:
    screen_res = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
    @staticmethod
    def click_xy(x, y):
        """
        Clicks on a position on the screen.
        :param x: width where the click should occur in PERCENT
        :param y: height where the click should occur in PERCENT
        """
        new_x = int(CommandClicker.screen_res[0] * (x / 100))
        new_y = int(CommandClicker.screen_res[1] * (y / 100))
        ctypes.windll.user32.SetCursorPos(new_x, new_y)
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left up
        print("Clicked " + str(new_x) + "," + str(new_y))


if __name__ == '__main__':
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    print(screensize)
    # CommandClicker.click_xy(1920, 1080)
