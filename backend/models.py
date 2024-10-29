# models.py

from tortoise import Model, fields

class Survey(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "surveys"

class Question(Model):
    id = fields.IntField(pk=True)
    survey: fields.ForeignKeyRelation[Survey] = fields.ForeignKeyField(
        "models.Survey", related_name="questions"
    )
    question_text = fields.CharField(max_length=255)
    question_type = fields.CharField(max_length=50)  # e.g., 'text', 'multiple_choice'

    class Meta:
        table = "questions"

class Response(Model):
    id = fields.IntField(pk=True)
    question: fields.ForeignKeyRelation[Question] = fields.ForeignKeyField(
        "models.Question", related_name="responses"
    )
    answer = fields.TextField()

    class Meta:
        table = "responses"

