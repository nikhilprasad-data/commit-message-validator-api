from pydantic import BaseModel, ConfigDict


class CommentSchema(BaseModel):

     commit_message: str

class CommentSchemaResponse(CommentSchema):

     model_config = ConfigDict(from_attributes= True)