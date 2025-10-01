"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = [] #empty list is created

    while True: #infinite loop until user types "done"
        user_input = input("Enter a number or 'done' to finish: ").strip() #read inputs and removes space with strip function
        if user_input.lower() == 'done':   #always check if user typed "done"
            break 
        try:
            num = float(user_input)     #try to convert input into a number
            numbers.append(num)     #add the number to the list
        except ValueError:      #if conversion fails 
            print("Invalid input. Please enter a number or 'done'.")    #show error message if wrong input

    return numbers  #return final list of numbers 

    
def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:     # if the list is empty, return None
        return None

    analysis = {}       #create an empty dictionnary to store the results

    # Count
    analysis["count"] = len(numbers)        #count how many numbers are in the list

    # Sum
    analysis["sum"] = sum(numbers)      #Sum of all numbers 

    # Average
    analysis["average"] = analysis["sum"] / analysis["count"]       #Average = sum divided by count 

    # Minimum
    analysis["minimum"] = min(numbers)      # find the smallest number

    # Maximum
    analysis["maximum"] = max(numbers)      # find the largest number 

    # Even and Odd counts
    #creating counters for even and odd numbers 
    even_count = 0
    odd_count = 0
    for num in numbers:     #loop trough the list to check each numbers 
        if isinstance(num, int) or num.is_integer():    #check only integers 
            if int(num) % 2 == 0:       # if divisible by 2, it's even and we add into the counters 
                even_count += 1
            else:       #otherwise it is odd 
                odd_count += 1

    analysis["even_count"] = even_count     # let's save into the dictionary
    analysis["odd_count"] = odd_count

    return analysis     #return the dictionary with all analysis results 

def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:    
        return

    print("\nAnalysis Results:") 
    print("-" * 20)

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.

    #Print header 
    print("\nAnalysis Results:")
    print("-" * 20)

    #Print each analysis result in a clear format 
    print(f"Count: {analysis['count']}")
    print(f"Sum: {analysis['sum']}")
    print(f"Average: {analysis['average']:.2f}")
    print(f"Minimum: {analysis['minimum']}")
    print(f"Maximum: {analysis['maximum']}")
    print(f"Even numbers: {analysis['even_count']}")
    print(f"Odd numbers: {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()