# coding=utf-8

import math
from typing import Callable

from number import Number
from decorator import staticmethod


class Operation:
    """
    Expression.Operation class used to store math operations and info about it
    """

    @staticmethod("+", prior=False)
    def addition(
            *summands: Number
    ) -> Number:
        """
        Summand numbers

        Args:
            *summands (Number): Numbers you want to summand

        Returns:
            Number: Result
        """

        result = 0

        for summand in summands:
            result += summand

        return result

    @staticmethod("-", prior=False)
    def subtract(
            minuend: Number,
            *subtrahends: Number
    ) -> Number:
        """
        Substract numbers

        Args:
            minuend (Number): Minuend numbers
            *subtrahends (Number): Number you want to substract

        Returns:
            Number: result
        """

        result = minuend

        for subtrahend in subtrahends:
            result -= subtrahend

        return result

    @staticmethod("*")
    def multiply(
            *multipliers: Number
    ) -> Number:
        """
        Multiply numbers

        Args:
            *multipliers (Number): Numbers you want to multiply

        Returns:
            Number: Result
        """

        result = 1

        for multiplier in multipliers:
            result *= multiplier

        return result

    @staticmethod("/")
    def division(
            dividend: Number,
            *divisors: Number
    ) -> Number:
        """
        Divide numbers

        Args:
            dividend (Number): Divident number
            *divisors (Number): Divisor numbers

        Returns:
            Number: Result
        """

        result = dividend

        for divisor in divisors:
            result /= divisor

        return result

    @staticmethod("%")
    def mod(
            dividend: Number,
            *divisors: Number
    ) -> Number:
        """
        Remainder of division

        Args:
            dividend (Number): Divident number
            *divisors (Number): Divisor numbers

        Returns:
            Number: Result
        """

        result = dividend

        for divisor in divisors:
            result %= divisor

        return result

    @staticmethod("^")
    def power(
            base: Number,
            *powers: Number
    ) -> Number:
        """
        Raise number to power

        Args:
            base (Number): Base
            *powers (Number): Powers

        Returns:
            Number: Power result
        """

        result = base

        for power in powers:
            result **= power

        return result

    def __class_getitem__(
            cls,
            operator: str
    ) -> Callable:
        """
        __class_getitem__ method override.
        Used to get operation method for specified operator char

        Args:
            operator (str): Operator

        Returns:
            Callable: Operation method

        Raises:
            ValueError: If specified operation not found

        Examples:
            >>> Expression.Operation["*"](2, 2)
            4
            >>> addFunc = Expression.Operation["+"]
            >>> addFunc(3, 4)
            7

        Notes:
            It searches methods from Expression.Operator.__dict__ (except method names containing "_")
            and checks if specified operator method is in method __dir__ attribute.
            If there is no such method, then searches math package functions
        """

        operations = dict(
            filter(
                lambda key: "_" not in key[0],
                {
                    **math.__dict__,
                    **cls.__dict__
                }.items()
            )
        )

        for operation, function in operations.items():
            try:
                # If requested operator specified in decorator
                if operator in function.args:
                    return function
            except AttributeError:
                # If decorator not used (math package functions)
                # Checks if requested operator is name of function
                if operator == operation:
                    return function

        raise ValueError(f"Operation '{operator}' not found.")

    @classmethod
    def exists(
            cls,
            operator: str,
            prior=False
    ) -> bool:
        """
        Checks if there are given operator method

        Args:
            operator (str): Operator you want to check
            prior (bool): True if operator must be prior (like multiply). Defaults by False

        Returns:
            bool: Is there given operator method
        """

        operations = dict(
            filter(
                lambda key: "_" not in key[0],
                cls.__dict__.items()
            )
        )

        for operation in operations.values():
            try:
                if operator in operation.args:
                    if not prior or operation.prior:
                        return True
            except AttributeError:
                pass

        return False