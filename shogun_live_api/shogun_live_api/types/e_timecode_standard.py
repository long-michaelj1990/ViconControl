
from vicon_core_api import SchemaServices
from enum import Enum


class ETimecodeStandard(Enum):
    """Supported timecode standards.

    Enum Values:
        ETimecodeNone: Invalid value representing no timecode standard
        ETimecode24: 24 fps (FILM)
        ETimecode24Drift: 24 fps but actually running at (24/1.001)fps - hence drifting from wall clock (NTSC compatible FILM)
        ETimecode25: 25 fps (PAL)
        ETimecode30: 30 fps
        ETimecode30Drift: 30 fps but actually running at (30/1.001)fps hence drifting from wall clock (NTSC)
        ETimecode30Drop: 30 fps but actually running at (30/1.001)fps with periodic correction to wall clock (NTSC Drop) [still drifts very slightly!]
    """
    ETimecodeNone = -1
    ETimecode24 = 0
    ETimecode24Drift = 1
    ETimecode25 = 2
    ETimecode30 = 3
    ETimecode30Drift = 4
    ETimecode30Drop = 5




SchemaServices.register_json_schema(ETimecodeStandard,"""{"Type": "Enum32", "TypeName": "ETimecodeStandard", "EnumValues": [["TimecodeNone", -1], ["Timecode24", 0], ["Timecode24Drift",
                                                         1], ["Timecode25", 2], ["Timecode30", 3], ["Timecode30Drift", 4], ["Timecode30Drop", 5]]}""")

