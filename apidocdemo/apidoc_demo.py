def login():
 """
 @api {POST} /login/ 登录操作
 @apiVersion 0.0.1
 @apiName login
 @apiGroup User
 @apiDescription 这里可以描述一下这个函数的具体操作
 这一行也是可以描述的

 @apiParam {String} name 姓名
 @apiParam {String} password 密码

 @apiSuccess {Object} status 状态码
 @apiSuccess {Object} msg 简略描述

 @apiSuccessExample Response-Success:
     HTTP 1.1/ 200K
     {
         'status': 0,
         'msg': 'success'
     }
 @apiErrorExample Response-Fail:
     HTTP 1.1/ 404K
     {
         'status': 1,
         'msg': 'Fail'
     }
 """
 pass


def index():
 """
 @api {GET} /index/ 主页操作
 @apiVersion 0.0.1
 @apiName index
 @apiGroup User
 @apiDescription 这里可以描述一下这个函数的具体操作
 这一行也是可以描述的

 @apiParam {Data} name 姓名

 @apiSuccess {Object} status 状态码
 @apiSuccess {Object} msg 简略描述

 @apiSuccessExample Response-Success:
     HTTP 1.1/ 200K
     [
         {
             'id': 1,
             'name': '张三'
         }，
         {
             'id': 2,
             'name': '李四'
         },
         {
             'id': 3,
             'name': '王五'
         }
     ]

 @apiErrorExample Response-Fail:
     HTTP 1.1/ 404K
     {
         'status': 1,
         'msg': 'Fail'
     }
 """
 pass