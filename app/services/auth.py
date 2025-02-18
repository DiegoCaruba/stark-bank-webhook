import starkbank
from ..config import environment, project_id, private_key

user = starkbank.Project(
    environment=environment,
    id=project_id,
    private_key=open(private_key).read(),
)

starkbank.user = user
