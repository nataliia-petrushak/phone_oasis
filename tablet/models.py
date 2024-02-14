from device.models import Device


class Tablet(Device):
    def __str__(self) -> str:
        return self.name
