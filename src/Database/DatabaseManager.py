import psycopg2
from psycopg2 import pool
from fastapi import Depends
from typing import Any, Dict, List, Optional, Generator

class Database:
    def __init__(
        self,
        username: str,
        password: str,
        dbname: str,
        host: str = "localhost",
        port: int = 5432,
        ssl_mode: Optional[str] = None,
        ssl_cert: Optional[str] = None,
        ssl_key: Optional[str] = None,
        ssl_root_cert: Optional[str] = None,
        min_size: int = 1,
        max_size: int = 10,
    ):
        ssl_options = ""
        if ssl_mode!="":
            ssl_options = f"sslmode={ssl_mode} "
            if ssl_cert:
                ssl_options += f"sslcert={ssl_cert} "
            if ssl_key:
                ssl_options += f"sslkey={ssl_key} "
            if ssl_root_cert:
                ssl_options += f"sslrootcert={ssl_root_cert} "

        self.dsn = (
            f"dbname={dbname} user={username} password={password} host={host} port={port} {ssl_options}".strip()
        )
        self.min_size = min_size
        self.max_size = max_size
        self.pool: Optional[pool.SimpleConnectionPool] = None

    def connect(self):
        """Establish a connection pool to the database."""
        self.pool = psycopg2.pool.SimpleConnectionPool(
            minconn=self.min_size, maxconn=self.max_size, dsn=self.dsn
        )

    def disconnect(self):
        """Close the database connection pool."""
        if self.pool:
            self.pool.closeall()

    def get_connection(self) -> psycopg2.extensions.connection:
        """Get a connection from the pool."""
        if not self.pool:
            raise ValueError("Database connection is not established.")
        return self.pool.getconn()

    def release_connection(self, connection: psycopg2.extensions.connection):
        """Release a connection back to the pool."""
        if self.pool:
            self.pool.putconn(connection)

    def fetch(self, query: str, *args) -> List[Dict[str, Any]]:
        """Fetch multiple rows from the database."""
        connection = self.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, args)
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                return [dict(zip(columns, row)) for row in rows]
        finally:
            self.release_connection(connection)

    def execute(self, query: str, *args):
        """Execute a query (INSERT/UPDATE/DELETE)."""
        connection = self.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, args)
                connection.commit()
                if cursor.pgresult_ptr is not None:
                    return cursor.fetchall()
                return None
        finally:
            self.release_connection(connection)