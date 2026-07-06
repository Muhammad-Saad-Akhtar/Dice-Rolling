import tkinter as tk
import random

class DiceGame(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Python Dice Roller Simulation")
        self.geometry("550x450")
        self.configure(bg="#e0e0e0")
        
        # Game State Variables
        self.session_rolls = 0
        self.dice_values = [1, 1] # Default visual state
        
        self.setup_ui()
        self.draw_dice()

    def setup_ui(self):
        # --- Control Panel (Top) ---
        control_frame = tk.Frame(self, bg="#ffffff", pady=15, padx=15, relief=tk.RAISED, bd=1)
        control_frame.pack(fill=tk.X, side=tk.TOP)
        
        # Session Counter
        self.lbl_session = tk.Label(
            control_frame, text="Session Rolls: 0", 
            font=("Helvetica", 14, "bold"), bg="#ffffff", fg="#333333"
        )
        self.lbl_session.pack(side=tk.LEFT, padx=10)
        
        # Dice Count Selector
        tk.Label(
            control_frame, text="Number of Dice:", 
            font=("Helvetica", 12), bg="#ffffff"
        ).pack(side=tk.LEFT, padx=(30, 5))
        
        self.dice_count_var = tk.IntVar(value=2)
        self.spin_dice = tk.Spinbox(
            control_frame, from_=1, to=12, 
            textvariable=self.dice_count_var, width=3, 
            font=("Helvetica", 14), state="readonly"
        )
        self.spin_dice.pack(side=tk.LEFT)
        
        # Roll Action Button
        self.btn_roll = tk.Button(
            control_frame, text="ROLL DICE", 
            font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", 
            activebackground="#45a049", cursor="hand2",
            command=self.roll_dice
        )
        self.btn_roll.pack(side=tk.RIGHT, padx=10)

        # --- Play Area (Bottom) ---
        self.play_area = tk.Frame(self, bg="#e0e0e0")
        self.play_area.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    def roll_dice(self):
        # Update state
        count = self.dice_count_var.get()
        self.dice_values = [random.randint(1, 6) for _ in range(count)]
        self.session_rolls += 1
        
        # Update UI
        self.lbl_session.config(text=f"Session Rolls: {self.session_rolls}")
        self.draw_dice()

    def draw_dice(self):
        # Clear existing dice
        for widget in self.play_area.winfo_children():
            widget.destroy()
            
        # Grid parameters to wrap dice to the next line
        columns = 4 
        
        for index, value in enumerate(self.dice_values):
            row = index // columns
            col = index % columns
            
            # Create a visual die and place it in the grid
            die = self.create_die_canvas(self.play_area, value)
            die.grid(row=row, column=col, padx=15, pady=15)

    def create_die_canvas(self, parent, value):
        # Create a blank canvas for the die
        c = tk.Canvas(parent, width=80, height=80, bg="#e0e0e0", highlightthickness=0)
        
        # Draw the white rounded-looking box with a shadow effect
        c.create_rectangle(7, 7, 77, 77, fill="#cccccc", outline="") # Shadow
        c.create_rectangle(3, 3, 75, 75, fill="white", outline="#333333", width=2) # Main body
        
        # Dot radius
        r = 6 
        
        # Predefined coordinates for dots on an 80x80 canvas
        dot_positions = {
            1: [(39, 39)],
            2: [(20, 20), (58, 58)],
            3: [(20, 20), (39, 39), (58, 58)],
            4: [(20, 20), (20, 58), (58, 20), (58, 58)],
            5: [(20, 20), (20, 58), (39, 39), (58, 20), (58, 58)],
            6: [(20, 20), (20, 39), (20, 58), (58, 20), (58, 39), (58, 58)]
        }
        
        # Draw the dots based on the rolled value
        for (x, y) in dot_positions[value]:
            c.create_oval(x-r, y-r, x+r, y+r, fill="#222222", outline="")
            
        return c

if __name__ == "__main__":
    app = DiceGame()
    app.mainloop()