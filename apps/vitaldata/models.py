from django.db import models


# Create your models here.


class VitalData(models.Model):
    tg_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='台区总数')
    tg_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='台区总数_old')
    tg_num_change = models.CharField(null=True, blank=True, verbose_name='台区总数_变化值', max_length=20)
    tg_num_change_status = models.CharField(null=True, blank=True, verbose_name='台区总数_对比结果', max_length=20)
    meter_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='电能表数量')
    meter_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='电能表数量_old')
    meter_num_change = models.CharField(null=True, blank=True, verbose_name='电能表数量_变化值', max_length=20)
    meter_num_change_status = models.CharField(null=True, blank=True, verbose_name='电能表数量_对比结果', max_length=20)
    new_tgs_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='新建台区数量')
    new_tg_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='新建台区数量_old')
    new_tg_num_change = models.CharField(null=True, blank=True, verbose_name='新建台区数量_变化值', max_length=20)
    new_tg_num_change_status = models.CharField(null=True, blank=True, verbose_name='新建台区数量_对比结果', max_length=20)
    nor_tgs_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='正常台区数量')
    nor_tgs_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='正常台区数量_old')
    nor_tgs_num_change = models.CharField(null=True, blank=True, verbose_name='正常台区数量_变化值', max_length=20)
    nor_tgs_num_change_status = models.CharField(null=True, blank=True, verbose_name='正常台区数量_对比结果', max_length=20)
    abnor_tgs_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='异常台区数量')
    abnor_tgs_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='异常台区数量_old')
    abnor_tgs_num_change = models.CharField(null=True, blank=True, verbose_name='异常台区数量_变化值', max_length=20)
    abnor_tgs_num_change_status = models.CharField(null=True, blank=True, verbose_name='异常台区数量_对比结果', max_length=20)
    tg_cal_rate = models.DecimalField(null=True, blank=True, default=0, verbose_name='台区可算率', max_digits=4,
                                      decimal_places=2)
    tg_cal_rate_old = models.DecimalField(null=True, blank=True, default=0, verbose_name='台区可算率_old', max_digits=4,
                                          decimal_places=2)
    tg_cal_rate_change = models.DecimalField(null=True, blank=True, verbose_name='台区可算率_变化值', max_digits=4,
                                             decimal_places=2)
    tg_cal_rate_change_status = models.CharField(null=True, blank=True, verbose_name='台区可算率_对比结果', max_length=20)
    obs_meters_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='观察表数量')
    obs_meters_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='观察表数量_old')
    obs_meters_num_change = models.CharField(null=True, blank=True, verbose_name='观察表数量_变化值', max_length=20)
    obs_meters_num_change_status = models.CharField(null=True, blank=True, verbose_name='观察表数量_对比结果', max_length=20)
    nor_meters_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='正常表数量')
    nor_meters_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='正常表数量_old')
    nor_meters_num_change = models.CharField(null=True, blank=True, verbose_name='正常表数量_变化值', max_length=20)
    nor_meters_num_change_status = models.CharField(null=True, blank=True, verbose_name='正常表数量_对比结果', max_length=20)
    abnor_meters_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='异常表数量')
    abnor_meters_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='异常表数量_old')
    abnor_meters_num_change = models.CharField(null=True, blank=True, verbose_name='异常表数量_变化值', max_length=20)
    abnor_meters_num_change_status = models.CharField(null=True, blank=True, verbose_name='异常表数量_对比结果', max_length=20)
    meter_com_rate_num = models.DecimalField(null=True, blank=True, default=0, verbose_name='电能表可算率', max_digits=4,
                                             decimal_places=2)
    meter_com_rate_num_old = models.DecimalField(null=True, blank=True, default=0, verbose_name='电能表可算率_old',
                                                 max_digits=4, decimal_places=2)
    meter_com_rate_num_change = models.DecimalField(null=True, blank=True, verbose_name='电能表可算率_变化值', max_digits=4,
                                                    decimal_places=2)
    meter_com_rate_num_change_status = models.CharField(null=True, blank=True, verbose_name='电能表可算率_对比结果',
                                                        max_length=20)
    un_govern_question_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='待治理问题数')
    un_govern_question_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='待治理问题数_old')
    un_govern_question_num_change = models.CharField(null=True, blank=True, verbose_name='待治理问题数_变化值', max_length=20)
    un_govern_question_num_change_status = models.CharField(null=True, blank=True, verbose_name='待治理问题数_对比结果',
                                                            max_length=20)
    cal_tgs_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='可计算台区')
    cal_tgs_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='可计算台区_old')
    cal_tgs_num_change = models.CharField(null=True, blank=True, verbose_name='可计算台区_变化值', max_length=20)
    cal_tgs_num_change_status = models.CharField(null=True, blank=True, verbose_name='可计算台区_对比结果', max_length=20)
    un_govern_tgs_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='待治理台区')
    un_govern_tgs_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='待治理台区_old')
    un_govern_tgs_num_change = models.CharField(null=True, blank=True, verbose_name='待治理台区_变化值', max_length=20)
    un_govern_tgs_num_change_status = models.CharField(null=True, blank=True, verbose_name='待治理台区_对比结果', max_length=20)
    involve_meters_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='涉及电能表')
    involve_meters_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='涉及电能表_old')
    involve_meters_num_change = models.CharField(null=True, blank=True, verbose_name='涉及电能表_变化值', max_length=20)
    involve_meters_num_change_status = models.CharField(null=True, blank=True, verbose_name='涉及电能表_对比结果', max_length=20)
    white_tgs_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='白名单台区')
    white_tgs_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='白名单台区_old')
    white_tgs_num_change = models.CharField(null=True, blank=True, verbose_name='白名单台区_变化值', max_length=20)
    white_tgs_num_change_status = models.CharField(null=True, blank=True, verbose_name='白名单台区_对比结果', max_length=20)
    all_abnor_tgs_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='累计异常台区')
    all_abnor_tgs_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='累计异常台区_old')
    all_abnor_tgs_num_change = models.CharField(null=True, blank=True, verbose_name='累计异常台区_变化值', max_length=20)
    all_abnor_tgs_num_change_status = models.CharField(null=True, blank=True, verbose_name='累计异常台区_对比结果', max_length=20)
    abnor_tg_govern_rate_num = models.DecimalField(null=True, blank=True, default=0, verbose_name='累计异常台区治理率',
                                                   max_digits=4, decimal_places=2)
    abnor_tg_govern_rate_num_old = models.DecimalField(null=True, blank=True, default=0, verbose_name='累计异常台区治理率_old',
                                                       max_digits=4,
                                                       decimal_places=2)
    abnor_tg_govern_rate_num_change = models.DecimalField(null=True, blank=True, verbose_name='累计异常台区治理率_变化值',
                                                          max_digits=4, decimal_places=2)
    abnor_tg_govern_rate_num_change_status = models.CharField(null=True, blank=True, verbose_name='累计异常台区治理率_对比结果',
                                                              max_length=20)
    all_questions_num = models.IntegerField(null=True, blank=True, default=0, verbose_name='累计数据问题')
    all_questions_num_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='累计数据问题_old')
    all_questions_num_change = models.CharField(null=True, blank=True, verbose_name='累计数据问题_变化值', max_length=20)
    all_questions_num_change_status = models.CharField(null=True, blank=True, verbose_name='累计数据问题_对比结果', max_length=20)
    questions_govern_rate = models.DecimalField(null=True, blank=True, default=0, verbose_name='累计数据问题治理率',
                                                max_digits=4, decimal_places=2)
    questions_govern_rate_old = models.DecimalField(null=True, blank=True, default=0, verbose_name='累计数据问题治理率_old',
                                                    max_digits=4,
                                                    decimal_places=2)
    questions_govern_rate_change = models.DecimalField(null=True, blank=True, verbose_name='累计数据问题治理率_变化值',
                                                       max_digits=4, decimal_places=2)
    questions_govern_rate_change_status = models.CharField(null=True, blank=True, verbose_name='累计数据问题治理率_对比结果',
                                                           max_length=20)
    precompute_time = models.CharField(null=True, blank=True, default=0, verbose_name='预计算用时', max_length=20)
    precompute_time_old = models.CharField(null=True, blank=True, default=0, verbose_name='预计算用时_old', max_length=20)
    precompute_time_change = models.CharField(null=True, blank=True, verbose_name='预计算用时_变化值', max_length=20)
    precompute_time_change_status = models.CharField(null=True, blank=True, verbose_name='预计算用时_对比结果', max_length=20)
    over_meters = models.IntegerField(null=True, blank=True, default=0, verbose_name='评价异常电能表')
    over_meters_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='评价异常电能表_old')
    over_meters_change = models.CharField(null=True, blank=True, verbose_name='评价异常电能表_变化值', max_length=20)
    over_meters_change_status = models.CharField(null=True, blank=True, verbose_name='评价异常电能表_对比结果', max_length=20)
    check_meter_num_model = models.IntegerField(null=True, blank=True, default=0, verbose_name='模型输出工单')
    check_meter_num_model_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='模型输出工单_old')
    check_meter_num_model_change = models.CharField(null=True, blank=True, verbose_name='模型输出工单_变化值', max_length=20)
    check_meter_num_model_change_status = models.CharField(null=True, blank=True, verbose_name='模型输出工单_对比结果',
                                                           max_length=20)
    check_meter_num_sz = models.IntegerField(null=True, blank=True, default=0, verbose_name='失准输出工单')
    check_meter_num_sz_old = models.IntegerField(null=True, blank=True, default=0, verbose_name='失准输出工单_old')
    check_meter_num_sz_change = models.CharField(null=True, blank=True, verbose_name='失准输出工单_变化值', max_length=20)
    check_meter_num_sz_change_status = models.CharField(null=True, blank=True, verbose_name='失准输出工单_对比结果',
                                                        max_length=20)
    container_version = models.CharField(verbose_name='新版', max_length=20)
    container_version_old = models.CharField(verbose_name='旧版', max_length=20)
    cal_date = models.DateField(null=False, verbose_name='计算日期')
    cal_date_old = models.DateField(null=False, verbose_name='计算日期_old')

    class Meta:
        db_table = 'vital_data'  # 指明数据库表名
        verbose_name = '重点数据对比'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tg_num

# Create your models here.
