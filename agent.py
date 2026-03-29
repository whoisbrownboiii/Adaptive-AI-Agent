from google import genai
import os

class Agent:

    def __init__(self, registry, memory):
        self.client = genai.Client(
            api_key=os.getenv("AIzaSyDbRgRNAOuZbaKu3UbCha5IuVQYESJ2p4w")
        )

        self.registry = registry
        self.memory = memory

    def run(self, user_input):
        self.memory.add("user", user_input)

        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input
            )

            output = response.text

        except Exception as e:
            output = f"Error: {str(e)}"

        self.memory.add("assistant", output)
        return output


