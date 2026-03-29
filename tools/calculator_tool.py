from base_tool import BaseTool

class CalculatorTool(BaseTool):

    def execute(self, expression):
        try:
            return str(eval(expression))
        except Exception as e:
            return f"Error: {str(e)}"

    def get_declaration(self):
        return {
            "name": "calculator",
            "description": "Solve math expressions",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string"}
                },
                "required": ["expression"]
            }
        }