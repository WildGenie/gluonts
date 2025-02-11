# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from typing import Any

import pandas as pd
from pandas.tseries.offsets import BaseOffset

from ._base import Kind, encode


@encode.register(pd.Timestamp)
def encode_pd_timestamp(v: pd.Timestamp) -> Any:
    """
    Specializes :func:`encode` for invocations where ``v`` is an instance of
    the :class:`~pandas.Timestamp` class.
    """
    return {
        "__kind__": Kind.Instance,
        "class": "pandas.Timestamp",
        "args": encode([str(v)]),
    }


@encode.register(pd.Period)
def encode_pd_period(v: pd.Period) -> Any:
    """
    Specializes :func:`encode` for invocations where ``v`` is an instance of
    the :class:`~pandas.Period` class.
    """
    return {
        "__kind__": Kind.Instance,
        "class": "pandas.Timestamp",
        "args": encode([str(v)]),
        "kwargs": {"freq": v.freqstr},
    }


@encode.register(BaseOffset)
def encode_pd_baseoffset(v: BaseOffset) -> Any:
    return {
        "__kind__": Kind.Instance,
        "class": "pandas.tseries.frequencies.to_offset",
        "args": encode([v.freqstr]),
        "kwargs": {},
    }
