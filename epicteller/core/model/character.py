#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel


class Character(BaseModel):
    id: int
    url_token: str
    member_id: Optional[int]
    name: str
    avatar: str
    description: str
    is_removed: bool
    raw_data: dict
    created: int
    updated: int
