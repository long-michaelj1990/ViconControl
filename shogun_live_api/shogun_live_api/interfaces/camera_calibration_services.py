
from vicon_core_api import SchemaServices
from vicon_core_api import ViconInterface
from vicon_core_api import Result


class CameraCalibrationServices(ViconInterface):
    """Functions for loading/saving camera calibrations and registering for event notifications."""
    def __init__(self, client):
        """Initialises CameraCalibrationServices with a Client and checks if interface is supported."""
        super(CameraCalibrationServices, self).__init__(client)

    def import_camera_calibration(self, file_path):
        """Import a camera calibration from file (*.

        mcp *.xcp)

        Args:
            file_path < string >: Full path to camera calibration file.

        Return:
            return < Result >: Ok - On success.
                NotFound - If file does not exist.
                NotSupported - If file extension is not '.mcp' or '.xcp'.
                FileIOFailure - If file could not be loaded.
        """
        return self.client.send_command("CameraCalibrationServices.ImportCameraCalibration", file_path)

    def export_camera_calibration(self, file_path):
        """Export a camera calibration to an XCP file (*.

        xcp)

        Args:
            file_path < string >: Full path to desired location of camera calibration file.

        Return:
            return < Result >: Ok - On success.
                NotSupported - If file extension is not '.xcp'.
                FileIOFailure - If file could not be saved.
        """
        return self.client.send_command("CameraCalibrationServices.ExportCameraCalibration", file_path)

    def clear_camera_calibration(self):
        """Clear the current camera calibration.

        Return:
            return < Result >: Ok - On success.
        """
        return self.client.send_command("CameraCalibrationServices.ClearCameraCalibration")



SchemaServices.register_json_schema(CameraCalibrationServices,"""{"Type": "NamedTuple", "TypeName": "CameraCalibrationServices"}""")

SchemaServices.register_json_schema(CameraCalibrationServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "CameraCalibrationServices.ImportCameraCalibration", "SubSchemas":
                                                                 [["Return", {"Type": "UInt32", "Role": "Result"}], ["FilePath", {"Type": "String", "Role": "Input"}]]}""")

SchemaServices.register_json_schema(CameraCalibrationServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "CameraCalibrationServices.ExportCameraCalibration", "SubSchemas":
                                                                 [["Return", {"Type": "UInt32", "Role": "Result"}], ["FilePath", {"Type": "String", "Role": "Input"}]]}""")

SchemaServices.register_json_schema(CameraCalibrationServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "CameraCalibrationServices.ClearCameraCalibration", "SubSchemas":
                                                                 [["Return", {"Type": "UInt32", "Role": "Result"}]]}""")

