from django.test import TestCase

# Create your tests here.
# Create your tests here.
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import os, django, sys

sys.path.append('./')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restframeworkdemo.settings")  # 导入django的配置文件
django.setup()
from vitaldata.models import VitalData

vital = VitalData.objects.create(
    tg_num=52740,
    tg_num_old=52740,
    tg_num_change='0',
    tg_num_change_status='不变',
    meter_num=4079779,
    meter_num_old=4079779,
    meter_num_change='0',
    meter_num_change_status='不变',
    new_tgs_num=1864,
    new_tg_num_old=1864,
    new_tg_num_change='0',
    new_tg_num_change_status='不变',
    nor_tgs_num=47940,
    nor_tgs_num_old=47939,
    nor_tgs_num_change='1',
    nor_tgs_num_change_status='增加',
    abnor_tgs_num=2936,
    abnor_tgs_num_old=2937,
    abnor_tgs_num_change='-1',
    abnor_tgs_num_change_status='降低',
    tg_cal_rate=94.23,
    tg_cal_rate_old=94.23,
    tg_cal_rate_change='0.0',
    tg_cal_rate_change_status='不变',
    obs_meters_num=1684589,
    obs_meters_num_old=1684562,
    obs_meters_num_change='27',
    obs_meters_num_change_status='增加',
    nor_meters_num=2371021,
    nor_meters_num_old=2371047,
    nor_meters_num_change='-26',
    nor_meters_num_change_status='降低',
    abnor_meters_num=24169,
    abnor_meters_num_old=24170,
    abnor_meters_num_change='-1',
    abnor_meters_num_change_status='降低',
    cal_date='2022-05-17',
    cal_date_old='2022-05-09',
    meter_com_rate_num='96.99',
    meter_com_rate_num_old='96.99',
    meter_com_rate_num_change='0.0',
    meter_com_rate_num_change_status='不变',
    un_govern_question_num=6805,
    un_govern_question_num_old=6809,
    un_govern_question_num_change='-4',
    un_govern_question_num_change_status='降低',
    cal_tgs_num=47940,
    cal_tgs_num_old=47939,
    cal_tgs_num_change='1',
    cal_tgs_num_change_status='增加',
    un_govern_tgs_num=2895,
    un_govern_tgs_num_old=2896,
    un_govern_tgs_num_change='-1',
    un_govern_tgs_num_change_status='降低',
    involve_meters_num=40075,
    involve_meters_num_old=40085,
    involve_meters_num_change='-10',
    involve_meters_num_change_status='降低',
    white_tgs_num=2,
    white_tgs_num_old=2,
    white_tgs_num_change='0',
    white_tgs_num_change_status='不变',
    all_abnor_tgs_num=6838,
    all_abnor_tgs_num_old=6838,
    all_abnor_tgs_num_change='0',
    all_abnor_tgs_num_change_status='不变',
    abnor_tg_govern_rate_num='57.66',
    abnor_tg_govern_rate_num_old='57.65',
    abnor_tg_govern_rate_num_change='0.01',
    abnor_tg_govern_rate_num_change_status='增加',
    all_questions_num=22258,
    all_questions_num_old=22252,
    all_questions_num_change='6',
    all_questions_num_change_status='增加',
    questions_govern_rate='69.43',
    questions_govern_rate_old='69.4',
    questions_govern_rate_change='0.03',
    questions_govern_rate_change_status='增加',
    precompute_time='08分45秒',
    precompute_time_old='',
    precompute_time_change='',
    precompute_time_change_status='',
    check_meter_num_model=44,
    check_meter_num_model_old=44,
    check_meter_num_model_change=0,
    check_meter_num_model_change_status='不变',
    check_meter_num_sz=10,
    check_meter_num_sz_old=10,
    check_meter_num_sz_change='0',
    check_meter_num_sz_change_status='不变',
    container_version='2.0.4_release_test',
    container_version_old='2.0.4_beta'
)

