from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar
import random
import os


ASSETS_PATH = os.path.abspath("assets/gui_assets/question_frame")


class question_frame(Tk):
    question_font_size = 18
    font_size = 14

    def __shuffle_keys(self, question: dict):
        keys = list(question.keys())
        random.shuffle(keys)

        q_index = keys.index("question")
        keys[0], keys[q_index] = keys[q_index], keys[0]

        return keys

    def __define_func_list(self, keys_list):
        temp = []
        for k in keys_list:
            if k == "answer":
                temp.append(self.__correct_ans)
            else:
                temp.append(self.__incorrect_ans)

        return temp

    def __correct_ans(self):
        self.answer = 1
        self.btn_list[self.randomized_keys.index("answer") - 1].configure(bg="#25C904")
        self.after(500, self.destroy)

    def __incorrect_ans(self):
        self.answer = -1
        self.__canvas.create_text(
            80.0,
            200.0,
            anchor="nw",
            text="Soruyu yanlış cevapladınız",
            fill="#BF0000",
            font=("Inter", 20 * -1),
        )
        self.after(500, self.destroy)

    def format_question_text(self, question):
        q = question.split()
        s = ""
        while len(q) > 4:
            for i in range(4):
                s += f"{q[i]} "
            s += "\n"
            del q[0:4]

        for i in q:
            s += f"{i} "

        return s

    def __init__(self, qa_dict: dict):
        super().__init__()
        self.geometry("650x414")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)
        self.answer = -1

        self.randomized_keys = self.__shuffle_keys(qa_dict)
        self.func_list = self.__define_func_list(self.randomized_keys)
        self.btn_list = []

        self.btn1_text = StringVar(value=self.format_question_text(qa_dict[self.randomized_keys[1]]))
        self.btn2_text = StringVar(value=self.format_question_text(qa_dict[self.randomized_keys[2]]))
        self.btn3_text = StringVar(value=self.format_question_text(qa_dict[self.randomized_keys[3]]))
        self.btn4_text = StringVar(value=self.format_question_text(qa_dict[self.randomized_keys[4]]))

        self.__canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=414,
            width=650,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.__canvas.place(x=0, y=0)

        self.image_1 = PhotoImage(file=f"{ASSETS_PATH}/image_1.png")
        self.__image_1 = self.__canvas.create_image(325.0, 207.0, image=self.image_1)

        self.button_1 = Button(
            bg="#AF70B6",
            fg="#FFFFFF",
            textvariable=self.btn1_text,
            borderwidth=0,
            highlightthickness=0,
            command=self.func_list[1],
            relief="flat",
            font=("Inter", question_frame.font_size * -1),
        )
        self.btn_list.append(self.button_1)

        self.button_2 = Button(
            bg="#4C1072",
            fg="#FFFFFF",
            textvariable=self.btn2_text,
            borderwidth=0,
            highlightthickness=0,
            command=self.func_list[2],
            relief="flat",
            font=("Inter", question_frame.font_size * -1),
        )
        self.btn_list.append(self.button_2)

        self.button_3 = Button(
            bg="#DA92B5",
            fg="#FFFFFF",
            textvariable=self.btn3_text,
            borderwidth=0,
            highlightthickness=0,
            command=self.func_list[3],
            relief="flat",
            font=("Inter", question_frame.font_size * -1),
        )
        self.btn_list.append(self.button_3)

        self.button_4 = Button(
            bg="#AC1305",
            fg="#FFFFFF",
            textvariable=self.btn4_text,
            borderwidth=0,
            highlightthickness=0,
            command=self.func_list[4],
            relief="flat",
            font=("Inter", question_frame.font_size * -1),
        )
        self.btn_list.append(self.button_4)

        self.button_1.place(x=355.0, y=323.0, width=245.0, height=55.0)
        self.button_2.place(x=91.0, y=323.0, width=245.0, height=55.0)
        self.button_3.place(x=280.0, y=228.0, width=245.0, height=55.0)
        self.button_4.place(x=17.0, y=228.0, width=245.0, height=55.0)

        self.__canvas.create_text(
            10.0,
            40.0,
            anchor="nw",
            text=self.format_question_text(qa_dict["question"]),
            fill="#000000",
            font=("Inter", question_frame.question_font_size * -1),
        )
        try:
            self.after(7000, lambda: self.destroy())
        except:
            print("the window has already been terminated")
        self.mainloop()
