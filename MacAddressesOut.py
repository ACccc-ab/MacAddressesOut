import subprocess
import re
import os
from tkinter import Tk, Button, Label


# 获取本机所有MAC地址
def get_mac_addresses():
    output = subprocess.check_output(["getmac", "/FO", "CSV", "/NH"])
    output = output.decode(errors="replace").encode().decode()

    mac_addresses = re.findall(r"\"([\w-]+)\"", output)
    mac_addresses = [mac.replace("-", ":") for mac in mac_addresses]  # 将 '-' 替换为 ':'
    return mac_addresses



# 复制MAC地址到剪贴板
def copy_to_clipboard(mac_address):
    root = Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(mac_address)
    root.update()
    root.destroy()


# 导出MAC地址到文件
def export_to_file(mac_addresses):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "mac_addresses.txt")

    with open(file_path, "w") as file:
        for mac_address in mac_addresses:
            file.write(mac_address + "\n")

# 创建GUI窗口
def create_gui(mac_addresses):
    root = Tk()
    root.title("MAC地址列表")


    for i, mac_address in enumerate(mac_addresses):
        label = Label(root, text=mac_address)
        label.grid(row=i, column=0)

        copy_button = Button(root, text="复制", command=lambda mac=mac_address: copy_to_clipboard(mac))
        copy_button.grid(row=i, column=1)

    export_button = Button(root, text="导出", command=lambda: export_to_file(mac_addresses))
    export_button.grid(row=len(mac_addresses), column=0, columnspan=2)

    root.geometry("150x200")
    root.mainloop()

# 获取MAC地址并展示
mac_addresses = get_mac_addresses()
create_gui(mac_addresses)
