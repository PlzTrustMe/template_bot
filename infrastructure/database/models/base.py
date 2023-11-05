import datetime
import os

from peewee import SqliteDatabase, Model, DateTimeField

path_to_file: str = os.path.join(os.path.dirname(os.getcwd()), 'db.db')

db = SqliteDatabase(path_to_file)


def make_table_name(model_class):
    model_name: str = model_class.__name__

    return model_name.lower() + 's'


class BaseModel(Model):
    class Meta:
        database = db
        table_function = make_table_name


class TimestampMixin(Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        super(TimestampMixin, self).save(*args, **kwargs)
