import tkinter as tk
import tkinter.ttk as ttk

from utils.Window import StatefulWindow


class SettingsBar(ttk.Frame):
    def __init__(self, parent: StatefulWindow):
        super().__init__(parent)

        self.parent = parent
        self.background = parent.background

        frame = ttk.Frame(self, height="8m")
        frame.pack(side="top", fill="both", expand=True)
        frame.pack_propagate(False)

        self.label_name = ttk.Label(frame, text="Module Name", width=12)
        self.label_name.pack(side="left")

        self.textbox_name = ttk.Entry(frame)
        self.textbox_name.pack(side="left", expand=True, fill="both")

        self.label_comment = ttk.Label(frame, text="Comment", width=12)
        self.label_comment.pack(side="left", padx=(4, 4))

        self.textbox_comment = ttk.Entry(frame)
        self.textbox_comment.pack(side="left", expand=True, fill="both")

        frame = ttk.Frame(self, height="8m")
        frame.pack(side="top", fill="both", expand=True)
        frame.pack_propagate(False)

        self.label_src = ttk.Label(frame, text="Src. Addr", width=12)
        self.label_src.pack(side="left")

        self.textbox_src = ttk.Entry(frame, state="readonly")
        self.textbox_src.pack(side="left", expand=True, fill="both")

        self.label_dst = ttk.Label(frame, text="Dst. Addr", width=12)
        self.label_dst.pack(side="left", padx=(4, 4))

        self.textbox_dst = ttk.Entry(frame)
        self.textbox_dst.pack(side="left", expand=True, fill="both")

        frame = ttk.Frame(self, height="8m")
        frame.pack(side="top", fill="both", expand=True)
        frame.pack_propagate(False)

        self.label_name = ttk.Label(frame, text="Mode", width=12)
        self.label_name.pack(side="left")

        frame2 = ttk.Frame(frame)
        frame2.pack(side="left", fill="both", expand=True)
        self.mode = tk.BooleanVar(value=True)

        self.checkbox_src = ttk.Radiobutton(
            frame2, text="Source", variable=self.mode, value=True
        )
        self.checkbox_src.pack(side="left", expand=True, fill="both")

        self.checkbox_dst = ttk.Radiobutton(
            frame2, text="Destination", variable=self.mode, value=False
        )
        self.checkbox_dst.pack(side="left", expand=True, fill="both")

        self.label_comment = ttk.Label(frame, text="Destination Address", width=12)
        self.label_comment.pack(side="left", padx=(4, 4))

        self.textbox_comment = ttk.Entry(frame)
        self.textbox_comment.pack(side="left", expand=True, fill="both")
