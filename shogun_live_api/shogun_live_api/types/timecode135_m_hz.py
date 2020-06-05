
from vicon_core_api import SchemaServices
from e_timecode_standard import ETimecodeStandard


class Timecode135MHz(object):
    """This class represents a timecode value.

    The class also carries some additional non standard members that allow it to unambiguously describe a point in time at a
    finer granularity than standard timecode and outside of the standard 24 hours permitted by timecode. The granularity of
    representable time is given by the class' tick rate in Hz

    Members:
        standard < ETimecodeStandard >: The timecode standard being represented.
        hours < int >: Standard timecode part Hours.
        minutes < int >: Minutes.
        seconds < int >: Seconds.
        frames < int >: Frames.
        user_bits < int >: Extra bits in timecode format. Generally ignore these when comparing timecodes.
        days < int >: Days - allows us to do non-lossy conversion to and from timecode of times that are not in the range of 0-24 hours
        tick_remainder < int >: Tick Remainder in TRateInHz - allows us non-lossy conversion to and from timecode of times that do not fall exactly on a
            timecode boundary.
        sub_frame_period < int >: This is an optional field provided to facilitate backwards compatibility with older timecode representations that have the
            notion of SubFramesPerFrame. It supplies the frame period (in ticks) of the underlying data stream that is carrying this
            timecode signal. As such, a sub frame count can be calculated as the tick remainder divided by the sub frame period. A value
            of zero indicates that the sub frame period is not specified.
    """
    def __init__(self):
        """Initialiser for Timecode135MHz."""
        self.standard = ETimecodeStandard.ETimecodeNone
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.frames = 0
        self.user_bits = 0
        self.days = 0
        self.tick_remainder = 0
        self.sub_frame_period = 0

    def __str__(self):
        """Provide JSON string representation for Timecode135MHz."""
        return SchemaServices.write(self)




SchemaServices.register_json_schema(Timecode135MHz,"""{"Type": "NamedTuple", "TypeName": "Timecode135MHz", "SubSchemas": [["Standard", {"Type": "Ref", "TypeName": "ETimecodeStandard"}],
                                                      ["Hours", {"Type": "UInt8"}], ["Minutes", {"Type": "UInt8"}], ["Seconds", {"Type": "UInt8"}], ["Frames", {"Type": "UInt8"}],
                                                      ["UserBits", {"Type": "UInt32"}], ["Days", {"Type": "Int32"}], ["TickRemainder", {"Type": "UInt32"}], ["SubFramePeriod",
                                                      {"Type": "UInt32"}]]}""")

