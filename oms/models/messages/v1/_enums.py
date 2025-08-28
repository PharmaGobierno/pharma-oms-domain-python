from enum import Enum


class EntityActionTypes(str, Enum):
    CREATED = "CREATED"
    UPDATED = "UPDATED"
    DELETED = "DELETED"


class RemissionMigrationOrigins(str, Enum):
    FIRESTORE = "FIRESTORE"
    BLUEYONDER = "BLUEYONDER"


class RemissionOrigins(str, Enum):
    FIRESTORE = "FIRESTORE"
    BLUEYONDER = "BLUEYONDER"
