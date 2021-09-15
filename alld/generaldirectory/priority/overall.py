from alld.maincommunication.mainreps import *
import vk_api
import vk
import bs4
import wikipedia
import psycopg2
import requests
import time
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload
from urllib.request import urlopen
import linecache
from social_ethosa import *


import numpy as np
from sklearn.neighbors import BallTree
from sklearn.base import BaseEstimator
import csv

al_id = 272566909
admin = 391653357
#vk@id

hi = 0
uses = {}
dobavili = {}
user_ans = {}
user_fast_d = {}