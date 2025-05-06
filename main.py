from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

class SearchApp:
    def __init__(self, master):
        self.master = master
        master.title("SMART FARMING SYSTEM")

        # main window size
        master.geometry("1920x1080")

        # main background image
        self.background_image = Image.open("main_background.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(master, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)
        
        # Create a frame for login elements
        login_frame = tk.Frame(master)
        login_frame.place(relx=0.5, rely=0.532, anchor=tk.CENTER)

        # Create a frame to hold the search elements
        search_frame = tk.Frame(master)
        search_frame.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        self.label_district = tk.Label(search_frame, text="জেলা:", font=("Arial", 11, "bold"), bg="#3D8C40", fg="white")
        self.label_district.grid(row=0, column=0, padx=10, pady=10)

        # Use Combobox for District
        self.entry_district = ttk.Combobox(search_frame, values=["Mymensingh", "Other Districts"], font=("Arial", 10, "bold"), width=30)
        self.entry_district.grid(row=0, column=1, padx=10, pady=10)
        self.entry_district.set("Mymensingh")  # Set default value

        self.label_sub_district = tk.Label(search_frame, text="উপজেলা:", font=("Arial", 11, "bold"), bg="#3D8C40", fg="white")
        self.label_sub_district.grid(row=1, column=0, padx=10, pady=10)

        # Use Combobox for Sub-district
        self.entry_sub_district = ttk.Combobox(search_frame, values=["Mymensingh Sadar", "Trishal", "Bhaluka", 
                                                                     "Haluaghat", "Muktagacha", "Dhobaura", 
                                                                     "Fulbaria", "Gaffargaon", "Gauripur", "Ishwarganj",
                                                                     "Nandail", "Phulpur", "Tarakanda"], font=("Arial", 10, "bold"), width=30)
        self.entry_sub_district.grid(row=1, column=1, padx=10, pady=10)
        self.entry_sub_district.set("Mymensingh Sadar")  # Set default value

        self.search_button = tk.Button(search_frame, text="অনুসন্ধান", command=self.search, font=("Arial", 10, "bold"), bg="#3D8C40", fg="white")
        self.search_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(search_frame, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Add the label at the top middle of the window
        l = tk.Label(master, text="বি.দ্রঃ ইহা শুধুমাত্র ময়মনসিংহ জেলার জন্য প্রযোজ্য।", font=("Arial", 11), bg="white", fg="red", width= 38)
        l.place(relx=0.5, rely=0, anchor=tk.N)
        
        # Dictionary to store text file paths for each sub-district for "Info"
        self.info_files = {
            "Mymensingh Sadar": "Mymensingh Sadar_text.txt",
            "Trishal": "Trishal_text.txt",
            "Bhaluka": "Bhaluka_text.txt",
            "Haluaghat": "Haluaghat_text.txt",
            "Muktagacha": "Muktagacha_text.txt",
            "Dhobaura": "Dhobaura_text.txt",
            "Fulbaria": "Fulbaria_text.txt",
            "Gaffargaon": "Gaffargaon_text.txt",
            "Gauripur": "Gauripur_text.txt",
            "Ishwarganj": "Ishwarganj_text.txt",
            "Nandail": "Nandail_text.txt",
            "Phulpur": "Phulpur_text.txt",
            "Tarakanda": "Tarakanda_text.txt",
        }
        
        # Dictionary to store text file paths for each sub-district for "Result"
        self.result_files = {
            "Mymensingh Sadar": "Mymensingh Sadar_result.txt",
            "Trishal": "Trishal_result.txt",
            "Bhaluka": "Bhaluka_result.txt",
            "Haluaghat": "Haluaghat_result.txt",
            "Muktagacha": "Muktagacha_result.txt",
            "Dhobaura": "Dhobaura_result.txt",
            "Fulbaria": "Fulbaria_result.txt",
            "Gaffargaon": "Gaffargaon_result.txt",
            "Gauripur": "Gauripur_result.txt",
            "Ishwarganj": "Ishwarganj_result.txt",
            "Nandail": "Nandail_result.txt",
            "Phulpur": "Phulpur_result.txt",
            "Tarakanda": "Tarakanda_result.txt",
        }
        
        # Instance variables to store image references
        self.info_background_photo = None
        self.result_background_photo = None
        
        # Add the "Admin Panel" button
        admin_panel_button = tk.Button(master, text="Admin Panel", command=self.open_admin_panel, font=("Arial", 10, "bold"), bg="white", fg="black", width=15, height=1)
        admin_panel_button.place(relx=0.5, rely=0.87, anchor=tk.S)
        
        # Button to close the main window
        self.close_main_button = tk.Button(master, text="বন্ধ করুন", command=master.destroy, font=("Arial", 10, "bold"), bg="#c0dccc", fg="black", width=10, height=1)
        self.close_main_button.place(relx=0.5, rely=0.96, anchor=tk.S)
        
         # Button to open the Feedback window
        feedback_button = tk.Button(master, text="মতামত ও যোগাযোগ", command=self.feedback, font=("Arial", 10, "bold"), bg="#d2e6db", fg="black", width=17, height=1)
        feedback_button.place(relx=0.5, rely=0.915, anchor=tk.S)
        
    def feedback(self):
        # Create a new window for feedback
        feedback_window = tk.Toplevel(self.master)
        feedback_window.title("মতামত ও যোগাযোগ")

        # Set window size for the Feedback window
        feedback_window.geometry("450x550")
        
        # Create a frame for feedback elements
        feedback_frame = tk.Frame(feedback_window)
        feedback_frame.pack(pady=20)
    
        # Create labels for Name, Email, and Subject
        name_label = tk.Label(feedback_frame, text="নাম:", font=("Arial", 10, "bold"), bg="#c0dccc", fg="black")
        email_label = tk.Label(feedback_frame, text="ইমেইল:", font=("Arial", 10, "bold"), bg="#c0dccc", fg="black")
        subject_label = tk.Label(feedback_frame, text="বিষয়:", font=("Arial", 10, "bold"), bg="#c0dccc", fg="black")
    
        name_label.grid(row=0, column=0, pady=10)
        email_label.grid(row=1, column=0, pady=10)
        subject_label.grid(row=2, column=0, pady=10)
    
        # Create Entry widgets for Name, Email, and Subject
        name_entry = ttk.Entry(feedback_frame, font=("Arial", 10, "bold"), width=30)
        email_entry = ttk.Entry(feedback_frame, font=("Arial", 10, "bold"), width=30)
        subject_entry = ttk.Entry(feedback_frame, font=("Arial", 10, "bold"), width=30)
    
        name_entry.grid(row=0, column=1, pady=10)
        email_entry.grid(row=1, column=1, pady=10)
        subject_entry.grid(row=2, column=1, pady=10)
        
        # Create a label for instructions
        instructions_label = tk.Label(feedback_window, text="আপনার মতামত:", font=("Arial", 10, "bold"), bg="#c0dccc", fg="black")
        instructions_label.pack(pady=10)

        # Create a text widget for user input
        feedback_text = tk.Text(feedback_window, wrap=tk.WORD, width=50, height=10)
        feedback_text.pack(padx=20, pady=20)

        # Function to handle submission of feedback
        def submit_feedback():
            user_name = name_entry.get()
            user_email = email_entry.get()
            user_subject = subject_entry.get()
            user_feedback = feedback_text.get("1.0", tk.END)
            
            # Save the feedback to a text file
            feedback_filename = "user_feedback.txt"
            with open(feedback_filename, "a", encoding="utf-8") as feedback_file:
                feedback_file.write(f"নাম: {user_name}\nইমেইল: {user_email}\nবিষয়: {user_subject}\n\nমতামত: {user_feedback}")

            messagebox.showinfo("Feedback Submitted", "আপনার মতামত গৃহীত হয়েছে। ধন্যবাদ!")

        # Create a button to submit feedback
        submit_button = tk.Button(feedback_window, text="জমা দিন", command=submit_feedback, font=("Arial", 10, "bold"), bg="#3D8C40", fg="white")
        submit_button.pack(pady=10)

        # Button to close the Feedback window
        close_feedback_button = tk.Button(feedback_window, text="বন্ধ করুন", command=feedback_window.destroy, font=("Arial", 10, "bold"), bg="#d2dfd3", fg="black")
        close_feedback_button.pack()
        
    def open_admin_panel(self):
        # Create a frame for login elements
        admin_panel_frame = tk.Frame(self.master)
        admin_panel_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.label_admin_username = tk.Label(admin_panel_frame, text="এডমিন নাম:", font=("Arial", 11, "bold"), bg="#3D8C40", fg="white")
        self.label_admin_username.grid(row=0, column=0, padx=10, pady=10)

        self.entry_admin_username = ttk.Entry(admin_panel_frame, font=("Arial", 10, "bold"), width=30)
        self.entry_admin_username.grid(row=0, column=1, padx=10, pady=10)

        self.label_admin_password = tk.Label(admin_panel_frame, text="পাসওয়ার্ড:", font=("Arial", 11, "bold"), bg="#3D8C40", fg="white")
        self.label_admin_password.grid(row=1, column=0, padx=10, pady=10)

        self.entry_admin_password = ttk.Entry(admin_panel_frame, show="*", font=("Arial", 10, "bold"), width=30)
        self.entry_admin_password.grid(row=1, column=1, padx=10, pady=10)

        self.login_admin_button = tk.Button(admin_panel_frame, text="লগ ইন", command=self.authenticate_admin, font=("Arial", 10, "bold"), bg="white", fg="#3D8C40")
        self.login_admin_button.grid(row=2, column=0, columnspan=2, pady=10)

    def authenticate_admin(self):
        admin_username = self.entry_admin_username.get()
        admin_password = self.entry_admin_password.get()

        # Add your authentication logic here
        valid_admin_username = "admin"
        valid_admin_password = "admin123"

        if admin_username == valid_admin_username and admin_password == valid_admin_password:
            # Check if the user is an admin and display the "Update Information" button accordingly
            self.update_button = tk.Button(self.master, text="Update Information", command=self.update_file, font=("Arial", 10, "bold"), bg="#d2dfd3", fg="black")
            self.update_button.place(relx=0.66, rely=0.7, anchor=tk.CENTER)
        else:
            messagebox.showwarning("Error", "এডমিন নাম ও পাসওয়ার্ড সঠিকভাবে দিন।")

    def update_file(self):
        
        # Open a file dialog for administrators to choose a file
        file_path = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))

        # Check if a file is selected
        if file_path:
            try:
                # Open the selected file for updating
                with open(file_path, "r", encoding="utf-8") as file:
                    current_content = file.read()

                # Create a new window for updating file content
                update_window = tk.Toplevel(self.master)
                update_window.title("Update Information")

                # Set window size for the Update window
                update_window.geometry("600x500")

                # Create a text widget for user input
                update_text = tk.Text(update_window, wrap=tk.WORD, width=60, height=20)
                update_text.insert(tk.END, current_content)
                update_text.pack(padx=20, pady=20)

                # Function to handle submission of updated content
                def submit_update():
                    updated_content = update_text.get("1.0", tk.END)

                    # Save the updated content back to the selected file
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(updated_content)

                    messagebox.showinfo("Update Successful", "File updated successfully!")

                    # Close the Update window after successful update
                    update_window.destroy()

                # Create a button to submit the updated content
                submit_update_button = tk.Button(update_window, text="জমা দিন", command=submit_update, font=("Arial", 10, "bold"), bg="#3D8C40", fg="white")
                submit_update_button.pack(pady=10)
                
                # Button to close the Feedback window
                close_update_button = tk.Button(update_window, text="বন্ধ করুন", command=update_window.destroy, font=("Arial", 10, "bold"), bg="#d2dfd3", fg="black")
                close_update_button.pack()

            except Exception as e:
                messagebox.showerror("Error", f"Error updating file: {str(e)}")
        else:
            messagebox.showwarning("File Update", "No file selected.")
    
    def search(self):
        district = self.entry_district.get()
        sub_district = self.entry_sub_district.get()

        valid_district = "Mymensingh"
        valid_sub_districts = [
            "Mymensingh Sadar", "Trishal", "Bhaluka", "Haluaghat", "Muktagacha",
            "Dhobaura", "Fulbaria", "Gaffargaon", "Gauripur", "Ishwarganj",
            "Nandail", "Phulpur", "Tarakanda"
        ]

        if district == valid_district and sub_district in valid_sub_districts:
            result_text = f"আপনি {sub_district} উপজেলা নির্বাচন করেছেন।"
            self.result_label.config(text=result_text, font=("Arial", 10, "bold"), bg="#d2dfd3", fg="black")
            
            i_button = tk.Button(self.master, text=f"{sub_district} উপজেলার কৃষি তথ্য অথবা উপযুক্ত শস্য বিন্যাস সম্পর্কে জানতে নিচের বাটন দুটি ক্লিক করুন।", 
                                 command=self.show_info, font=("Arial", 10, "bold"), bg="#3D8C40", fg="white", width=86, height=1)
            
            # Create "Info" and "Result" buttons
            info_button = tk.Button(self.master, text="কৃষি তথ্য", command=self.show_info, font=("Arial", 11, "bold"),  bg="#d2dfd3", fg="black")
            result_button = tk.Button(self.master, text="উপযুক্ত শস্য বিন্যাস", command=self.show_result, font=("Arial", 11, "bold"),  bg="#d2dfd3", fg="black")

            i_button.place(relx=0.5, rely=0.30, anchor=tk.CENTER)

            # Place the buttons below the Sub-district name
            info_button.place(relx=0.45, rely=0.36, anchor=tk.CENTER)
            result_button.place(relx=0.53, rely=0.36, anchor=tk.CENTER)
            
        else:
            messagebox.showerror("Error", "দুঃখিত! আপনার জেলা অথবা উপজেলা সঠিকভাবে দিন।")
    
    def show_info(self):
        sub_district = self.entry_sub_district.get()
        
        # Retrieve the file path from the dictionary
        info_file_path = self.info_files.get(sub_district)

        if info_file_path:
            try:
                with open(info_file_path, "r", encoding="utf-8") as file:
                    info_text = file.read()

                    # Create a new window for displaying info
                    info_window = tk.Toplevel(self.master)
                    info_window.title(f"{sub_district} উপজেলার কৃষি তথ্য")
                    
                    # Set window size for the Info window
                    info_window.geometry("1920x1080")  # Adjust the size as needed

                    # Load background image for Info window
                    self.info_background_image = Image.open("info_background.png")
                    self.info_background_photo = ImageTk.PhotoImage(self.info_background_image)

                    # Add background image to the Info window
                    info_background_label = tk.Label(info_window, image=self.info_background_photo)
                    info_background_label.place(relwidth=1, relheight=1)

                    # Display the text content in a label
                    info_label = tk.Label(info_window, text=info_text, font=("Arial", 12), justify=LEFT)
                    info_label.pack(padx=20, pady=20)

            except FileNotFoundError:
                messagebox.showerror("Error", f"দুঃখিত! {sub_district} উপজেলার কোন কৃষি তথ্য পাওয়া যায় নি।")
        else:
            messagebox.showerror("Error", f"দুঃখিত! {sub_district} উপজেলার কোন কৃষি তথ্য পাওয়া যায় নি।")
        
        # Button to close the Info window
        close_info_button = tk.Button(info_window, text="বন্ধ করুন", command=info_window.destroy, font=("Arial", 10, "bold"), bg="#119011", fg="white", width=10, height=1)
        close_info_button.place(relx=0.5, rely=0.99, anchor=tk.S)

    def show_result(self):
        sub_district = self.entry_sub_district.get()
        
        # Retrieve the file path from the dictionary for "Result"
        result_file_path = self.result_files.get(sub_district)

        if result_file_path:
            try:
                with open(result_file_path, "r", encoding="utf-8") as file:
                    result_text = file.read()

                    # Create a new window for displaying result
                    result_window = tk.Toplevel(self.master)
                    result_window.title(f"{sub_district} উপজেলার উপযুক্ত শস্য বিন্যাস")
        
                    # Set window size for the Result window
                    result_window.geometry("1920x1080")

                    # Load background image for Result window
                    self.result_background_image = Image.open("result_background.png")
                    self.result_background_photo = ImageTk.PhotoImage(self.result_background_image)

                    # Add background image to the Result window
                    result_background_label = tk.Label(result_window, image=self.result_background_photo)
                    result_background_label.place(relwidth=1, relheight=1)

                    # Display the text content in a label
                    result_label = tk.Label(result_window, text=result_text, font=("Arial", 12), justify=LEFT)
                    result_label.pack(padx=20, pady=20)

            except FileNotFoundError:
                messagebox.showerror("Error", f"দুঃখিত! {sub_district} উপজেলার কোন উপযুক্ত শস্য বিন্যাস পাওয়া যায় নি।")
        else:
            messagebox.showerror("Error", f"দুঃখিত! {sub_district} উপজেলার কোন উপযুক্ত শস্য বিন্যাস পাওয়া যায় নি।")
        
        # Button to close the Result window
        close_result_button = tk.Button(result_window, text="বন্ধ করুন", command=result_window.destroy, font=("Arial", 10, "bold"), bg="#119011", fg="white", width=10, height=1)
        close_result_button.place(relx=0.5, rely=0.99, anchor=tk.S)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = SearchApp(root)
    root.mainloop()