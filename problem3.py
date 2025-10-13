"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """Get numbers from user until they type 'done'."""
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ").strip()
        if user_input.lower() == "done":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
    return numbers


def analyze_numbers(numbers):
    """
    Analyze a list of numbers and return a dictionary with statistics.
    """
    if not numbers:
        return {}

    analysis = {}
    analysis["count"] = len(numbers)
    analysis["sum"] = sum(numbers)
    analysis["average"] = sum(numbers) / len(numbers)
    analysis["min"] = min(numbers)
    analysis["max"] = max(numbers)

    even_count = 0
    odd_count = 0
    for num in numbers:
        if int(num) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    analysis["even_count"] = even_count
    analysis["odd_count"] = odd_count

    return analysis


def display_analysis(analysis):
    """Display the analysis in a formatted way."""
    if not analysis:
        return
    print("\nAnalysis Results:")
    print("-" * 20)
    print(f"Count      : {analysis['count']}")
    print(f"Sum        : {analysis['sum']}")
    print(f"Average    : {analysis['average']:.2f}")
    print(f"Min        : {analysis['min']}")
    print(f"Max        : {analysis['max']}")
    print(f"Even Count : {analysis['even_count']}")
    print(f"Odd Count  : {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.\n")

    numbers = get_numbers_from_user()
    if not numbers:
        print("No numbers entered!")
        return

    analysis = analyze_numbers(numbers)
    display_analysis(analysis)


if __name__ == "__main__":
    main()
