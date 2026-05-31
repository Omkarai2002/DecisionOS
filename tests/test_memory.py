from app.memory.memory_manager import (
    MemoryManager
)

manager = MemoryManager()

saved = (
    manager.process_message(
        "Learning matters more than stability for me"
    )
)

print(saved)

retrieved = (
    manager.retrieve_memories(
        "career"
    )
)

for memory in retrieved:

    print(memory.content)