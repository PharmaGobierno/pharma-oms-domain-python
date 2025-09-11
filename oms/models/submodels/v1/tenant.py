from dataclasses import dataclass
from typing import Literal, Self


@dataclass
class Tenant:
    company: str
    project: str

    version: Literal["1.0.0"] = "1.0.0"

    def encode(self) -> str:
        return "#".join([self.company, self.project])

    @classmethod
    def decode(cls, *, tenant: str) -> Self:
        result = tenant.split("#")
        if len(result) <= 1:
            raise ValueError("Invalid tenant format")
        company, project = result
        return cls(company=company, project=project)
