from phi.agent import Agent
from phi.model.groq import Groq

# Simple art & design-related functions for debugging, without external calls
def get_art_inspiration(style, theme):
    # Mocked response for testing purposes
    return f"Here are some art inspirations based on {style} and {theme}:\n- Abstract painting with bold colors\n- Minimalist design with geometric shapes\n- Nature-inspired artwork featuring calming blues and greens"

def get_design_tips(style):
    # Mocked design tips
    return f"Here are some design tips for {style}:\n- Use clean lines and simple color schemes for modern design.\n- Incorporate organic shapes and earth tones for bohemian style.\n- Add metallic accents for an elegant, luxurious feel."

def get_color_palette(style):
    # Mocked color palette suggestion
    return f"For {style}, a suitable color palette might be:\n- Navy Blue, Charcoal Grey, and White for a professional, minimalist look.\n- Terracotta, Sage Green, and Sand for an earthy bohemian vibe."

def get_art_materials(art_type):
    # Mocked art materials suggestion
    return f"For {art_type} artwork, consider using:\n- Acrylic paints for vibrant colors\n- Watercolors for a soft, delicate effect\n- Charcoal for bold lines and shading"

# Personalized Art & Design Assistant setup with simplified tools
art_design_agent = Agent(
    name="Personalized Art & Design Assistant",
    role="Help users create personalized art, provide design inspiration, and suggest creative ideas",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[get_art_inspiration],  # Using only the get_art_inspiration tool for testing
    instructions=[
        "Provide art inspiration based on the user’s preferred style and theme."
    ],
    show_tools_calls=True,
    markdown=True
)

# Test the agent with a simple prompt and one tool
def get_art_design_inspiration(style, theme):
    try:
        # Ask the agent for art inspiration based on style and theme
        inspiration = art_design_agent.print_response(
            f"Give me art inspiration for a {style} style with a {theme} theme.",
            stream=True
        )
        return inspiration
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example query
style = "Modern"
theme = "Nature"
art_inspiration = get_art_design_inspiration(style, theme)

if art_inspiration:
    print(art_inspiration)
