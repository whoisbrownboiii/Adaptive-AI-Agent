import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agent import Agent
from memory_manager import MemoryManager
from tool_registry import ToolRegistry

from tools.calculator_tool import CalculatorTool
from tools.time_tool import TimeTool
from tools.translation_tool import TranslationTool
from tools.file_reader_tool import FileReaderTool


def main():
    registry = ToolRegistry()

    registry.register("calculator", CalculatorTool())
    registry.register("time", TimeTool())
    registry.register("translate", TranslationTool())
    registry.register("read_file", FileReaderTool())

    memory = MemoryManager()
    agent = Agent(registry, memory)

    print("AI Assistant Running (type 'exit' to quit)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = agent.run(user_input)
        print("Agent:", response)


if __name__ == "__main__":
    main()