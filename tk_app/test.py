import tkinter as tk

def pushed(b):
    if b["text"] != 'false':
        b["text"] = "false"
    else:
        b["text"] = "true"


#メインウィンドウ作成
root = tk.Tk()

#タイトル
root.title("Tkinter test")

#ウィンドウサイズを指定
root.geometry("550x400")

#ラベルを追加
label = tk.Label(root,text='Hello')

label.grid()

button = tk.Button(root, text="true", command=lambda: pushed(button))
button.grid()

# 描画
root.mainloop()