# apan5310_f22_demo

Brief demo for APAN 5310

## Virtual environment setup

[This](https://realpython.com/python-virtual-environments-a-primer/) is a good guide on virtual environments.

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
pip install --upgrade setuptools wheel pip
```

```
pip install -r requirements.txt
```

## Alembic setup

-   add the connection string to the alembic.ini file
-   edit the env.py file to add the models to the target_metadata variable

```
alembic init alembic
alembic revision --autogenerate -m "create tables"
alembic upgrade head
```
