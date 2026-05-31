from app.memory.memory_extractor import (
    MemoryExtractor
)

extractor = (
    MemoryExtractor()
)

result = (
    extractor.extract_memory(
        "Learning matters more than stability for me"
    )
)

print(
    result.model_dump()
)