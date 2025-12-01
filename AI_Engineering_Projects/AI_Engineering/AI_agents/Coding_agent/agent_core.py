import os
import streamlit as st
from langchain_tavily import TavilySearch
from langchain_core.messages import HumanMessage, ToolMessage
from langchain.chat_models import init_chat_model
from langchain.globals import set_verbose
set_verbose(True)

# Import the custom tool definition from core/tools.py
from core.tools import python_repl


# --- Check st.secrets first for the keys
google_api_key = st.secrets.get("GOOGLE_API_KEY")
tavily_api_key = st.secrets.get("TAVILY_API_KEY")

# For compatibility, also set them into os.environ if found in secrets
if not google_api_key:
    os.environ["GOOGLE_API_KEY"] = google_api_key
if not tavily_api_key:
    os.environ["TAVILY_API_KEY"] = tavily_api_key

# Variables will be defined here only if keys are present
model = None
model_with_tools = None
search_tool = None
tool_map = {}

if google_api_key and tavily_api_key:
    # --- Model Initialization ---
    model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

    # --- Instantiate the Tavily Search Tool ---
    search_tool = TavilySearch(max_results=5)

    # --- Bind the tools to the model ---
    # We include the imported custom tool and the search tool
    model_with_tools = model.bind_tools([python_repl, search_tool])

    # This map is essential for executing the tools in the agent loop
    tool_map = {
        "python_repl": python_repl,
        "tavily_search_results": search_tool,
        "tavily_search": search_tool,
    }

    st.sidebar.success("✅ Agent Tools Ready!")
else:
    st.error("""⚠️ **API Keys Missing**
        
        This agent requires both **Gemini API Key** and **Tavily API Key**.
        
        Please ensure you have created the file `.streamlit/secrets.toml` 
        in your project root and populated it with both keys.
        """)
    st.stop()

# --- Agent Response Function ---
# This function orchestrates the agent's actions
def get_agent_response(query):
    # This check ensures the function is callable without crashing if keys are missing
    if not model_with_tools:
        st.error("Cannot run query: Agent is not initialized. Please enter API keys.")
        return

    # Invoke the model with the user query
    response_from_model = model_with_tools.invoke([{"role": "user", "content": query}])

    st.write("---")
    st.write("Agent Response:")

    # Handle the case where the model does NOT call a tool.
    if not response_from_model.tool_calls:
        if isinstance(response_from_model.content, list):
            for part in response_from_model.content:
                st.write(part)
        else:
            st.write(response_from_model.content)

    # Handle the case where the model DOES call a tool.
    else:
        # Note: This is simplified to handle only the first tool call
        tool_call = response_from_model.tool_calls[0]
        st.write(f"⚙️ **Tool Used:** {tool_call['name']}")

        try:
            # Execute the tool and get the result
            tool_result = tool_map[tool_call['name']].invoke(tool_call['args'])
        except KeyError:
            st.write(f"Sorry, I'm having trouble using the tool {tool_call['name']}.")
            return

        # Sends the tool's result back to the model for a final, natural language response
        final_response = model_with_tools.invoke(
            [
                # We send the original user query, the model's tool call, and the tool's result
                {"role": "user", "content": query},
                response_from_model,
                ToolMessage(content=str(tool_result), tool_call_id=tool_call['id'])
            ]
        )

        # Display the final, polished response
        if isinstance(final_response.content, list):
            for part in final_response.content:
                st.write(part)
        else:
            st.write(final_response.content)

# --- Final Check ---
if not google_api_key or not tavily_api_key:
    # Display an error if the script ends without a fully initialized agent
    st.error("Please enter both the Gemini and Tavily API keys in the sidebar to activate the Agent.")
    st.stop()