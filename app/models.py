from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base  # Импортируем Base из database.py


class Show(Base):
    __tablename__ = 'shows'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True, index=True)
    description = Column(String, nullable=True)
    source_type = Column(String)
    source_id = Column(String)
    videos = relationship("Video", back_populates="show")

    def __repr__(self):
        return f"<Show(id={self.id}, title={self.title})>"


class Video(Base):
    __tablename__ = 'videos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True, index=True)
    description = Column(String, nullable=True)
    url = Column(String)
    source_type = Column(String)
    source_id = Column(String)
    show_id = Column(Integer, ForeignKey('shows.id'))
    show = relationship("Show", back_populates="videos")

    def __repr__(self):
        return f"<Video(id={self.id}, title={self.title}, url={self.url})>"