from enum import Enum
from symtable import Class

class AllureEpic(str, Enum):
    LMS = "LMS System"
    STUDENT = "Student system"
    ADMINISTRATION = "Administration system"