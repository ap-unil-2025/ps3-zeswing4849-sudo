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
    numbers = []

    while True:
        user_input = input("Enter a number or 'done' to finish: ").strip()
        if user_input.lower() == 'done':
            break
        try:
            num = float(user_input)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    return numbers

    
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
    if not numbers:
        return None

    analysis = {}

    # Count
    analysis["count"] = len(numbers)

    # Sum
    analysis["sum"] = sum(numbers)

    # Average
    analysis["average"] = analysis["sum"] / analysis["count"]

    # Minimum
    analysis["minimum"] = min(numbers)

    # Maximum
    analysis["maximum"] = max(numbers)

    # Even and Odd counts
    even_count = 0
    odd_count = 0
    for num in numbers:
        if isinstance(num, int) or num.is_integer(): 
            if int(num) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    analysis["even_count"] = even_count
    analysis["odd_count"] = odd_count

    return analysis

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
        print("\nAnalysis Results:")
    print("-" * 20)
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