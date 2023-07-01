from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, Date, Time
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Master(Base):
    __tablename__ = 'masters'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    full_name: Mapped[str] = mapped_column(String(50))
    appointments: Mapped[List["Appointment"]] = relationship(back_populates="master")


class Client(Base):
    __tablename__ = 'clients'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    full_name: Mapped[str] = mapped_column(String(50))
    appointments: Mapped[List["Appointment"]] = relationship(back_populates="client")


class AvailableSlot(Base):
    __tablename__ = 'available_slots'

    id: Mapped[int] = mapped_column(primary_key=True)
    master_id: Mapped[int] = mapped_column(ForeignKey('masters.id'))
    date: Mapped[Date] = mapped_column(Date)
    time: Mapped[Time] = mapped_column(Time)
    master: Mapped["Master"] = relationship("Master", back_populates="available_dates")


class Appointment(Base):
    __tablename__ = 'appointments'

    id: Mapped[int] = mapped_column(primary_key=True)
    master_id: Mapped[int] = mapped_column(ForeignKey('masters.id'))
    client_id: Mapped[int] = mapped_column(ForeignKey('clients.id'))
    date: Mapped[Date] = mapped_column(Date)
    time: Mapped[Time] = mapped_column(Time)
    master: Mapped["Master"] = relationship("Master", back_populates="appointments")
    client: Mapped["Client"] = relationship("Client", back_populates="appointments")
