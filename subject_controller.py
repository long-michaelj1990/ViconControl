"""Defines a basic controller for subjects."""
import sys

from vicon_core_api import Client
from vicon_core_api import RPCError

from shogun_live_api.interfaces import SubjectServices


def list_to_string(string_list):
    """Concatenate list of strings."""
    return ', '.join(str(s) for s in string_list)


def subject_type_to_string(subject_type):
    """Convert subject type enum value to string."""
    if subject_type is SubjectServices.ESubjectType.EGeneral:
        return 'general'
    elif subject_type is SubjectServices.ESubjectType.ERigidObject:
        return 'prop'
    elif subject_type is SubjectServices.ESubjectType.ELabelingCluster:
        return 'labeling cluster'
    return 'object'


def string_to_subject_type(subject_type):
    """Convert subject type enum value to string."""
    if subject_type == 'general':
        return SubjectServices.ESubjectType.EGeneral
    elif subject_type == 'prop':
        return SubjectServices.ESubjectType.ERigidObject
    elif subject_type == 'labeling cluster':
        return SubjectServices.ESubjectType.ELabelingCluster
    return SubjectServices.ESubjectType.ETrackerObject


def subject_role_to_string(role):
    """Convert subject role enum value to string."""
    if role is SubjectServices.ESubjectRole.ELabeling:
        return 'labeling'
    return 'solving'


class BasicSubjectController(object):
    """Implements basic subject control functions."""
    def __init__(self, host, port, verbose):
        self.client = Client(host, port)
        if not self.client.connected:
            print 'Server not found at ' + host + ':' + str(port)
            sys.exit()

        self.verbose = verbose
        if self.verbose:
            print 'Connected to: [ ' + host + ':' + str(port) + ' ]'

        self.subject_service = SubjectServices(self.client)

        if self.verbose:
            self.print_general_info()

    def import_subject(self, directory, subject_name, subject_type):
        try:
            result = self.subject_service.import_subject(directory, subject_name, subject_type)
            if self.verbose:
                print 'Import subject result - ' + str(result)
                self.print_general_info()
            return result
        except RPCError as e:
            print e

    def remove_subject(self, name):
        try:
            result = self.subject_service.remove_subject(name)
            if self.verbose:
                print 'Remove subject result - ' + str(result)
                self.print_general_info()
            return result
        except RPCError as e:
            print e

    def remove_all_subjects(self):
        try:
            result = self.subject_service.remove_all_subjects()
            if self.verbose:
                print 'Remove all subjects result - ' + str(result)
                self.print_general_info()
            return result
        except RPCError as e:
            print e

    def set_subject_enabled(self, name, enable):
        try:
            result = self.subject_service.set_subject_enabled(name, enable)
            if self.verbose:
                print('Enable' if enable else 'Disable') + ' subject result - ' + str(result)
                self.print_enabled_subjects()
            return result
        except RPCError as e:
            print e

    def set_all_subjects_enabled(self, enable):
        try:
            result = self.subject_service.set_all_subjects_enabled(enable)
            if self.verbose:
                print('Enable' if enable else 'Disable') + ' all subjects result - ' + str(result)
                self.print_enabled_subjects()
            return result
        except RPCError as e:
            print e

    def print_general_info(self):
        self.print_subjects()
        self.print_enabled_subjects()

    def print_subjects(self):
        try:
            _result, subjects = self.subject_service.subjects()
            print 'Loaded subjects: '
            for subject in subjects:
                _type_result, subject_type = self.subject_service.subject_type(subject)
                _roles_result, subject_roles = self.subject_service.subject_roles(subject)
                sys.stdout.write('\t' + subject + ' (' + subject_type_to_string(subject_type))
                first_role = True
                for role in subject_roles:
                    sys.stdout.write((': ' if first_role else ', ') + subject_role_to_string(role))
                    first_role = False
                print ')'
        except RPCError as e:
            print e

    def print_enabled_subjects(self):
        try:
            result, subjects = self.subject_service.enabled_subjects()
            if result:
                print 'Enabled subjects: ' + list_to_string(subjects)
        except RPCError as e:
            print e

    def shutdown(self):
        self.client.stop()
