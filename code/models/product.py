from db import db


class ProductModel(db.Model):
	__tablename__ = 'products'

	code = db.Column(db.Integer, primary_key=True)
	value = db.Column(db.Float(precision=2))


	def __init__(self, code, value):
		self.code = code
		self.value = value

	def json(self):
		return {'code': self.code, 'value': self.value}

	@classmethod
	def find_by_code(cls,code):
		return cls.query.filter_by(code=code).first()

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
