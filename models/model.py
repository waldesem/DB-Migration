from datetime import datetime

from typing import List
from sqlalchemy import Boolean, create_engine, ForeignKey, String, Text, Date, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from classes import Conclusions


engine = create_engine('sqlite:///persons.db', echo=True)


def default_time():
    return datetime.now()


class Base(DeclarativeBase):
    
    __abstract__ = True


class Category(Base):

    __tablename__ = 'categories'
    
    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    category: Mapped[str] = mapped_column(String(255))
    persons: Mapped[List['Person']] = relationship(back_populates='categories')

    def get_id(self, category):
        with engine.connect() as conn:
            result = conn.execute(
                select(Category.id)
                .filter(Category.category == category)
                ).scalar_one_or_none()
        return result


class Status(Base):
    
    __tablename__ = 'statuses'
    
    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    status: Mapped[str] = mapped_column(String(255))
    persons: Mapped[List['Person']] = relationship(back_populates='statuses')

    def get_id(self, status):
        with engine.connect() as conn:
            result = conn.execute(
                select(Status.id)
                .filter(Status.status == status)
                ).scalar_one_or_none()
        return result
    

class Region(Base):
    """ Create model for regions"""

    __tablename__ = 'regions'
    
    id: Mapped[int] = mapped_column(nullable=True, unique=True, primary_key=True, autoincrement=True)
    region: Mapped[str] = mapped_column(String(255))
    persons : Mapped[List['Person']] = relationship(back_populates='regions')
   
    def get_id(self, region):
        with engine.connect() as conn:
            result = conn.execute(
                select(Region.id)
                .filter(Region.region == region)
                ).scalar_one_or_none()
        return result
    

class Person(Base):
    """ Create model for persons dates"""

    __tablename__ = 'persons'

    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    region_id: Mapped[int] = mapped_column(ForeignKey('regions.id'))
    fullname: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    previous: Mapped[str] = mapped_column(Text, nullable=True)
    birthday: Mapped[datetime] = mapped_column(Date, nullable=False, index=True)
    birthplace: Mapped[str] = mapped_column(Text, nullable=True)
    country: Mapped[str] = mapped_column(String(255), nullable=True)
    ext_country: Mapped[str] = mapped_column(String(255), nullable=True)
    snils: Mapped[str] = mapped_column(String(11), nullable=True)
    inn: Mapped[str] = mapped_column(String(12), nullable=True)
    education: Mapped[str] = mapped_column(Text, nullable=True)
    marital: Mapped[str] = mapped_column(String(255), nullable=True)
    addition: Mapped[str] = mapped_column(Text, nullable=True)
    path: Mapped[str] = mapped_column(Text, nullable=True)
    status_id: Mapped[int] = mapped_column(ForeignKey('statuses.id'))
    created: Mapped[datetime] = mapped_column(Date, default=default_time, nullable=True)
    updated: Mapped[datetime] = mapped_column(Date, onupdate=default_time, nullable=True)
    staffs: Mapped[List['Staff']] = relationship(
        back_populates='persons', cascade="all, delete, delete-orphan"
        )
    documents: Mapped[List['Document']] = relationship(
        back_populates='persons', cascade="all, delete, delete-orphan"
        )
    addresses: Mapped[List['Address']] = relationship(
        back_populates='persons', cascade="all, delete, delete-orphan"
        )
    workplaces: Mapped[List['Workplace']] = relationship(
        back_populates='persons', cascade="all, delete, delete-orphan"
        )
    contacts: Mapped[List['Contact']] = relationship(
        back_populates='persons', cascade="all, delete, delete-orphan"
        )
    checks: Mapped[List['Check']] = relationship(
        back_populates='persons', cascade="all, delete, delete-orphan"
        )
    robots: Mapped[List['Robot']] = relationship(
        back_populates='persons', cascade="all, delete, delete-orphan"
        )
    inquiries: Mapped[List['Inquiry']] = relationship(
        back_populates='persons', cascade="all, delete, delete-orphan"
        )
    affilations: Mapped[List['Affilation']] = relationship(
        back_populates='persons', cascade="all, delete, delete-orphan"
        )
    categories: Mapped['Category'] = relationship(back_populates='persons')
    statuses: Mapped['Status'] = relationship(back_populates='persons')
    regions: Mapped['Region'] = relationship(back_populates='persons')


