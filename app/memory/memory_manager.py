from sqlalchemy.orm import Session

from app.db.database import (
    SessionLocal
)

from app.db.models import (
    Memory
)

from app.schemas.memory import (
    MemoryCreate
)

from app.memory.memory_extractor import (
    MemoryExtractor
)

class MemoryManager:

    def __init__(self):

        self.db: Session = (
            SessionLocal()
        )

        self.extractor = (
            MemoryExtractor()
        )

    def save_memory(
        self,
        memory: MemoryCreate
    ):

        db_memory = Memory(
            memory_type=
                memory.memory_type,

            category=
                memory.category,

            content=
                memory.content,

            importance_score=
                memory.importance_score
        )

        self.db.add(
            db_memory
        )

        self.db.commit()

        self.db.refresh(
            db_memory
        )

        return db_memory

    def retrieve_memories(
        self,
        category: str,
        limit: int = 5
    ):

        memories = (
            self.db.query(
                Memory
            )
            .filter(
                Memory.category
                == category
            )
            .order_by(
                Memory.importance_score
                .desc()
            )
            .limit(limit)
            .all()
        )

        return memories
    def process_message(
        self,
        message: str
    ):

        extracted = (
            self.extractor
            .extract_memory(
                message
            )
        )

        if not extracted.should_store:

            return None

        memory = MemoryCreate(
            memory_type=
                extracted.memory_type,

            category=
                extracted.category,

            content=
                extracted.content,

            importance_score=
                extracted
                .importance_score
        )

        existing_memory = (
        self.find_similar_memory(
            content=
                extracted.content,

            category=
                extracted.category
                )
            )

        if existing_memory:

            print(
                "Memory reinforced"
            )

            return (
                self.reinforce_memory(
                    existing_memory
                )
            )

        print(
            "New memory stored"
        )

        return self.save_memory(
            memory
        )
    
    def find_similar_memory(
        self,
        content: str,
        category: str
    ):
        memory = (
            self.db.query(
                Memory
            )
            .filter(
                Memory.content
                == content,

                Memory.category
                == category
            )
            .first()
        )

        return memory
    
    def reinforce_memory(
        self,
        memory: Memory
    ):

        memory.importance_score = min(
            memory.importance_score
            + 0.1,
            1.0
        )

        self.db.commit()

        self.db.refresh(
            memory
        )

        return memory