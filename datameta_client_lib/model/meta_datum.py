"""
    DataMeta

    DataMeta  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: leon.kuchenbecker@uni-tuebingen.de
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from datameta_client_lib.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


class MetaDatum(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'name': (str,),  # noqa: E501
            'regex_description': (str,),  # noqa: E501
            'long_description': (str,),  # noqa: E501
            'example': (str,),  # noqa: E501
            'reg_exp': (str,),  # noqa: E501
            'date_time_fmt': (str,),  # noqa: E501
            'is_mandatory': (bool,),  # noqa: E501
            'order': (int,),  # noqa: E501
            'is_file': (bool,),  # noqa: E501
            'is_submission_unique': (bool,),  # noqa: E501
            'is_site_unique': (bool,),  # noqa: E501
            'service_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'regex_description': 'regexDescription',  # noqa: E501
        'long_description': 'longDescription',  # noqa: E501
        'example': 'example',  # noqa: E501
        'reg_exp': 'regExp',  # noqa: E501
        'date_time_fmt': 'dateTimeFmt',  # noqa: E501
        'is_mandatory': 'isMandatory',  # noqa: E501
        'order': 'order',  # noqa: E501
        'is_file': 'isFile',  # noqa: E501
        'is_submission_unique': 'isSubmissionUnique',  # noqa: E501
        'is_site_unique': 'isSiteUnique',  # noqa: E501
        'service_id': 'serviceId',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, name, regex_description, long_description, example, reg_exp, date_time_fmt, is_mandatory, order, is_file, is_submission_unique, is_site_unique, service_id, *args, **kwargs):  # noqa: E501
        """MetaDatum - a model defined in OpenAPI

        Args:
            name (str):
            regex_description (str):
            long_description (str):
            example (str):
            reg_exp (str):
            date_time_fmt (str):
            is_mandatory (bool):
            order (int):
            is_file (bool):
            is_submission_unique (bool):
            is_site_unique (bool):
            service_id (str, none_type):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.name = name
        self.regex_description = regex_description
        self.long_description = long_description
        self.example = example
        self.reg_exp = reg_exp
        self.date_time_fmt = date_time_fmt
        self.is_mandatory = is_mandatory
        self.order = order
        self.is_file = is_file
        self.is_submission_unique = is_submission_unique
        self.is_site_unique = is_site_unique
        self.service_id = service_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
