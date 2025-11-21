#
#  Import LIBRARIES
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import func

from app.core.data.source.local.base import Base

#  Import FILES
#  _______________________


class CountryModel(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    country_code = Column(String, unique=True, nullable=False)
    currency_code = Column(String, nullables=False)

    created_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
