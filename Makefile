run:
	uvicorn app.main:app --reload

migration:
	cd app/ && alembic revision --autogenerate -m $(MESSAGE)

alembic-upgrade:
	cd app/ && alembic upgrade head
