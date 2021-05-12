## 场景
做为一名coder, 一定拥有自己的github账号和项目，同时在工作时，可能会额外申请一个github账号加入公司的organization，
为了让不同的项目可以push到不同的账号仓库，此时就需要在本地机器上为每一个github账号配置对应的ssh key，具体步骤如下。

---
### SSH方式

 1. 为每个账号生成密钥对
    ```bash
    > cd ~/.ssh
    > ssh-keygen -t rsa -C "account1@youremail.com"
    > ssh-keygen -t rsa -C "account2@youremail.com"
    # 生成过程可以指定密钥对的文件名，用于区分用途。
    > ls
    id_rsa_account1 id_rsa_account1.pub id_rsa_account2 id_rsa_account2.pub
    ```
<br />

 2. 注册生成的密钥对
    ```bash
    > ssh-add -D # 可以先清空缓存
    > ssh-add ~/.ssh/id_rsa_account1
    > ssh-add ~/.ssh/id_rsa_account2
    ```
<br />
    
 3. 配置ssh config
     ```bash
    > cd ~/.ssh
    > vim config # 如果之前没有配置过，手动创建
    Host account_self # 可以任意起一个名字
        HostName github.com
        IdentityFile ~/.ssh/id_rsa_account1

    Host account_company
        HostName github.com
        IdentityFile ~/.ssh/id_rsa_account2
    ```
<br />

4. 去github配置共钥 
   - 登录github账号 -> Settings -> SSH and GPG keys -> New SSH key
   - 将本地 `~/.ssh/id_rsa_accountX.pub` 公钥内容粘贴进表单并提交

<br /> 

5. 配置仓库
    
     ```bash
    > git clone git@{configed_host}:{remote_user}/{remote_project}.git your_local_project_dir
    ```
<br />


6. 测试验证
   
    ```bash
    # 对本地项目做一些更改
    > git add .
    > git commit -m "your comments"
    > git push
    ```
<br />
