from datetime import datetime
from uuid import UUID
from typing import Optional

import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as pg
from sqlmodel import Field, Index, SQLModel


class FlaggedMessage(SQLModel, table=True):
    __tablename__ = "flagged_message"
    __table_args__ = (Index("ix_message_emoji__user_id__message_id", "user_id", "message_id", unique=False),)

    message_id: Optional[UUID] = Field(
        sa_column=sa.Column(
            pg.UUID(as_uuid=True), sa.ForeignKey("message.id", ondelete="CASCADE"), nullable=False, primary_key=True
        )
    )
    processed: bool = Field(nullable=False, index=True)
    created_date: Optional[datetime] = Field(
        sa_column=sa.Column(
            sa.DateTime(timezone=True), nullable=False, server_default=sa.func.current_timestamp(), index=True
        )
    )
