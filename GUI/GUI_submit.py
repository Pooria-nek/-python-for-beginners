import tkinter as tk

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    print(f"Name: {name}\nEmail: {email}")

# Create the main root
root = tk.Tk()
root.title("My Application")

# Create a label widget and add it to the root
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)

# Create an entry widget for the name field and add it to the root
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Create a label widget for the email field and add it to the root
email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0)

# Create an entry widget for the email field and add it to the root
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

# Create a button to submit the form and add it to the root
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=2, column=1)

# Display the main root
root.mainloop()
