## 步骤
1、 登录页面发送请求get，获取csrftoken
2、 发送post请求:
	用户名：
	密码：
	csrftoken
	-------获得cookie

3、 在登录页面分析form表单是提交到session了，随便输入一个账号和密码，通过chrom的F12的Network 查看session， 可以看到headers 里面的From data 需要提交的数据，这个数据我们在模拟的时候就是需要提交的
