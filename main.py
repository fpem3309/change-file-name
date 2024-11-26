from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
import os

tk = Tk()
tk.title("파일 이름 변환기")
tk.geometry("550x400")


# 파일탐색기 열어서 경로 가져오기
def load_path():
    directory_path["text"] = filedialog.askdirectory()


def change_string_preview():
    file_names = os.listdir(directory_path["text"])

    if file_name_before_input.get() == "":
        showerror("오류", "변경할 문자를 입력해주세요")
        return

    if len(file_names) < 1:
        showerror("오류", "경로에 파일이 없습니다.")
        return

    predict_file_names.delete(0, END)
    for name in file_names:
        re_name = name
        re_name = re_name.replace(
            file_name_before_input.get(), file_name_after_input.get()
        )
        if name != re_name:  # 파일명이 변경됐다면
            predict_file_names.insert(END, "%s ➡️ %s 로 변경합니다.\n" % (name, re_name))


# 파일명 변경
def change_string():
    change_count = 0
    file_names = os.listdir(directory_path["text"])

    if file_name_before_input.get() == "":
        showerror("오류", "변경할 문자를 입력해주세요")
        return

    if len(file_names) < 1:
        showerror("오류", "경로에 파일이 없습니다.")
        return

    if askyesno("확인", "정말 변경하시겠습니까?"):
        for name in file_names:
            src = os.path.join(directory_path["text"], name)

            re_name = name
            re_name = re_name.replace(
                file_name_before_input.get(), file_name_after_input.get()
            )

            if name != re_name:  # 파일명이 변경됐다면
                re_src = os.path.join(directory_path["text"], re_name)
                try:
                    os.rename(src, re_src)
                    change_count += 1
                except FileExistsError as e:
                    print(e)
                    showerror("오류", "해당 이름의 파일이 이미 있습니다.")
        message = str(change_count) + "개의 파일명이 변경되었습니다."
        showinfo("성공", message)
    else:
        print("취소")


directory_path_label = Label(tk, text="폴더 경로")
load_button = Button(tk, text="경로 불러오기", command=load_path, fg="#fff", bg="#B404AE")
directory_path = Label(tk, text="/")


# 변경할 문자 입력
file_name_before_label = Label(tk, text="변경할 문자")
file_name_before_input = Entry(tk)

file_name_after_label = Label(tk, text="변경될 문자")
file_name_after_input = Entry(tk)

predict_file_names = Listbox(tk, width=75, height=10)
preview_button = Button(
    tk, text="미리보기", command=change_string_preview, fg="#fff", bg="#04B404"
)

change_button = Button(
    tk, text="변경하기", command=change_string, fg="#fff", bg="#045FB4"
)

directory_path_label.grid(row=0, column=0, padx=10, pady=10)
directory_path.grid(row=0, column=1)
load_button.grid(row=0, column=2)
file_name_before_label.grid(row=1, column=0, padx=10, pady=10)
file_name_before_input.grid(row=1, column=1)
file_name_after_label.grid(row=2, column=0, padx=10, pady=10)
file_name_after_input.grid(row=2, column=1)
predict_file_names.grid(row=3, column=0, columnspan=5, padx=10, pady=10)
preview_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
change_button.grid(row=4, column=1, columnspan=2)
tk.mainloop()
