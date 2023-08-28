# 1.基本配置

## 1.1 安装django

```
`pip install django`
```

## 1.2 创建django项目

```
django-admin startproject 项目名
```

若用pycharm创建，记得删除settings.py中的DIRS TEMPLATES中的内容

## 1.3 创建app

```
python manage.py startapp 应用名
```

app创建完成后要记得在settings.py中的INSTALLED_APPS中注册

## 1.4 静态文件配置和模板路径

## 1.5 数据库配置

### 1.5.1安装mysqlclient

```
pip install mysqlclient
```

### 1.5.2 创建数据库

### 1.5.3 settings.py中配置数据库

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "gx_day16",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }}
```

### 1.5.4 编写model类

```
from django.db import models


class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题", max_length=32)

    def __str__(self):
        return self.title
```

### 1.5.5 数据迁移

```
python manage.py makemigrations

python manage.py migrate
```

## 1.6 路由配置

在urls.py中进行路由配置(url和视图函数的映射关系)

## 1.7 编写视图函数

在views.py，视图函数，业务逻辑编写

## 1.8 模板渲染

模板语法

继承

引用静态文件

ModelForm和Form组件(自动生成HTML标签、请求数据校验、保存数据库、获取错误信息)

## 1.9 cookie和session

登录用户信息保存

## 1.10 中间件

## 1.11分页

# 2. orm操作

## 2.1 查询

```
models.PrettyNum.objects.filter(mobile="15389745567", id=1)
```

等价于

```
data_dict = {"mobile": "15389745567", "id": 1}
models.PrettyNum.objects.filter(**data_dict)
```

```
`models.PrettyNum.objects.filter(mobile__contains="15389745", id=1)`
```

等价于

```
data_dict = {"mobile__contains": "15389745", "id": 1}
models.PrettyNum.objects.filter(**data_dict)
```

### 2.1.1 数字相关

#### 2.1.1.1 等于

```
models.PrettyNum.objects.filter(id=1)
```

#### 2.1.1.2 大于

```
models.PrettyNum.objects.filter(id__gt=1)
```

#### 2.1.1.3 大于等于

```
models.PrettyNum.objects.filter(id__gte=1)
```

#### 2.1.1.4 小于

```
models.PrettyNum.objects.filter(id__lt=1)
```

#### 2.1.1.5 小于等于

```
models.PrettyNum.objects.filter(id__lte=1)
```

### 2.1.2 字符串相关

#### 2.1.2.1 精准匹配

`models.PrettyNum.objects.filter(mobile="15389745567")`

#### 2.1.2.2 包含

```
models.PrettyNum.objects.filter(mobile__contains="6")
```

#### 2.1.2.3 以字符结尾

```
models.PrettyNum.objects.filter(mobile__endswith="6")
```

#### 2.1.2.4 以字符开头

```
models.PrettyNum.objects.filter(mobile__startswith="6")
```

### 2.1.3 获取所有数据

```
models.PrettyNum.objects.filter(id=1).all()
```

### 2.1.4 获取第一条数据

```
models.PrettyNum.objects.filter(id=1).first()
```

## 2.2 values()的使用

用于获取特定的列所用，结果为字典

```
models.Order.objects.filter(id=uid).values("title",'status', "price").first()
```

result:

```
{'title': '礼服', 'status': 2, 'price': 400}
```



```
a=models.Order.objects.all().values("title",'status', "price")
print(a)
print(a[0])
```

result:

```
<QuerySet [{'title': '礼服', 'status': 2, 'price': 400}, {'title': '书籍', 'status': 1, 'price': 325}, {'title': '洗发水', 'status': 1, 'price': 28}, {'title': '打印纸', 'status': 1, 'price': 49}, {'title': '羽毛球', 'status': 2, 'price': 68}, {'title': '外卖', 'status': 1, 'price': 15}, {'title': '手机', 'status': 2, 'price': 2999}, {'title': '试卷', 'status': 2, 'price': 14}, {'title': '火龙果', 'status': 2, 'price': 26}, {'title': '奶茶', 'status': 1, 'price': 8}, {'title': '伞', 'status': 2, 'price': 18}, {'title': '衣服', 'status': 1, 'price': 175}]>
{'title': '礼服', 'status': 2, 'price': 400}
```

## 2.3 values_list()的使用

用于获取特定的列所用，结果为元组

```
b=models.Order.objects.all().values_list("title",'status', "price")
print(b)
print(b[0])
```

result:

```
<QuerySet [('礼服', 2, 400), ('书籍', 1, 325), ('洗发水', 1, 28), ('打印纸', 1, 49), ('羽毛球', 2, 68), ('外卖', 1, 15), ('手机', 2, 2999), ('试卷', 2, 14), ('火龙果', 2, 26), ('奶茶', 1, 8), ('伞', 2, 18), ('衣服', 1, 175)]>
('礼服', 2, 400)
```

## 2.4 新增数据

```
models.UserInfo.objects.create(name=“wupeiqi”, pwd='123', age=19,
                               email='xxx@live.com')
```

等价于

```
models.UserInfo.objects.create(**{“name“:“wupeiqi”, “pwd“:'123', “age“:19,
                              “email“:'xxx@live.com'})
```

## 2.5 删除

```
models.PrettyNum.objects.all().delete()
models.PrettyNum.objects.filter(mobile__endswith="6").delete()
```

## 2.6 修改

```
models.UserInfo.objects.all().update(age=19)
models.PrettyNum.objects.filter(id=10).update(mobile="11111111")
```