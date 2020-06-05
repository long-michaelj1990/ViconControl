
from vicon_core_api import SchemaServices
from vicon_core_api import ViconInterface
from enum import Enum
from vicon_core_api import Result


class SubjectServices(ViconInterface):
    """Functions for controlling and monitoring subjects."""

    class ESubjectType(Enum):
        """Type of subject.

        Enum Values:
            EGeneral: General multi-segment subject.
            EProp: Single or multi-segment prop.
            ELabelingCluster: Cluster of markers labeled as a single-segment target.
            ETrackerObject: Tracker-style object labeled as a single-segment target.
        """
        EGeneral = 1
        EProp = 2
        ELabelingCluster = 3
        ETrackerObject = 4


    class ESubjectRole(Enum):
        """Role this subject supports.

        Enum Values:
            ELabeling: Subject for intermediate marker tracking and labeling.
            ESolving: Subject for kinematic solving.
        """
        ELabeling = 1
        ESolving = 2


    def __init__(self, client):
        """Initialises SubjectServices with a Client and checks if interface is supported."""
        super(SubjectServices, self).__init__(client)

    def import_subject(self, directory, name, type):
        """Import subject from file.

        If a subject with the same name is already loaded then it will be overwritten

        Args:
            directory < string >: Absolute path to a directory containing a valid VSK or VSS file matching the subject name.
            name < string >: Name of subject. 'Name.vsk' and 'Name.vss' will be loaded from the supplied directory (if present).
            type < SubjectServices.ESubjectType >: Type of subject.

        Return:
            return < Result >: Ok - On success.
                NotFound - If directory does not exist or no matching subject files were found.
                FileIOFailure - If a subject file could not be read.
        """
        return self.client.send_command("SubjectServices.ImportSubject", directory, name, type)

    def remove_subject(self, name):
        """Remove a named subject.

        Args:
            name < string >: Name of the subject.

        Return:
            return < Result >: Ok - On success.
                NotFound - If subject was not already loaded.
        """
        return self.client.send_command("SubjectServices.RemoveSubject", name)

    def remove_all_subjects(self):
        """Remove all subjects.

        Return:
            return < Result >: Ok - On success.
                NotFound - If no subjects were loaded.
        """
        return self.client.send_command("SubjectServices.RemoveAllSubjects")

    def subjects(self):
        """Get names of all loaded subjects.

        Return:
            return < Result >: Ok - On success.
            subject_names < [string] >: Names of loaded subjects.
        """
        return self.client.send_command("SubjectServices.Subjects")

    def subject_type(self, name):
        """Determine type of a subject.

        Args:
            name < string >: Name of subject.

        Return:
            return < Result >: Ok - On success.
            type < SubjectServices.ESubjectType >: Type of subject.
        """
        return self.client.send_command("SubjectServices.SubjectType", name)

    def subject_roles(self, name):
        """Determine roles supported by a subject.

        Args:
            name < string >: Name of subject.

        Return:
            return < Result >: Ok - On success.
            roles < [SubjectServices.ESubjectRole] >: Roles supported by subject.
        """
        return self.client.send_command("SubjectServices.SubjectRoles", name)

    def add_subjects_changed_callback(self, function):
        """Callback issued whenever the list of loaded subjects has changed."""
        return self.client.add_callback("SubjectServices.SubjectsChangedCallback", function)

    def set_subject_enabled(self, subject_name, enable):
        """Enable or disable a subject.

        Args:
            subject_name < string >: Name of the subject.
            enable < bool >: Enable if true, otherwise disable.

        Return:
            return < Result >: Ok - On success.
                NotFound - If the subject was not found.
        """
        return self.client.send_command("SubjectServices.SetSubjectEnabled", subject_name, enable)

    def set_all_subjects_enabled(self, enable):
        """Enable or disable all subjects.

        Args:
            enable < bool >: Enable if true, otherwise disable.

        Return:
            return < Result >: Ok - On success.
                NotFound - If no subjects were found.
        """
        return self.client.send_command("SubjectServices.SetAllSubjectsEnabled", enable)

    def enabled_subjects(self):
        """Get names of all enabled subjects.

        Return:
            return < Result >: Ok - On success.
            subject_names < [string] >: Names of enabled subjects.
        """
        return self.client.send_command("SubjectServices.EnabledSubjects")

    def add_enabled_subjects_changed_callback(self, function):
        """Callback issued whenever the list of subjects enabled has changed."""
        return self.client.add_callback("SubjectServices.EnabledSubjectsChangedCallback", function)

    def remove_callback(self, callback_id):
        """remove callback of any type using the id supplied when it was added."""
        return self.client.remove_callback(callback_id)



