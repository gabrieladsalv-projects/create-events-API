from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy import func

class CheckIns(Base):
    __tablename__ = "check_ins"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    attendeeId = Column(String, ForeignKey("attendees.id"), nullable=False)

    def __repr__(self):
        return f"CheckIns [attendeeId={self.attendeeId}]"