from django.db import models


class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题", max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10,
                                  decimal_places=2, default=0)
    create_time = models.DateField(verbose_name="入职时间")
    # to:关联的表
    # to_field：关联的表的列
    # department字段在表中所生成的列为department_id
    # 当员工表删除时，所在部门下的其他员工部门id删除
    department = models.ForeignKey(verbose_name="部门", to='Department',
                                   to_field='id',
                                   on_delete=models.CASCADE)
    # # 当员工表删除时，所在部门下的其他员工部门id置空
    # department = models.ForeignKey(to='Department', to_field='id',
    #                                on_delete=models.SET_NULL, null=True,
    #                                blank=True)
    gender_choices = ((1, "男"), (2, "女"))
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


class PrettyNum(models.Model):
    """靓号表"""
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    price = models.IntegerField(verbose_name="价格", default=0)
    level_choices = ((1, "1级"), (2, "2级"), (3, "3级"), (4, "4级"))
    level = models.SmallIntegerField(verbose_name="级别",
                                     choices=level_choices, default=1)
    status_choices = ((1, "已占用"), (2, "未占用"))
    status = models.SmallIntegerField(verbose_name="状态",
                                      choices=status_choices, default=2)


class Admin(models.Model):
    """管理员表"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username


class Task(models.Model):
    """任务"""
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")
    level_choices = ((1, "紧急"), (2, "重要"), (3, "临时"))
    level = models.SmallIntegerField(verbose_name="级别",
                                     choices=level_choices, default=1)
    user = models.ForeignKey(verbose_name="负责人", to="Admin",
                             on_delete=models.CASCADE)


class Order(models.Model):
    """订单"""
    oid = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")
    status_choices = (
        (1, "待支付"),
        (2, "已支付"),
    )
    status = models.SmallIntegerField(verbose_name="状态",
                                      choices=status_choices, default=1)
    admin = models.ForeignKey(verbose_name="管理员", to="Admin",
                              on_delete=models.CASCADE)


class Boss(models.Model):
    """老板"""
    name = models.CharField(verbose_name="姓名", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    img = models.CharField(verbose_name="头像", max_length=120)


class City(models.Model):
    """城市"""
    name = models.CharField(verbose_name="姓名", max_length=32)
    count = models.IntegerField(verbose_name="人口")
    # 此时上传的文件可以自动保存
    img = models.FileField(verbose_name="Logo", max_length=120,
                           upload_to='city/')
# Create your models here.
