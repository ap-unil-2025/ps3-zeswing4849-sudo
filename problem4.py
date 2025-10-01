"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""

def create_sample_file(filename="sample.txt"):
    """
    Create a sample text file for testing.

    Args:
        filename (str): Name of the file to create
    """
    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects."""
    
# Open the file in write mode ('w') and write the content
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    """
    Count total words in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        int: Total number of words
    """
    # TODO: Open file and count words
    # Hint: Use split() to separate words
    try:
        with open(filename, 'r') as f:      #open file in read mode
            text = f.read()                 #read entire content 
            words = text.split()            #split text by whitespace = list
            return len(words)               #return the numbers of words 
    except FileNotFoundError:               #handle missing file 
            print(f"File {filename} not found.")
            return 0


def count_lines(filename):
    """
    Count total lines in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        int: Total number of lines
    """
    # TODO: Open file and count lines
    try:
        with open(filename, 'r') as f:      #open file in read mode
            lines = f.readlines()           #read all lines into a list
            return len(lines)               # return number of lines 
    except FileNotFoundError:               # handle missing file 
        print(f"File {filename} not found.")
        return 0


def count_characters(filename, include_spaces=True):
    """
    Count characters in the file.

    Args:
        filename (str): Name of the file to analyze
        include_spaces (bool): Whether to include spaces in count

    Returns:
        int: Total number of characters
    """
    # TODO: Open file and count characters
    # If include_spaces is False, don't count spaces
    try:
        with open(filename, 'r') as f:      # open file in read mode
            text = f.read()                 # read entire content
            if include_spaces:              # count all characters (also spaces)
                return len(text)
            else:                           #removes spaces, newlines, tabs 
                return len(text.replace(" ", "").replace("\n", "").replace("\t", ""))  
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return 0

def find_longest_word(filename):
    """
    Find and return the longest word in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        str: The longest word found
    """
    try:
        with open(filename, 'r') as f:          # open file
            text = f.read()                     # read all content
            words = text.split()                # split text into words

            # Initialize longest word
            longest_word = ""

            # Loop through each word
            for word in words:
                # Compare lengths, keep the longest
                if len(word) > len(longest_word):
                    longest_word = word

            return longest_word  # return the longest word

    except FileNotFoundError:                   # handle missing file
        print(f"File {filename} not found.")
        return None


def word_frequency(filename):
    """
    Return a dictionary of word frequencies.
    Convert words to lowercase and remove punctuation.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        dict: Dictionary with words as keys and frequencies as values
    """
    import string

    frequency = {}  # empty dictionary to store word counts

    try:
        with open(filename, 'r') as f:               # open the file
            text = f.read()                          # read entire content
            text = text.lower()                      # convert text to lowercase

            # Remove punctuation from the text
            translator = str.maketrans('', '', string.punctuation)
            text = text.translate(translator)

            words = text.split()                     # split into list of words

            # Count frequency of each word
            for word in words:
                if word in frequency:                # if word already exists, add 1
                    frequency[word] += 1
                else:                                # if first time, set count to 1
                    frequency[word] = 1

    except FileNotFoundError:                        # handle missing file
        print(f"File {filename} not found.")
        return {}

    return frequency  # return dictionary of word frequencies


def analyze_file(filename):
    """
    Perform complete analysis of the file.

    Args:
        filename (str): Name of the file to analyze
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        # Display all analyses
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        # Display top 5 most common words
        print("\nTop 5 most common words:")
        freq = word_frequency(filename)

        # Sort by frequency and get top 5
        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the file analyzer."""
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "=" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()