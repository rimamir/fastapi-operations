## Pet project with FastApi

### Install poetry

```shell
pip install poetry
```

### Install the project dependencies

```shell
cd src && poetry install
```

### Spawn a shell within the virtual environment

```shell
cd src && poetry install
```

### Create database

```shell
from workshop.database import engine
from worshop.tables import Base

Base.metadata.create_all(engine)
```

