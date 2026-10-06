import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os

from main import transcribe_audio, generate_minutes
from utils import save_doc

# -----------------------------
# OUTPUT FOLDER
# -----------------------------
OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# -----------------------------
# PROCESS FILE
# -----------------------------
def process_file(file_path):
    try:
        status_var.set("⏳ AI processing...")

        root.update_idletasks()

        # STEP 1: Transcription
        text = transcribe_audio(file_path)

        # STEP 2: AI Analysis
        data = generate_minutes(text)

        summary = data["summary"]
        decisions = data["decisions"]
        actions = data["actions"]
        agenda = data["agenda"]
        entities = data["entities"]

        # STEP 3: Save DOCX
        name = os.path.splitext(os.path.basename(file_path))[0]
        output_path = save_doc(summary, decisions, actions, agenda, entities, name)

        status_var.set("✅ Ready")

        # STEP 4: Show Output
        output_text.delete("1.0", tk.END)

        output_text.insert(tk.END, "✨ SUMMARY\n", "h")
        output_text.insert(tk.END, summary + "\n\n")

        output_text.insert(tk.END, "📌 AGENDA\n", "h")
        for a in agenda:
            output_text.insert(tk.END, "• " + a + "\n")

        output_text.insert(tk.END, "\n🚀 DECISIONS\n", "h")
        for d in decisions:
            output_text.insert(tk.END, "• " + d + "\n")

        output_text.insert(tk.END, "\n⚡ ACTION ITEMS\n", "h")
        for a in actions:
            output_text.insert(tk.END, "• " + a + "\n")

        output_text.insert(tk.END, "\n👥 ENTITIES\n", "h")
        for e in entities:
            output_text.insert(tk.END, "• " + e + "\n")

        messagebox.showinfo("Success", f"File saved:\n{output_path}")

    except Exception as e:
        status_var.set("❌ Error")
        messagebox.showerror("Error", str(e))


# -----------------------------
# UPLOAD FILE
# -----------------------------
def upload_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.mp3 *.wav *.m4a")]
    )
    if file_path:
        process_file(file_path)


# -----------------------------
# UI SETUP
# -----------------------------
root = tk.Tk()
root.title("AI Meeting Assistant")
root.geometry("900x650")
root.configure(bg="#0f172a")

# ---------------- STYLE ----------------
style = ttk.Style()
style.theme_use("clam")

style.configure("Header.TLabel",
                font=("Segoe UI", 22, "bold"),
                background="#0f172a",
                foreground="#38bdf8")

style.configure("Sub.TLabel",
                font=("Segoe UI", 11),
                background="#0f172a",
                foreground="#94a3b8")

# ---------------- HEADER ----------------
header = ttk.Label(root,
                   text="🎤 Meeting Minutes Generator",
                   style="Header.TLabel")
header.pack(pady=10)

sub = ttk.Label(root,
                text="Upload audio → AI extracts summary, agenda, decisions & tasks",
                style="Sub.TLabel")
sub.pack()

# ---------------- UPLOAD BUTTON ----------------
card = tk.Frame(root, bg="#1e293b")
card.pack(pady=20, padx=30, fill="x")

upload_btn = tk.Button(card,
                       text="📂 Upload Audio File",
                       command=upload_file,
                       bg="#38bdf8",
                       fg="black",
                       font=("Segoe UI", 12, "bold"),
                       relief="flat",
                       padx=20,
                       pady=10)
upload_btn.pack(pady=15)

# ---------------- STATUS ----------------
status_var = tk.StringVar()
status_var.set("Ready")

status = tk.Label(root,
                  textvariable=status_var,
                  bg="#0f172a",
                  fg="#22c55e",
                  font=("Segoe UI", 10, "bold"))
status.pack()

# ---------------- OUTPUT ----------------
output_frame = tk.Frame(root, bg="#1e293b")
output_frame.pack(fill="both", expand=True, padx=20, pady=15)

scroll = tk.Scrollbar(output_frame)
scroll.pack(side="right", fill="y")

output_text = tk.Text(output_frame,
                      wrap="word",
                      yscrollcommand=scroll.set,
                      bg="#0b1220",
                      fg="white",
                      insertbackground="white",
                      font=("Consolas", 11),
                      bd=0,
                      padx=10,
                      pady=10)

output_text.pack(fill="both", expand=True)

scroll.config(command=output_text.yview)

output_text.tag_config("h",
                       font=("Segoe UI", 13, "bold"),
                       foreground="#38bdf8")

root.mainloop()