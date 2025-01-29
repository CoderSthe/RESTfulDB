from db_setup import db
from enum_choice import HardDriveType


class Computer(db.Model):
    __tablename__ = "Computer"
    id = db.Column(db.Integer, primary_key=True)
    hard_drive_type = db.Column(db.Enum(HardDriveType), nullable=False)
    processor = db.Column(db.String(80), nullable=False)
    ram_amount = db.Column(db.Integer, nullable=False)
    maximum_ram = db.Column(db.Integer, nullable=False)
    form_factor = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return (
            f"Computer(hd type: {self.hard_drive_type.value}, "
            f"processor: {self.processor}, "
            f"ram amount: {self.ram_amount}, "
            f"maximum ram: {self.maximum_ram}, "
            f"form factor: {self.form_factor})"
        )
