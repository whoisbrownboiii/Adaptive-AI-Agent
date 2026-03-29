from base_tool import BaseTool

class TranslationTool(BaseTool):

    def execute(self, text):
        return text[::-1]

    def get_declaration(self):
        return {
            "name": "translate",
            "description": "Translate text",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"]
            }
        }