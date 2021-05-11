### 打造本地k8s终端

前置步骤：本地安装docker [官方网站](https://www.docker.com/get-started)

---

1. 安装kube命令行提示插
   
   [kube-ps1项目地址](https://github.com/jonmosco/kube-ps1)
    ```bash
    > brew install kube-ps1
    > vim ~/.zshrc
    # 在.zshrc中添加以下内容 
    source /path/to/kube-ps1.sh
    PROMPT='$(kube_ps1)'$PROMPT
    ```
<br/>

 2. 安装kubectx增强工具

    [kubectx项目地址](https://github.com/ahmetb/kubectx)
    ```bash
    > brew install kubectx
    ```
<br/>

3. 为常用命令配置别名
    ```bash
    > vim ~/.zshrc
    # 在.zshrc中添加以下内容 
    alias k=kubectl
    alias kctx=kubectx # 切换集群
    alias kon=kubeon
    alias koff=kubeoff
    
    function log_pod() {
    kubectl logs $@;
    }
    alias kl=log_pod
    
    function log_pod_f() {
    kubectl logs -f $@;
    }
    alias klf=log_pod_f
    
    function list_pod() {
    if [ -z $@ ]
    then
    kubectl get pods;
    else
    kubectl get pods | grep $@;
    fi
    }
    alias kgp=list_pod # 列出当前命名空间下所有pod，支持正则
    
    function exec_pod() {
    kubectl exec -it $@ -- sh;
    }
    alias kec=exec_pod # 进入pod
    
    function switch_context() {
    kubectl config set-context --current --namespace="$@";
    }
    alias kns=switch_context # 切换命名空间
    
    export KUBECONFIG=:~/.kube/config
    ```