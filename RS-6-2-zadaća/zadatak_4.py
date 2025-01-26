from pydantic import BaseModel, Field
from typing import Tuple
from datetime import datetime

# Definicija modela za trenutnu sliku s CCTV kamere
class CCTV_frame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate: Tuple[float, float] = Field(default=(0.0, 0.0))

# Primjer korištenja
if __name__ == "__main__":

    frame_podaci = {
        "id": 1,
        "vrijeme_snimanja": datetime.now(),
        "koordinate": (45.815, 15.981)  
    }

    # Validacija podatka o trenutnoj slici
    frame = CCTV_frame(**frame_podaci)
    print("CCTV Frame validiran:", frame)

    # Primjer validacije 
    frame_podaci_bez_koordinata = {
        "id": 2,
        "vrijeme_snimanja": datetime.now()
    }

    frame_bez_koordinata = CCTV_frame(**frame_podaci_bez_koordinata)
    print("CCTV Frame sa zadanim koordinatama validiran:", frame_bez_koordinata)
