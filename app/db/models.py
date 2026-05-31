import uuid

from sqlalchemy import (
    Column,
    String,
    Float,
    DateTime
)

from sqlalchemy.dialects.postgresql import (
    UUID
)

from sqlalchemy.sql import (
    func
)

from app.db.database import (
    Base
)


class Memory(Base):

    __tablename__ = "memories"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    memory_type = Column(
        String,
        nullable=False
    )

    category = Column(
        String,
        nullable=False
    )

    content = Column(
        String,
        nullable=False
    )

    importance_score = Column(
        Float,
        default=0.5
    )

    created_at = Column(
        DateTime(
            timezone=True
        ),
        server_default=
            func.now()
    )