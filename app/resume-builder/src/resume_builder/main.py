from pydantic import BaseModel, StrictStr


class Hello(BaseModel):
    message: StrictStr

    def hello(self) -> str:
        return self.message
