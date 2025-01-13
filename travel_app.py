from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

# Simple travel-related functions as tools
def get_travel_tips(destination):
    # Placeholder: Use DuckDuckGo to search for travel tips for the given destination
    search_result = DuckDuckGo().search(f"travel tips for {destination}")
    return search_result

def get_weather(destination):
    # Placeholder: Use DuckDuckGo to search weather for the destination
    search_result = DuckDuckGo().search(f"current weather in {destination}")
    return search_result

def get_flight_info(origin, destination):
    # Placeholder: Use DuckDuckGo to search flight info
    search_result = DuckDuckGo().search(f"flights from {origin} to {destination}")
    return search_result

def get_hotel_info(destination):
    # Placeholder: Use DuckDuckGo to search hotels for the destination
    search_result = DuckDuckGo().search(f"hotels in {destination}")
    return search_result

# Travel Agent setup with simplified tools
travel_agent = Agent(
    name="AI Travel Assistant",
    role="Help users plan their trips by providing destination suggestions, flights, hotels, and activities",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[get_travel_tips],  # Start by using just one tool to simplify
    instructions=[
        "Provide travel tips for the user’s destination."
    ],
    show_tools_calls=True,
    markdown=True
)

# Test the agent with a simple prompt and one tool
def get_travel_plan(destination):
    try:
        # Ask the agent for travel tips for the destination
        travel_plan = travel_agent.print_response(
            f"Give me travel tips for {destination}.",
            stream=True
        )
        return travel_plan
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example query
destination = "Mumbai"
travel_plan = get_travel_plan(destination)

if travel_plan:
    print(travel_plan)
