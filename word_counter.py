import string
import os

# Optional: A list of common "stop words" to ignore
STOP_WORDS = {"the", "and", "is", "in", "to", "of", "a", "it", "was", "for", "on", "can"}

def clean_text(text):
    """
    Cleans the input text by converting to lowercase and removing punctuation.
    """
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    return text

def count_words(file_path):
    """
    Reads a text file, counts word frequencies, and returns the results.
    """
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            return None, "Error: File not found. Please check the path."
        
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
        # Handle empty files gracefully
        if not text.strip():
            return None, "Error: The file is empty."
        
        # Clean the text
        cleaned_text = clean_text(text)
        
        # Split into a list of words
        words = cleaned_text.split()
        
        # Count word frequencies using a dictionary
        word_counts = {}
        for word in words:
            # Optionally, filter out stop words and short words
            if word not in STOP_WORDS and len(word) >= 3:
                word_counts[word] = word_counts.get(word, 0) + 1
        
        return word_counts, None
    
    except Exception as e:
        return None, f"An unexpected error occurred: {e}"

def display_results(word_counts, total_words, top_n=10):
    """
    Displays the summary statistics and the top N most common words.
    """
    print(f"\nTotal number of words: {total_words}")
    print(f"Total number of unique words: {len(word_counts)}\n")

    # Check if top_n is valid
    if top_n <= 0 or top_n > len(word_counts):
        print("Invalid number for top words. Displaying top 10 instead.")
        top_n = 10
    
    print(f"Top {top_n} most common words:")
    
    # Sort words by frequency in descending order
    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    
    # Display the top N words
    for i, (word, count) in enumerate(sorted_words[:top_n], 1):
        print(f"{i}. {word}: {count}")

def main():
    """
    Main function to run the application.
    """
    print("--- WORD FREQUENCY COUNTER ---")
    
    while True:
        file_path = input("Enter the path to a text file (or 'exit' to quit): ").strip()
        
        if file_path.lower() == 'exit':
            break
            
        word_counts, error = count_words(file_path)
        
        if error:
            print(error)
            continue
            
        # Calculate the total number of words
        total_words = sum(word_counts.values())
        
        try:
            # Ask the user for how many top words to display
            top_n_input = input("How many top words to display? (Press Enter for default 10): ").strip()
            top_n = int(top_n_input) if top_n_input else 10
            display_results(word_counts, total_words, top_n)
        except ValueError:
            print("Invalid input. Displaying top 10 words.")
            display_results(word_counts, total_words)

if __name__ == "__main__":
    main()