class Staff(Base):
    """ Create model for staff"""

    __tablename__ = 'staffs'

    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    position: Mapped[str] = mapped_column(Text, nullable=True)
    department: Mapped[str] = mapped_column(Text, nullable=True)
    person_id: Mapped[int] = mapped_column(ForeignKey('persons.id'))
    persons: Mapped[List['Person']] = relationship(back_populates='staffs')


class Document(Base):
    """ Create model for Document dates"""

    __tablename__ = 'documents'

    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    view: Mapped[str] = mapped_column(String(255), nullable=True)
    series: Mapped[str] = mapped_column(String(255), nullable=True)
    number: Mapped[str] = mapped_column(String(255), nullable=True)
    agency: Mapped[str] = mapped_column(Text, nullable=True)
    issue: Mapped[datetime] = mapped_column(Date, nullable=True)
    person_id: Mapped[int] = mapped_column(ForeignKey('persons.id'))
    persons: Mapped[List['Person']] = relationship(back_populates='documents')


class Address(Base): 
    """ Create model for addresses"""

    __tablename__ = 'addresses'

    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    view: Mapped[str] = mapped_column(String(255), nullable=True)
    region: Mapped[str] = mapped_column(String(255), nullable=True)
    address: Mapped[str] = mapped_column(Text, nullable=True)
    person_id: Mapped[int] = mapped_column(ForeignKey('persons.id'))
    persons: Mapped[List['Person']] = relationship(back_populates='addresses')


class Contact(Base):
    """ Create model for contacts"""

    __tablename__ = 'contacts'

    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    view: Mapped[str] = mapped_column(String(255), nullable=True)
    contact: Mapped[str] = mapped_column(String(255), nullable=True)
    person_id: Mapped[int] = mapped_column(ForeignKey('persons.id'))
    persons: Mapped[List['Person']] = relationship(back_populates='contacts')


class Workplace(Base):
    """ Create model for workplaces"""

    __tablename__ = 'workplaces'

    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    start_date: Mapped[datetime] = mapped_column(Date, nullable=True)
    end_date: Mapped[datetime] = mapped_column(Date, nullable=True)
    workplace: Mapped[str] = mapped_column(String(255), nullable=True)
    address: Mapped[str] = mapped_column(Text, nullable=True)
    position: Mapped[str] = mapped_column(Text, nullable=True)
    reason: Mapped[str] = mapped_column(Text, nullable=True)
    person_id: Mapped[int] = mapped_column(ForeignKey('persons.id'))
    persons: Mapped[List['Person']] = relationship(back_populates='workplaces')


class Affilation(Base):
    """ Create model for affilations"""

    __tablename__ = 'affilations'

    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    view: Mapped[str] = mapped_column(String(255), nullable=True)
    name: Mapped[str] = mapped_column(Text, nullable=True)
    inn: Mapped[str] = mapped_column(String(255), nullable=True)
    position: Mapped[str] = mapped_column(Text, nullable=True)
    deadline: Mapped[datetime] = mapped_column(Date, default=default_time, nullable=True)
    person_id: Mapped[int] = mapped_column(ForeignKey('persons.id'))
    persons: Mapped[List['Person']] = relationship(back_populates='affilations')


