from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

# AI Study Assistant Agent setup
study_assistant_agent = Agent(
    name="AI Study Assistant",
    role="Provide detailed explanations for specific topics and subjects.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Provide a detailed explanation and examples for the specified topic."],
    show_tools_calls=True,
    markdown=True
)

# Function to get explanation for a given topic
def get_explanation(topic: str):
    try:
        # Request the AI assistant to explain the topic
        explanation_response = study_assistant_agent.print_response(
            f"Explain the concept of {topic} in detail, including any examples and applications, types etc. als use a diagram if possible.",
            stream=True
        )
        return explanation_response
    except Exception as e:
        print(f"Error: {e}")
        return None


# Example usage: Explanation of a topic from a subject
topic = "what do you mean by neural networks"

response = get_explanation(topic)

if response:
    print(response)
