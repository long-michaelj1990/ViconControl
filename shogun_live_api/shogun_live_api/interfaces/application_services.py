
from vicon_core_api import SchemaServices
from vicon_core_api import ViconInterface
from vicon_core_api import Result


class ApplicationServices(ViconInterface):
    """Functions for controlling the application and registering for event notifications."""
    def __init__(self, client):
        """Initialises ApplicationServices with a Client and checks if interface is supported."""
        super(ApplicationServices, self).__init__(client)

    def shutdown(self):
        """Shutdown the application shutdown, closing all device connections.

        Return:
            return < Result >: Ok - On success.
                NotPermitted - If application is in a mode that prevents shutdown.
            blocking_mode < string >: Application mode preventing shutdown (if any).
        """
        return self.client.send_command("ApplicationServices.Shutdown")

    def load_system_configuration(self, file_path):
        """Load a system configuration from file.

        Args:
            file_path < string >: Full path to system file.

        Return:
            return < Result >: Ok - On success.
                NotFound - If system file does not exist.
                FileIOFailure - If system file could not be loaded.
        """
        return self.client.send_command("ApplicationServices.LoadSystemConfiguration", file_path)

    def save_system_configuration(self, file_path):
        """Save system configuration to a file.

        Args:
            file_path < string >: Full path to desired location of system file.

        Return:
            return < Result >: Ok - On success.
                FileIOFailure - If system file could not be saved.
        """
        return self.client.send_command("ApplicationServices.SaveSystemConfiguration", file_path)



SchemaServices.register_json_schema(ApplicationServices,"""{"Type": "NamedTuple", "TypeName": "ApplicationServices"}""")

SchemaServices.register_json_schema(ApplicationServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "ApplicationServices.Shutdown", "SubSchemas": [["Return", {"Type":
                                                           "UInt32", "Role": "Result"}], ["BlockingMode", {"Type": "String", "Role": "Output"}]]}""")

SchemaServices.register_json_schema(ApplicationServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "ApplicationServices.LoadSystemConfiguration", "SubSchemas": [["Return",
                                                           {"Type": "UInt32", "Role": "Result"}], ["FilePath", {"Type": "String", "Role": "Input"}]]}""")

SchemaServices.register_json_schema(ApplicationServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "ApplicationServices.SaveSystemConfiguration", "SubSchemas": [["Return",
                                                           {"Type": "UInt32", "Role": "Result"}], ["FilePath", {"Type": "String", "Role": "Input"}]]}""")

