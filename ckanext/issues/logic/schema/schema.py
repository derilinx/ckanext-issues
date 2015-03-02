from ckan.plugins import toolkit
from ckanext.issues.logic.validators import (
    as_package_id,
    is_valid_sort,
    is_valid_status,
)

not_missing = toolkit.get_validator('not_missing')
ignore_missing = toolkit.get_validator('ignore_missing')
package_exists = toolkit.get_validator('package_id_or_name_exists')
resource_id_exists = toolkit.get_validator('resource_id_exists')
user_exists = toolkit.get_validator('user_id_or_name_exists')
is_natural_number = toolkit.get_validator('natural_number_validator')
is_positive_integer = toolkit.get_validator('is_positive_integer')


def issue_update_schema():
    return {
        'id': [not_missing, unicode],
        'title': [ignore_missing, unicode],
        'description': [ignore_missing, unicode],
        'dataset_id': [ignore_missing, unicode, package_exists, as_package_id],
        'resource_id': [ignore_missing, unicode, resource_id_exists],
        'resolver_id': [ignore_missing, unicode, user_exists],
        'status':  [ignore_missing, unicode],
    }


def issue_list_schema():
    return {
        'dataset_id': [not_missing, unicode, package_exists, as_package_id],
        'status': [ignore_missing, unicode, is_valid_status],
        'sort': [ignore_missing, unicode, is_valid_sort],
        'limit': [ignore_missing, is_natural_number],
        'offset': [ignore_missing, is_natural_number],
    }


def issue_count_schema():
    return {
        'dataset_id': [not_missing, unicode, package_exists, as_package_id],
    }


def issue_home_controller_schema():
    return {
        'status': [ignore_missing, unicode],
        'sort': [ignore_missing, unicode ],
        'page': [ignore_missing, is_positive_integer],
        'per_page': [ignore_missing, is_positive_integer],
    }