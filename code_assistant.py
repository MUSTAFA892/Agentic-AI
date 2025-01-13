from phi.agent import Agent
from phi.model.groq import Groq

# Function to generate a full response based on the question
def generate_code_response(question: str):
    return f"""
    ### Answer for the question: "{question}"

    #### Code Example:
    ```python
    # Here goes the Python code based on the question
    # Example: Binary Search Implementation

    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid  # Target found
            elif arr[mid] < target:
                left = mid + 1  # Ignore the left half
            else:
                right = mid - 1  # Ignore the right half
        return -1  # Target not found
    ```

    #### Explanation:
    - This algorithm is called **Binary Search**, and it's used to search for a target element in a **sorted** array.
    - It works by repeatedly dividing the search interval in half. If the value of the target is less than the value in the middle of the interval, the algorithm narrows the interval to the lower half. Otherwise, it narrows it to the upper half.
    - The process continues until the value is found or the interval is empty.

    #### Time Complexity:
    - **Best case**: O(1) - The target is found in the middle of the array.
    - **Worst case**: O(log n) - The interval is halved at each step, so the number of operations grows logarithmically with the size of the array.

    #### Best Practices:
    - Ensure the array is **sorted** before using Binary Search.
    - Binary Search is much faster than linear search (O(n)) for large datasets due to its O(log n) time complexity.
    - Use Binary Search on **sorted arrays or lists** to optimize search time.

    #### Notes:
    - For small datasets, the difference in speed between Binary Search and Linear Search might not be significant.
    - You can also implement Binary Search recursively, but the iterative version above is often more efficient in terms of space.

    """
    

# General-purpose Code Assistant setup
code_assistant = Agent(
    name="AI Advanced Code Assistant",
    role="Help users with coding problems, explanations, and best practices.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[generate_code_response],  # Using the generate_code_response function
    instructions=[
        "Provide code for the given programming problem or algorithm, explain it step by step, and mention time and space complexity.",
    ],
    show_tools_calls=True,
    markdown=True
)

# Function to get response for a code-related query
def get_code_assistance(query):
    try:
        # Request the assistant for the code and explanation
        full_response = code_assistant.print_response(
            f"Give me the code and explanation for: {query}",
            stream=True
        )
        return full_response
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test the assistant with an example query
query = "How do I implement binary search?"
response = get_code_assistance(query)

if response:
    print(response)