SchemaServices.register_json_schema(SubjectServices,"""{"Type": "NamedTuple", "TypeName": "SubjectServices"}""")

SchemaServices.register_json_schema(SubjectServices.ESubjectType,"""{"Type": "Enum32", "TypeName": "SubjectServices.ESubjectType", "EnumValues": [["General", 1], ["Prop", 2], ["LabelingCluster",
                                                                    3], ["TrackerObject", 4]]}""")

SchemaServices.register_json_schema(SubjectServices.ESubjectRole,"""{"Type": "Enum32", "TypeName": "SubjectServices.ESubjectRole", "EnumValues": [["Labeling", 1], ["Solving", 2]]}""")

SchemaServices.register_json_schema(SubjectServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "SubjectServices.ImportSubject", "SubSchemas": [["Return", {"Type":
                                                       "UInt32", "Role": "Result"}], ["Directory", {"Type": "String", "Role": "Input"}], ["Name", {"Type": "String", "Role": "Input"}],
                                                       ["Type", {"Type": "Ref", "Role": "Input", "TypeName": "SubjectServices.ESubjectType"}]]}""")

SchemaServices.register_json_schema(SubjectServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "SubjectServices.RemoveSubject", "SubSchemas": [["Return", {"Type":
                                                       "UInt32", "Role": "Result"}], ["Name", {"Type": "String", "Role": "Input"}]]}""")

SchemaServices.register_json_schema(SubjectServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "SubjectServices.RemoveAllSubjects", "SubSchemas": [["Return", {"Type":
                                                       "UInt32", "Role": "Result"}]]}""")

SchemaServices.register_json_schema(SubjectServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "SubjectServices.Subjects", "SubSchemas": [["Return", {"Type": "UInt32",
                                                       "Role": "Result"}], ["SubjectNames", {"Type": "List", "Role": "Output", "SubSchemas": [["", {"Type": "String"}]]}]]}""")

SchemaServices.register_json_schema(SubjectServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "SubjectServices.SubjectType", "SubSchemas": [["Return", {"Type":
                                                       "UInt32", "Role": "Result"}], ["Name", {"Type": "String", "Role": "Input"}], ["Type", {"Type": "Ref", "Role": "Output",
                                                       "TypeName": "SubjectServices.ESubjectType"}]]}""")

SchemaServices.register_json_schema(SubjectServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "SubjectServices.SubjectRoles", "SubSchemas": [["Return", {"Type":
                                                       "UInt32", "Role": "Result"}], ["Name", {"Type": "String", "Role": "Input"}], ["Roles", {"Type": "List", "Role": "Output",
                                                       "SubSchemas": [["", {"Type": "Ref", "TypeName": "SubjectServices.ESubjectRole"}]]}]]}""")

SchemaServices.register_json_schema(SubjectServices,"""{"Type": "NamedTuple", "Role": "Callback", "TypeName": "SubjectServices.SubjectsChangedCallback"}""")

SchemaServices.register_json_schema(SubjectServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "SubjectServices.SetSubjectEnabled", "SubSchemas": [["Return", {"Type":
                                                       "UInt32", "Role": "Result"}], ["SubjectName", {"Type": "String", "Role": "Input"}], ["Enable", {"Type": "Bool", "Role":
                                                       "Input"}]]}""")

SchemaServices.register_json_schema(SubjectServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "SubjectServices.SetAllSubjectsEnabled", "SubSchemas": [["Return",
                                                       {"Type": "UInt32", "Role": "Result"}], ["Enable", {"Type": "Bool", "Role": "Input"}]]}""")

SchemaServices.register_json_schema(SubjectServices,"""{"Type": "NamedTuple", "Role": "Function", "TypeName": "SubjectServices.EnabledSubjects", "SubSchemas": [["Return", {"Type":
                                                       "UInt32", "Role": "Result"}], ["SubjectNames", {"Type": "List", "Role": "Output", "SubSchemas": [["", {"Type": "String"}]]}]]}""")

SchemaServices.register_json_schema(SubjectServices,"""{"Type": "NamedTuple", "Role": "Callback", "TypeName": "SubjectServices.EnabledSubjectsChangedCallback"}""")