class Check(Base):
    """ Create model for persons checks"""

    __tablename__ = 'checks'

    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    workplace: Mapped[str] = mapped_column(Text, nullable=True)
    document: Mapped[str] = mapped_column(Text, nullable=True)
    inn: Mapped[str] = mapped_column(Text, nullable=True)
    debt: Mapped[str] = mapped_column(Text, nullable=True)
    bankruptcy: Mapped[str] = mapped_column(Text, nullable=True)
    bki: Mapped[str] = mapped_column(Text, nullable=True)
    courts: Mapped[str] = mapped_column(Text, nullable=True)
    affilation: Mapped[str] = mapped_column(Text, nullable=True)
    terrorist: Mapped[str] = mapped_column(Text, nullable=True)
    mvd: Mapped[str] = mapped_column(Text, nullable=True)
    internet: Mapped[str] = mapped_column(Text, nullable=True)
    cronos: Mapped[str] = mapped_column(Text, nullable=True)
    cros: Mapped[str] = mapped_column(Text, nullable=True)
    addition: Mapped[str] = mapped_column(Text, nullable=True)
    pfo: Mapped[bool] = mapped_column(Boolean, nullable=True)
    comments: Mapped[str] = mapped_column(Text, nullable=True)
    conclusion: Mapped[int] = mapped_column(ForeignKey('conclusions.id'))
    officer: Mapped[str] = mapped_column(String(255), nullable=True)
    deadline: Mapped[datetime] = mapped_column(Date, default=default_time, 
                         onupdate=default_time)
    person_id: Mapped[int] = mapped_column(ForeignKey('persons.id'))
    persons: Mapped[List['Person']] = relationship(back_populates='checks')
    conclusions: Mapped['Conclusion'] = relationship(back_populates='checks')


class Conclusion(Base):
    
    __tablename__ = 'conclusions'
    
    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    conclusion: Mapped[str] = mapped_column(String(255))
    checks: Mapped[List['Check']] = relationship(back_populates='conclusions')

    def get_id(self, conclusion):
        with engine.connect() as conn:
            mapped = {
                'согласовано': Conclusions.agreed.value,
                'с комментарием': Conclusions.with_comment.value,
                'отказ': Conclusions.denied.value
            }
            result = conn.execute(
            select(Conclusion)
            .filter(Conclusion.conclusion == mapped.get(conclusion.lower(), Conclusions.canceled.value))
            ).scalar_one_or_none().id
            return result


class Robot(Base):
    """ Create model for robots"""

    __tablename__ = 'robots'

    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    employee: Mapped[str] = mapped_column(Text, nullable=True)
    inn: Mapped[str] = mapped_column(Text, nullable=True)
    bankruptcy: Mapped[str] = mapped_column(Text, nullable=True)
    bki: Mapped[str] = mapped_column(Text, nullable=True)
    courts: Mapped[str] = mapped_column(Text, nullable=True)
    terrorist: Mapped[str] = mapped_column(Text, nullable=True)
    mvd: Mapped[str] = mapped_column(Text, nullable=True)
    deadline: Mapped[datetime] = mapped_column(Date, default=default_time, nullable=True)
    person_id: Mapped[int] = mapped_column(ForeignKey('persons.id'))
    persons: Mapped[List['Person']] = relationship(back_populates='robots')


class Inquiry(Base):
    """ Create model for persons inquiries"""

    __tablename__ = 'inquiries'

    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    info: Mapped[str] = mapped_column(Text, nullable=True)
    initiator: Mapped[str] = mapped_column(String(255), nullable=True)
    source: Mapped[str] = mapped_column(String(255), nullable=True)
    officer: Mapped[str] = mapped_column(String(255), nullable=True)
    deadline: Mapped[datetime] = mapped_column(Date, default=default_time, nullable=True)
    person_id: Mapped[int] = mapped_column(ForeignKey('persons.id'))
    persons: Mapped[List['Person']] = relationship(back_populates='inquiries')


class Connect(Base):
    """ Create model for persons connects"""
    
    __tablename__ = 'connects'

    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)
    company: Mapped[str] = mapped_column(String(255), nullable=True)
    city: Mapped[str] = mapped_column(String(255), nullable=True)
    fullname: Mapped[str] = mapped_column(String(255), nullable=True)
    phone: Mapped[str] = mapped_column(String(255), nullable=True)
    adding: Mapped[str] = mapped_column(String(255), nullable=True)
    mobile: Mapped[str] = mapped_column(String(255), nullable=True)
    mail: Mapped[str] = mapped_column(String(255), nullable=True)
    comment: Mapped[str] = mapped_column(Text, nullable=True)
    data: Mapped[datetime] = mapped_column(Date, default=default_time, onupdate=default_time, nullable=True)

Base.metadata.create_all(engine)