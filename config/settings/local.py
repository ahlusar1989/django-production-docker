from __future__ import absolute_import
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY',
	default='gg0kcl&m1nxt2j_jn=mp_q50gdvn82jr^waqd3_c)nil)a=a#c')

DEBUG = env.bool('DJANGO_DEBUG', default=True)