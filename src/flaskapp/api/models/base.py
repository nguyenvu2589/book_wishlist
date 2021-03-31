from flaskapp.extensions import db


class Base(db.Model):
    """
    Base class
    """

    __abstract__ = True

    def __str__(self):
        return f"{self.__class__.__qualname__}: {self.first_name if hasattr(self, 'first_name') else self.title}"

    def __repr__(self):
        return f"<{self.__class__.__qualname__} object name={self.first_name if hasattr(self, 'first_name') else self.title}>"

    def to_dict(self):
        data = {}
        dict_keys = self.columns.keys()
        for k in dict_keys:
            value = getattr(self, k)
            data[k] = value
        return data
