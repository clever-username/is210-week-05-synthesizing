#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program converts temperatures between various standards."""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Convert Fahrenheit to decimal of Celsius value

    Args:
        degrees (int): Value specifying degrees Fahrenheit
    Returns:
        celsius (decimal): Temperature in degrees Celsius
    Example:

        >>> fahrenheit_to_celsius(32)
        Decimal('0')
    """
    celsius = (decimal.Decimal(degrees) - decimal.Decimal(32)) * 5 / 9
    return celsius


def celsius_to_kelvin(degrees):
    """Convert Celsius to Kelvin

    Args:
        degrees (int): Value specifying degrees Celsius
    Returns:
        kelvin (decimal): Temperature in degrees Kelvin
    Example:

        >>> celsius_to_kelvin(20)
        Decimal('293.15')
    """
    kelvin = decimal.Decimal(degrees + ABSOLUTE_DIFFERENCE)
    return kelvin


def fahrenheit_to_kelvin(degrees):
    """Convert Fahrenheit to Kelvin by calling fahrenheit_to_celsius function
    and celsius_to_kelvin function

    Args:
        degrees (int): Value specifying degrees Fahrenheit
    Returns:
        faranheit (decimal): Temperature in degrees Kelvin
    Example:

        >>> fahrenheit_to_kelvin(75)
        Decimal('297.0388888888888888888888889')
    """
    faranheit = celsius_to_kelvin(fahrenheit_to_celsius(degrees))
    return faranheit
