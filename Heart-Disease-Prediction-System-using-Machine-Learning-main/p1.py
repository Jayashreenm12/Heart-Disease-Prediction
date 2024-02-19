import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import pandas as pd

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabbed GUI")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")

        self.tabs = [
            ("Data Collection", [
                ("Load Data", "This is Loading Data tab"),
                ("Display Columns Name", "This is Display Columns Name tab"),
                ("Shape of Dataset", "This is Shape of Dataset tab"),
                ("Describing Data", "This is Describing Data tab"),
                ("Dataset Information", "This is Dataset Information tab"),
                ("Check for Missing Values", "This is Checking for Missing Values tab")
            ]),
            ("Data Visualization", "This is Data Visualization tab"),
            ("Splitting Features and Target", "This is Splitting tab"),
            ("Train-Test Split", "This is Train-Test Split tab"),
            ("Model Training", "This is Model Training tab"),
            ("Model Evaluation", "This is Model Evaluation tab"),
            ("Predicting Results", "This is Predicting Results tab"),
            ("Saving Model", "This is Saving Model tab")
        ]

        self.frames = []

        for tab_name, sub_tabs in self.tabs:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=tab_name)
            self.frames.append(frame)

            if isinstance(sub_tabs, list):
                sub_notebook = ttk.Notebook(frame)
                sub_notebook.pack(expand=True, fill="both")

                sub_frames = []
                for sub_tab_name, sub_tab_label in sub_tabs:
                    # Load data into a pandas DataFrame
                    heart_data = pd.read_csv("dataset/heart.csv")
                    sub_frame = ttk.Frame(sub_notebook)
                    sub_notebook.add(sub_frame, text=sub_tab_name)
                    sub_frames.append(sub_frame)

                    text_area = scrolledtext.ScrolledText(sub_frame, wrap=tk.WORD, width=60, height=20)
                    text_area.pack(padx=10, pady=10)

                    # Replace the following with your data processing logic
                    if sub_tab_name == "Load Data":
                        
                        text_area.insert(tk.END, "Loading data into Pandas DataFrame...")
                        #text_area.insert(tk.END, str('\n\n' + str(heart_data.columns) + '\n\n' + str(heart_data.shape) + '\n\n' + str(heart_data.describe())))

                        # Example: df = pd.read_csv('your_file.csv')
                        # Display results in text_area

                
                    if sub_tab_name == "Display Columns Name":
                        text_area.insert(tk.END, str('\n\n' + str(heart_data.columns)))
                    if sub_tab_name == "Display Columns Name":
                        text_area.insert(tk.END, str('\n\n' + str(heart_data.columns)))
                    if sub_tab_name == "Shape of Dataset":
                        text_area.insert(tk.END, str('\n\n' + str(heart_data.shape)))
                    if sub_tab_name == "Describing Data":
                        text_area.insert(tk.END, str('\n\n' + str(heart_data.describe())))
                    if sub_tab_name == "Dataset Information":
                        text_area.insert(tk.END, str('\n\n' + str(heart_data.info())))
                    if sub_tab_name == "Check for Missing Values":
                        text_area.insert(tk.END, str('\n\n' + str(heart_data.isnull().sum())))
                self.frames.extend(sub_frames)
            else:
                label = tk.Label(frame, text=sub_tabs, padx=10, pady=10)
                label.pack()

            button_frame = ttk.Frame(frame)
            button_frame.pack(pady=10)

            back_button = ttk.Button(button_frame, text="Back", command=lambda: self.show_frame(-1))
            back_button.grid(row=0, column=0, padx=5)

            next_button = ttk.Button(button_frame, text="Next", command=lambda: self.show_frame(1))
            next_button.grid(row=0, column=1, padx=5)

        self.show_frame(0)

    def show_frame(self, index):
        current_tab = self.notebook.index("current")
        new_tab = (current_tab + index) % len(self.tabs)
        self.notebook.select(new_tab)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
