"""TcEx Framework Module"""

# standard library
from pathlib import PosixPath

# third-party
from pydantic.v1 import BaseModel, validator

__all__ = ['TcexJsonModel']


# pylint: disable=no-self-argument
class PackageModel(BaseModel):
    """Model definition for tcex_json.package"""

    app_name: str
    app_version: str | None
    excludes: list
    output_dir: str = 'target'

    @validator('excludes')
    def sorted(cls, v):
        """Change value for excludes field."""
        # the requirements.txt file is required for App Builder
        v = [e for e in v if e != 'requirements.txt']
        return list(sorted(set(v)))

    class Config:
        """DataModel Config"""

        validate_assignment = True


class TcexJsonModel(BaseModel):
    """Model definition for tcex.json configuration file"""

    package: PackageModel
    template_name: str | None
    template_repo_hash: str | None = None
    template_type: str | None

    class Config:
        """DataModel Config"""

        json_encoders = {PosixPath: lambda v: v.original_value}
        use_enum_values = True
        validate_assignment = True
