# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Category(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'category_group_id': 'str',
        'name': 'str',
        'hidden': 'bool',
        'note': 'str',
        'budgeted': 'float',
        'activity': 'float',
        'balance': 'float'
    }

    attribute_map = {
        'id': 'id',
        'category_group_id': 'category_group_id',
        'name': 'name',
        'hidden': 'hidden',
        'note': 'note',
        'budgeted': 'budgeted',
        'activity': 'activity',
        'balance': 'balance'
    }

    def __init__(self, id=None, category_group_id=None, name=None, hidden=None, note=None, budgeted=None, activity=None, balance=None):  # noqa: E501
        """Category - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._category_group_id = None
        self._name = None
        self._hidden = None
        self._note = None
        self._budgeted = None
        self._activity = None
        self._balance = None
        self.discriminator = None

        self.id = id
        self.category_group_id = category_group_id
        self.name = name
        self.hidden = hidden
        self.note = note
        self.budgeted = budgeted
        self.activity = activity
        self.balance = balance

    @property
    def id(self):
        """Gets the id of this Category.  # noqa: E501


        :return: The id of this Category.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Category.


        :param id: The id of this Category.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def category_group_id(self):
        """Gets the category_group_id of this Category.  # noqa: E501


        :return: The category_group_id of this Category.  # noqa: E501
        :rtype: str
        """
        return self._category_group_id

    @category_group_id.setter
    def category_group_id(self, category_group_id):
        """Sets the category_group_id of this Category.


        :param category_group_id: The category_group_id of this Category.  # noqa: E501
        :type: str
        """
        if category_group_id is None:
            raise ValueError("Invalid value for `category_group_id`, must not be `None`")  # noqa: E501

        self._category_group_id = category_group_id

    @property
    def name(self):
        """Gets the name of this Category.  # noqa: E501


        :return: The name of this Category.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Category.


        :param name: The name of this Category.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def hidden(self):
        """Gets the hidden of this Category.  # noqa: E501

        Whether or not the category is hidden  # noqa: E501

        :return: The hidden of this Category.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Category.

        Whether or not the category is hidden  # noqa: E501

        :param hidden: The hidden of this Category.  # noqa: E501
        :type: bool
        """
        if hidden is None:
            raise ValueError("Invalid value for `hidden`, must not be `None`")  # noqa: E501

        self._hidden = hidden

    @property
    def note(self):
        """Gets the note of this Category.  # noqa: E501


        :return: The note of this Category.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Category.


        :param note: The note of this Category.  # noqa: E501
        :type: str
        """
        self._note = note

    @property
    def budgeted(self):
        """Gets the budgeted of this Category.  # noqa: E501

        Budgeted amount in current month in milliunits format  # noqa: E501

        :return: The budgeted of this Category.  # noqa: E501
        :rtype: float
        """
        return self._budgeted

    @budgeted.setter
    def budgeted(self, budgeted):
        """Sets the budgeted of this Category.

        Budgeted amount in current month in milliunits format  # noqa: E501

        :param budgeted: The budgeted of this Category.  # noqa: E501
        :type: float
        """
        if budgeted is None:
            raise ValueError("Invalid value for `budgeted`, must not be `None`")  # noqa: E501

        self._budgeted = budgeted

    @property
    def activity(self):
        """Gets the activity of this Category.  # noqa: E501

        Activity amount in current month in milliunits format  # noqa: E501

        :return: The activity of this Category.  # noqa: E501
        :rtype: float
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this Category.

        Activity amount in current month in milliunits format  # noqa: E501

        :param activity: The activity of this Category.  # noqa: E501
        :type: float
        """
        if activity is None:
            raise ValueError("Invalid value for `activity`, must not be `None`")  # noqa: E501

        self._activity = activity

    @property
    def balance(self):
        """Gets the balance of this Category.  # noqa: E501

        Balance in current month in milliunits format  # noqa: E501

        :return: The balance of this Category.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Category.

        Balance in current month in milliunits format  # noqa: E501

        :param balance: The balance of this Category.  # noqa: E501
        :type: float
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Category):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
