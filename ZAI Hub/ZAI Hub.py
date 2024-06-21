import os  
import tkinter as tk  
from tkinter import scrolledtext  
  
def check_and_create_zai_dir():  
    zai_dir = '.zai'  
    if not os.path.exists(zai_dir):  
        os.makedirs(zai_dir)  
        os.makedirs(os.path.join(zai_dir, 'version'))  
        os.makedirs(os.path.join(zai_dir, 'libraries'))  
        os.makedirs(os.path.join(zai_dir, 'assets'))  
        print("ZAI directory and subdirectories created successfully!")  
    else:  
        print("ZAI directory already exists.")  
  
def main():  
    root = tk.Tk()  
    root.title("ZAI Hub")  
      
    # 设置窗口大小  
    root.geometry("648x424")  
      
    # 创建一个左侧框架  
    left_frame = tk.Frame(root, bg='#f0f0f0')  # 假设使用浅灰色背景  
    left_frame.pack(side="left", fill="y", expand=True, padx=10, pady=10)  
      
    # 顶部标题  
    download_label = tk.Label(left_frame, text="下载", font=("Arial", 14), bg='#f0f0f0')  
    download_label.pack(side="top", fill="x", pady=(10, 0))  
      
    # 列表框  
    listbox = tk.Listbox(left_frame, bg='white', font=("Arial", 12))  
    listbox.pack(side="top", fill="both", expand=True, padx=10, pady=10)  
      
    # 添加列表项  
    listbox.insert(tk.END, "哉-夏")  # 你可以添加更多项  
      
    # 检查并创建 .zai 目录  
    check_and_create_zai_dir()  
      
    # 启动 GUI 事件循环  
    root.mainloop()  
  
if __name__ == "__main__":  
    main()
