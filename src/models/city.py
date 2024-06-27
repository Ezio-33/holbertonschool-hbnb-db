"""
City related functionality
"""

from src.persistence import db
from src.models.country import Country


class City(db.Model):
    """City representation"""
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_code = db.Column(db.String(36), db.ForeignKey('country.code'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    def __init__(self, name: str, country_code: str, **kw) -> None:
        """Dummy init"""
        super().__init__(**kw)

        self.name = name
        self.country_code = country_code

    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<City {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "City":
        """Create a new city"""
        from src.persistence.file import FileRepository

        country = Country.get(data["country_code"])

        if not country:
            raise ValueError("Country not found")

        city = City(**data)

        FileRepository.save(city)

        return city

    @staticmethod
    def update(city_id: str, data: dict) -> "City":
        """Update an existing city"""
        from src.persistence.file import FileRepository

        city = City.get(city_id)

        if not city:
            raise ValueError("City not found")

        for key, value in data.items():
            setattr(city, key, value)

        FileRepository.update(city)

        return city
