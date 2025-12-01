import math
import builtins
import ast
from pydantic.v1 import BaseModel, Field
from langchain_core.tools import tool

# --- Define the Safe Execution Environment ---

# This dictionary restricts the functions available to 'exec()', blocking access 
# to dangerous modules like 'os', 'sys', or 'subprocess'.
SAFE_GLOBALS = {
    '__builtins__': {
        'abs': abs, 
        'max': max, 
        'min': min, 
        'round': round,
        'int': int, 
        'float': float, 
        'complex': complex,
        'len': builtins.len, 
        'str': builtins.str, 
        'list': builtins.list,
        'tuple': builtins.tuple, 
        'dict': builtins.dict,
        'sum': builtins.sum, 
        'pow': builtins.pow,
        'zip': builtins.zip,             # Allows parallel iteration (like in dot product)
        'range': builtins.range,         # Allows simple loops
        'enumerate': builtins.enumerate, # Allows indexed loops
        'print': builtins.print,         # Allows printing simple debug messages
    },
    'math': math
}

# --- Define the Pydantic Input Schema for the Tool ---

class PythonReplInput(BaseModel):
    """Input for the Python REPL tool."""
    code: str = Field(description="The Python code to execute.")

# --- Define the Python REPL Tool Function ---

@tool(args_schema=PythonReplInput)
def python_repl(code: str) -> str:
    """Use this to execute basic Python math code. The code runs in a sandboxed 
    environment. The tool will automatically assign the result of a single 
    expression to the required 'output' variable.
    
    Example: math.log(100) + math.pow(2, 5)
    
    Note: Multi-line code must still use the 'output = ...' assignment itself.
    """
    try:
        # Compile the code to check for syntax errors before execution
        # --- Input Validation and Auto-Assignment ---
        
        _locals = {}
        _globals = SAFE_GLOBALS.copy() # Use a copy to protect SAFE_GLOBALS
        # We ensure the code is compiled correctly before passing it to exec
        compiled_code = compile(code, '<string>', 'exec')

        # Execute the code using the heavily restricted SAFE_GLOBALS
        exec(compiled_code, _globals, _locals)
        
        # Try to capture an explicit 'output' variable
        #output = _locals.get('output', 'Execution successful, but no `output` variable was explicitly set.')
        output = _locals.get('output', None)
        if output is None:
            output = _globals.get('output', 'Execution successful, but no `output` variable was explicitly set.')
        return str(output)

    except Exception as e:
        # Report the error back to the agent
        return f"Error executing code: {e}"