# Unless explicitly stated otherwise all files in this repository are licensed
# under the Apache License 2.0.
# Copyright 2020 Datadog, Inc. for original work
# Copyright 2021 GraphMetrics for modifications

"""Exceptions thrown by DDSketch"""


class IllegalArgumentException(Exception):
    """thrown when an argument is misspecified"""


class UnequalSketchParametersException(Exception):
    """thrown when trying to merge two sketches with different relative_accuracy
    parameters
    """
