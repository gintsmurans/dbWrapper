from typing import Any

from MySQLdb.cursors import DictCursor as MySqlDictCursor

from db_wrapper import DBWrapper

from .connector import MySQL


class DBWrapperMysql(DBWrapper):
    """Base model for all RV4 models"""

    # Override db instance
    db: MySQL

    ######################
    ### Helper methods ###
    ######################

    def logQuery(
        self,
        cursor: MySqlDictCursor,
        query: Any,
        params: tuple[Any, ...],
    ) -> None:
        """
        Logs the given query and parameters.

        Args:
            query (Any): The query to log.
            params (tuple[Any, ...]): The parameters to log.
        """
        queryString = cursor.mogrify(query, params)
        self.logger.debug(f"Query: {queryString}")

    #####################
    ### Query methods ###
    #####################

    def limitQuery(self, offset: int = 0, limit: int = 100) -> str:
        return f"LIMIT {offset},{limit}"

    async def createCursor(self, emptyDataClass: Any | None = None) -> MySqlDictCursor:
        return self.db.connection.cursor(MySqlDictCursor)
