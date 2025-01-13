from phi.agent import Agent
from phi.model.groq import Groq
import random

# Define the Normal Joke and Dark Joke lists
normal_jokes = [
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don’t eggs tell jokes? Because they’d crack each other up!",
    "What do you get when you cross a snowman and a vampire? Frostbite!"
]

dark_jokes = [
    "Why don’t graveyards have 4G? Because they’re full of dead zones.",
    "I have a joke about a broken pencil... but it’s pointless.",
    "I’d tell you a joke about an elevator, but it’s an uplifting experience.",
    "The man who invented autocorrect died today. Restaurant in peace.",
    "I used to play piano by ear, but now I use my hands."
]

# Define the Joke Agents (Normal and Dark Joke Agents)
normal_joke_agent = Agent(
    name="Normal Joke Agent",
    role="Generate normal jokes",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[],
    instructions=["Return a random normal joke from the list"],
    show_tools_calls=True,
    markdown=True
)

dark_joke_agent = Agent(
    name="Dark Joke Agent",
    role="Generate dark jokes",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[],
    instructions=["Return a random dark joke from the list"],
    show_tools_calls=True,
    markdown=True
)

# Function to get a random joke
def get_random_joke(joke_type="normal"):
    if joke_type == "normal":
        return random.choice(normal_jokes)
    elif joke_type == "dark":
        return random.choice(dark_jokes)
    else:
        return "Invalid joke type. Please choose 'normal' or 'dark'."

# Define the main agent that interacts with users
multi_joke_agent = Agent(
    team=[normal_joke_agent, dark_joke_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Provide a random joke based on the user's selection"],
    show_tool_calls=True,
    markdown=True
)

# Main function to prompt for user input and get a joke
def get_joke(joke_type="normal"):
    # Generate the joke using the correct agent
    joke = get_random_joke(joke_type)
    return joke

# User input
joke_type = input("Do you want a 'normal' joke or a 'dark' joke? ").strip().lower()

# Get the joke based on input
joke = get_joke(joke_type)

# Output the joke
print("\nHere's your joke: ")
print(joke)
