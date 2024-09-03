
ProxyPool 爬虫代理IP池
=======
[![Build Status](https://travis-ci.org/jhao104/proxy_pool.svg?branch=master)](https://travis-ci.org/jhao104/proxy_pool)
[![](https://img.shields.io/badge/Powered%20by-@j_hao104-green.svg)](http://www.spiderpy.cn/blog/)
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg)](https://github.com/jhao104/proxy_pool/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/jhao104/proxy_pool.svg)](https://github.com/jhao104/proxy_pool/graphs/contributors)
[![](https://img.shields.io/badge/language-Python-green.svg)](https://github.com/jhao104/proxy_pool)

    ______                        ______             _
    | ___ \_                      | ___ \           | |
    | |_/ / \__ __   __  _ __   _ | |_/ /___   ___  | |
    |  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | |
    | |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___
    \_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____\
                           __ / /
                          /___ /

### ProxyPool

**爬虫代理IP池项目,主要功能为定时采集网上发布的免费代理验证入库，定时验证入库的代理保证代理的可用性，提供API和CLI两种使用方式。同时你也可以扩展代理源以增加代理池IP的质量和数量。**

**因为获取节点列表站点可能有拦截，如果可以请将此项目部署在海外服务器上**

这是一个修改分支的二次开发仓库, 因为是刚需的产物所以代码是随性写的，如果对命名或者是代码有任何问题的或者是想纠正的可以自行pr！

感谢下面两位大佬：

- 原作者: [jhao104](https://github.com/jhao104/proxy_pool)

- 使用分支: [wencan - dev_20240503_update-proxyfetcher](https://github.com/wencan/proxy_pool/tree/dev_20240503_update-proxyfetcher)

使用教程、开发教程、如何使用等请自行到源仓库进行查看↓

---

* 文档: [document](jhao104.github.io/proxy_pool/)

* 支持版本: [![](https://img.shields.io/badge/Python-3.8-blue.svg)](https://docs.python.org/3.8/)
[![](https://img.shields.io/badge/Python-3.9-blue.svg)](https://docs.python.org/3.9/)
[![](https://img.shields.io/badge/Python-3.10-blue.svg)](https://docs.python.org/3.10/)
[![](https://img.shields.io/badge/Python-3.11-blue.svg)](https://docs.python.org/3.11/)

### 目前代理源 (不严格按照获取顺序排列)

**本人并不会推广或推荐任何的付费代理，也并不会嵌入任何广告，如有需求请自行查看相关测评**

**本人并不保证节点的可用性，请自行在爬虫做好节点检测**

- [站大爷](https://www.zdaye.com/free/)
- [开心代理](http://www.kxdaili.com)
- [快代理](https://www.kuaidaili.com)
- [云代理](http://www.ip3366.net)
- [小幻代理](https://ip.ihuan.me)
- [89免费代理](https://www.89ip.cn/)
- [稻壳代理](https://www.docip.net/)
- [proxy-list.org](https://proxy-list.org/english/index.php)
- [proxylistplus.com](https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1)
- [proxifly - free-proxy-list](https://github.com/proxifly/free-proxy-list)
- [TheSpeedX - PROXY-List](https://github.com/TheSpeedX/PROXY-List)
- [sunny9577 - proxy-scraper](https://github.com/sunny9577/proxy-scraper)
- [zloi-user - hideip.me](https://github.com/zloi-user/hideip.me)
- [iproyal.com](https://iproyal.com/free-proxy-list)
- [pubproxy.com](http://pubproxy.com)
- [freeproxylist.cc](https://freeproxylist.cc/servers/)
- [hasdata.com](https://hasdata.com/free-proxy-list)
- [freeproxy.world](https://www.freeproxy.world/)
- [free-proxy-list.net](https://free-proxy-list.net/)
- [proxysitelist.net](https://proxysitelist.net/)
- [hide.mn](https://hide.mn/cn/proxy-list/#list)
- [proxyscrape.com](proxyscrape.com)

### 使用

* Api

启动web服务后, 默认配置下会开启 http://127.0.0.1:5010 的api接口服务:

#### get

介绍: `随机获取一个代理`

HTTP方法: `GET`

例子链接:

```
# 随机获取一个代理
http://127.0.0.1:5010/get

# 随机获取一个https代理
http://127.0.0.1:5010/get?type=https

# 随机获取一个中国大陆地区的代理
http://127.0.0.1:5010/get?cn

# 随机获取一个在中国大陆地区的https代理
http://127.0.0.1:5010/get?type=https&cn
```

#### pop

介绍: `获取并删除一个代理`

HTTP方法: `GET`

例子链接
```
# 获取并删除一个代理
http://127.0.0.1:5010/pop

# 获取并删除一个https代理
http://127.0.0.1:5010/pop?type=https

# 获取并删除一个中国大陆地区的代理
http://127.0.0.1:5010/pop?cn

# 获取并删除一个在中国大陆地区的https代理
http://127.0.0.1:5010/pop?type=https&cn
```

#### all

介绍: `获取所有代理`

HTTP方法: `GET`

例子链接
```
# 获取所有代理
http://127.0.0.1:5010/all

# 获取所有https代理
http://127.0.0.1:5010/all?type=https

# 获取所有中国大陆地区的代理
http://127.0.0.1:5010/all?cn

# 获取所有在中国大陆地区的https代理
http://127.0.0.1:5010/all?type=https&cn
```

#### count

介绍: `查看代理数量`

HTTP方法: `GET`

例子链接
```
http://127.0.0.1:5010/count
```

#### delete

介绍: `删除代理`

HTTP方法: `GET`

例子链接
```
# 假设代理地址为223.5.5.5
http://127.0.0.1:5010/delete?proxy=223.5.5.5:80
```
