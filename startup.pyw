import os
import subprocess
import threading
import time

from PIL import Image
from pystray import Icon as TrayIcon
from pystray import Menu, MenuItem
from win10toast import ToastNotifier


APP_NAME = "BAT 静默启动器"


def launch_all_bats(notifier, on_all_done):
    """Run every .bat file in the script directory without opening a console."""
    bat_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "script")

    if not os.path.isdir(bat_folder):
        notifier.show_toast(APP_NAME, "未找到 script 文件夹", duration=5)
        on_all_done()
        return

    bat_files = sorted(
        os.path.join(bat_folder, filename)
        for filename in os.listdir(bat_folder)
        if filename.lower().endswith(".bat")
    )

    if not bat_files:
        notifier.show_toast(APP_NAME, "未找到可运行的 .bat 文件", duration=5)
        on_all_done()
        return

    results = []
    startup_info = subprocess.STARTUPINFO()
    startup_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    for bat_file in bat_files:
        name = os.path.basename(bat_file)
        try:
            subprocess.Popen(
                ["cmd.exe", "/c", bat_file],
                startupinfo=startup_info,
                creationflags=subprocess.CREATE_NO_WINDOW,
            )
            results.append(name)
        except OSError:
            results.append(f"{name}（启动失败）")

        time.sleep(0.2)

    notifier.show_toast(
        APP_NAME,
        ("已启动：\n" + "\n".join(results))[:256],
        duration=6,
        threaded=True,
    )

    time.sleep(3)
    on_all_done()


def create_tray_icon(on_exit):
    image = Image.new("RGB", (64, 64), color="#2563eb")
    return TrayIcon(
        APP_NAME,
        image,
        menu=Menu(MenuItem("退出", lambda icon, menu_item: on_exit())),
    )


def main():
    notifier = ToastNotifier()
    icon = create_tray_icon(lambda: icon.stop())

    threading.Thread(
        target=launch_all_bats,
        args=(notifier, icon.stop),
        daemon=True,
    ).start()
    icon.run()


if __name__ == "__main__":
    main()
