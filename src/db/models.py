from typing import List
from sqlalchemy import ForeignKey, Date, Time, BigInteger
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class AbstractUser(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String(64), nullable=True)  # user can exist without username
    full_name: Mapped[str] = mapped_column(String(128))


class Master(AbstractUser):
    __tablename__ = 'masters'

    appointments: Mapped[List["Appointment"]] = relationship(back_populates="master")
    available_dates: Mapped[List["AvailableSlot"]] = relationship("AvailableSlot", back_populates="master")


class Client(AbstractUser):
    __tablename__ = 'clients'

    appointments: Mapped[List["Appointment"]] = relationship(back_populates="client")


class AvailableSlot(Base):
    __tablename__ = 'available_slots'

    master_id: Mapped[int] = mapped_column(ForeignKey('masters.id'))
    date: Mapped[Date] = mapped_column(Date)
    time: Mapped[Time] = mapped_column(Time)
    master: Mapped["Master"] = relationship("Master", back_populates="available_dates")


class Appointment(Base):
    __tablename__ = 'appointments'

    master_id: Mapped[int] = mapped_column(ForeignKey('masters.id'))
    client_id: Mapped[int] = mapped_column(ForeignKey('clients.id'))
    date: Mapped[Date] = mapped_column(Date)
    time: Mapped[Time] = mapped_column(Time)
    master: Mapped["Master"] = relationship("Master", back_populates="appointments")
    client: Mapped["Client"] = relationship("Client", back_populates="appointments")
