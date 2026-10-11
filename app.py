import tkinter as tk
import random
import network_manager

def create():
    # Fetch existing words from cloud first so we don't overwrite other people's additions
    current_cloud_words = network_manager.get_cloud_words()
    
    new_words = entry.get().split()
    # Combine old list and new words
    updated_list = current_cloud_words + new_words
    
    # Send the collective JSON array back to the database
    network_manager.save_cloud_words(updated_list)
    
    print("Updated Global List:", updated_list)
    entry.delete(0, tk.END)

def search():
    current_cloud_words = network_manager.get_cloud_words()
    if current_cloud_words:
        # Pick a random word from the shared online list
        word_chosen = random.choice(current_cloud_words)
        # Push the chosen word up so everyone see it change
        network_manager.set_current_chosen_word(word_chosen)
    else:
        wordLabel.config(text="No words available in the cloud database!")

# Track locally to prevent refreshing UI if nothing altered online
last_displayed_word = None

def update_loop():
    """Background loop checking for changes across clients every second."""
    global last_displayed_word
    
    remote_chosen_word = network_manager.get_current_chosen_word()
    
    if remote_chosen_word and remote_chosen_word != last_displayed_word:
        last_displayed_word = remote_chosen_word
        wordLabel.config(text=f'The chosen word is: {remote_chosen_word}')
        
    # Re-run loop in 1000 milliseconds
    window.after(1000, update_loop)

# Window Setup
window = tk.Tk()
window.geometry('500x500')
window.title("Cloud Synchronized Word Picker")

entry = tk.Entry(master=window)
entry.config(font=('Ink Free', 50))
entry.config(bg='black')
entry.config(fg='#1aff05')
entry.pack(pady=10)
 
searchButton = tk.Button(master=window, text='Random Word', command=search)
searchButton.pack(pady=5)

createButton = tk.Button(master=window, text='Create', command=create)
createButton.pack(pady=5)

wordLabel = tk.Label(master=window, text='Enter a word', font=('Arial', 14))
wordLabel.pack(pady=20)

# Start real-time syncing listener
update_loop()

window.mainloop()
