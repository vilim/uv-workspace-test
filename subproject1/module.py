from pydantic import BaseModel

class T(BaseModel):
    a: str

def dependency():
    return T(a="ABC")