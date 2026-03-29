from base_tool import BaseTool

class FileReaderTool(BaseTool):

    def execute(self, filename):
        try:
            with open(filename, "r") as f:
                return f.read()
        except Exception as e:
            return f"Error: {str(e)}"

    def get_declaration(self):
        return {
            "name": "read_file",
            "description": "Read a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {"type": "string"}
                },
                "required": ["filename"]
            }
        }