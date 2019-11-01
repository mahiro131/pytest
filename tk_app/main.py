import tkinter as tk

#メインウィンドウ作成
root = tk.Tk()

#ウィンドウサイズを指定
root.geometry("550x400")

#ラベルを追加
label = tk.Label(root,text='Hello')

label.grid()

button = tk.Button(root, text="true", command=lambda: pushed(button))
button.grid()

# 描画
root.mainloop()