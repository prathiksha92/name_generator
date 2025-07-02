import tkinter as tk
from tkinter import ttk, messagebox
import random

# 🔧 Name Blending Logic (based on mode)
def generate_random_blends(name1, name2, count=5, mode="Couple"):
    blends = []
    for _ in range(count):
        cut1 = random.randint(1, len(name1)-1)
        cut2 = random.randint(1, len(name2)-1)
        blend = name1[:cut1] + name2[cut2:]

        # Mode-based tweaks
        if mode == "Pet":
            blend = blend[:random.randint(3, 5)]  # shorter
        elif mode == "Baby":
            if not blend.endswith(("y", "a", "o")):
                blend += random.choice(["y", "a", "o"])  # softer sound
        blends.append(blend.capitalize())
    return list(set(blends))  # remove duplicates

# 🎯 Generate Button Action
def generate_names():
    name1 = entry1.get().strip()
    name2 = entry2.get().strip()
    mode = mode_var.get()

    if not name1 or not name2:
        messagebox.showerror("Missing Input", "Please enter both names.")
        return

    results = generate_random_blends(name1, name2, count=6, mode=mode)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f"🔮 Mode: {mode}\n\n")
    for r in results:
        output_box.insert(tk.END, f"→ {r}\n")

# 🌈 GUI Setup
root = tk.Tk()
root.title("✨ Creative Name Generator")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="Enter Name 1:").pack(pady=2)
entry1 = tk.Entry(root, width=30)
entry1.pack()

tk.Label(root, text="Enter Name 2:").pack(pady=2)
entry2 = tk.Entry(root, width=30)
entry2.pack()

# Mode Selection
tk.Label(root, text="Select Mode:").pack(pady=5)
mode_var = tk.StringVar(value="Couple")
mode_menu = ttk.Combobox(root, textvariable=mode_var, values=["Couple", "Baby", "Pet"], state="readonly")
mode_menu.pack()

tk.Button(root, text="Generate Names", command=generate_names).pack(pady=10)

output_box = tk.Text(root, height=10, width=40, font=("Consolas", 11))
output_box.pack()

root.mainloop()
