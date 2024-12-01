import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# alembic/env.py
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Importiere das MetaData-Objekt von deinen Modellen
from app.models import Base  # Importiere hier deine Base-Instanz aus models.py

config = context.config

# Konfiguriere Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Setze das MetaData-Objekt für Alembic
target_metadata = Base.metadata  # Setze hier das MetaData-Objekt

def run_migrations_offline() -> None:
    """Führe Migrationen im Offline-Modus aus."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Führe Migrationen im Online-Modus aus."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
