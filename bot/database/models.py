from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric, Boolean, Text, TIMESTAMP, BigInteger, JSON, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

Base = declarative_base()

class UserRole(enum.Enum):
    ADMIN = "admin"
    COMMITTEE = "committee"
    TEACHER = "teacher"
    PARENT = "parent"

class TransactionType(enum.Enum):
    TOPUP = "topup"
    EXPENSE = "expense"
    REFUND = "refund"
    ADJUSTMENT = "adjustment"

class PaymentStatus(enum.Enum):
    WAITING_ADMIN = "waiting_admin"
    NEED_INFO = "need_info"
    CONFIRMED = "confirmed"
    REJECTED = "rejected"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=True)
    role = Column(Enum(UserRole), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(20), nullable=True)
    password_hash = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    grade_level = Column(Integer, nullable=False)
    class_teacher_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    teacher = relationship("User")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    internal_id = Column(String(20), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=True)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    metadata = Column(JSON, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    class_obj = relationship("Class")

class StudentContact(Base):
    __tablename__ = "student_contacts"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    relation = Column(String(20), nullable=False)  # mother, father, grandmother, etc
    is_primary = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    
    student = relationship("Student")
    user = relationship("User")

class Wallet(Base):
    __tablename__ = "wallets"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), unique=True, nullable=False)
    balance_cents = Column(BigInteger, default=0, nullable=False)
    currency = Column(String(3), default="UAH", nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    student = relationship("Student")

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    kind = Column(String(10), nullable=False)  # income or expense
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    
    creator = relationship("User")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    amount_cents = Column(BigInteger, nullable=False)
    currency = Column(String(3), default="UAH", nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    performed_by_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(Text, nullable=True)
    external_ref = Column(String(128), nullable=True)  # payment_id or bank reference
    status = Column(String(20), default="confirmed")
    receipt_path = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    
    wallet = relationship("Wallet")
    category = relationship("Category")
    performed_by = relationship("User")

class PendingPayment(Base):
    __tablename__ = "pending_payments"
    id = Column(Integer, primary_key=True)
    payment_id = Column(String(64), unique=True, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # parent who made request
    amount_cents = Column(BigInteger, nullable=False)
    currency = Column(String(3), default="UAH", nullable=False)
    uploaded_receipt = Column(String(255), nullable=True)
    note = Column(Text, nullable=True)
    status = Column(Enum(PaymentStatus), default=PaymentStatus.WAITING_ADMIN)
    admin_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    admin_comment = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    student = relationship("Student")
    user = relationship("User", foreign_keys=[user_id])
    admin = relationship("User", foreign_keys=[admin_id])

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    sent_at = Column(TIMESTAMP, nullable=True)
    read_at = Column(TIMESTAMP, nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    
    user = relationship("User")

class AdminAuditLog(Base):
    __tablename__ = "admins_audit_log"
    id = Column(Integer, primary_key=True)
    admin_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    action = Column(String(100), nullable=False)
    target_type = Column(String(50), nullable=True)  # user, student, class, etc
    target_id = Column(Integer, nullable=True)
    payload = Column(JSON, nullable=True)  # before/after data
    ip_address = Column(String(45), nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    
    admin = relationship("User")

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    amount_cents = Column(BigInteger, nullable=False)
    currency = Column(String(3), default="UAH", nullable=False)
    payment_details = Column(Text, nullable=True)  # bank details, instructions
    deadline = Column(TIMESTAMP, nullable=True)
    is_active = Column(Boolean, default=True)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=True)  # null for all classes
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    category = relationship("Category")
    class_obj = relationship("Class")
    creator = relationship("User")
