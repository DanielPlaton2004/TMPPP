
from LogisticsDispatch.Infrastructure.Repositories.repository_base import RepositoryBase
from LogisticsDispatch.Domain.Entities.client import Client

class ClientService:
    """SRP: operații pentru clienți."""

    def __init__(self, repo: RepositoryBase[Client]):
        self._repo = repo

    def create(self, client: Client) -> None:
        client.validate()
        self._repo.add(client)

    def list_all(self):
        return self._repo.get_all()

    def get(self, client_id: int):
        return self._repo.get_by_id(client_id)

    def delete(self, client_id: int) -> bool:
        return self._repo.remove(client_id)
