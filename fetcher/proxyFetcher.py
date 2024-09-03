# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     proxyFetcher
   Description :
   Author :        JHao
   date：          2016/11/25
-------------------------------------------------
   Change Activity:
                   2016/11/25: proxyFetcher
-------------------------------------------------
"""
__author__ = 'JHao'

import re
import urllib
import urllib.parse
from datetime import datetime
from time import sleep

from util.webRequest import WebRequest
from playwright.sync_api import sync_playwright

class ProxyFetcher(object):
    """
    proxy getter
    """

    @staticmethod
    def freeProxy01():
        '''
        站大爷 https://www.zdaye.com/free/
        问题很多，估计反爬或者网站不稳定
        '''
        url = 'https://www.zdaye.com/free/'

        # 第一页
        r = WebRequest().get(url, timeout=10)
        proxies = re.findall(r'<tr>\s*<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>\s*<td>(\d+)</td>', r.text)
        yield from [':'.join(proxy) for proxy in proxies]
        
        # 后面几页
        pages = re.findall(r'\s+href=\"/free/(\d+)/\"', r.text)
        pages = list(dict.fromkeys(pages))
        for page in pages:
            page_url = urllib.parse.urljoin(url, page)
            sleep(5)
            r = WebRequest().get(page_url, timeout=10)
            proxies = re.findall(r'<tr>\s*<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>\s*<td>(\d+)</td>', r.text)
            yield from [':'.join(proxy) for proxy in proxies]

    @staticmethod
    def freeProxy02():
        """ 开心代理 http://www.kxdaili.com """
        urls = ["http://www.kxdaili.com/dailiip.html", "http://www.kxdaili.com/dailiip/2/1.html"]
        for url in urls:
            r = WebRequest().get(url)
            proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
            yield from [':'.join(proxy) for proxy in proxies]
            
            more_urls = re.findall(r'<a\s+href=\"(/dailiip/\d+/\d+.html)\">\d+</a>', r.text)
            more_urls = [urllib.parse.urljoin(url, more_url) for more_url in more_urls]
            for more_url in more_urls:
                sleep(1)
                r = WebRequest().get(more_url)
                proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
                yield from [':'.join(proxy) for proxy in proxies]

    @staticmethod
    def freeProxy03():
        """ 快代理 https://www.kuaidaili.com """
        categories = ['inha', 'intr', 'fps', 'dps']
        for category in categories:
            max_page = 1
            page = 1
            while page <= max_page:
                url = f'https://www.kuaidaili.com/free/{category}/{page}'
                sleep(5)
                r = WebRequest().get(url, timeout=10)
                proxies = re.findall(r'\"ip\":\s+\"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\",\s+\"last_check_time\":\s+\"[\d\-\s\:]+\",\s+\"port\"\:\s+\"(\d+)\"', r.text)
                yield from [':'.join(proxy) for proxy in proxies]
                
                total = re.findall(r'let\s+totalCount\s\=\s+[\'\"](\d+)[\'\"]', r.text)[0]
                max_page = min(int(total)/12, 10)
                page += 1

    @staticmethod
    def freeProxy04():
        """ 云代理 http://www.ip3366.net"""
        stypes = ('1', '2')
        for stype in stypes:
            url = f'http://www.ip3366.net/free/?stype={stype}'
            r = WebRequest().get(url, timeout=10)
            proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
            for proxy in proxies:
                yield ":".join(proxy)
            
            pages = re.findall(r'<a\s+href=\"\?stype=[12]&page=(\d+)\">\d+</a>', r.text)
            for page in pages:
                url = f'http://www.ip3366.net/free/?stype={stype}&page={page}'
                sleep(1)
                r = WebRequest().get(url, timeout=10)
                proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
                yield from [':'.join(proxy) for proxy in proxies]

    @staticmethod
    def freeProxy05():
        """ 小幻代理 https://ip.ihuan.me """
        now = datetime.now()
        url = f'https://ip.ihuan.me/today/{now.year}/{now.month:02}/{now.day:02}/{now.hour:02}.html'
        r = WebRequest().get(url, timeout=10)
        proxies = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)', r.text)
        yield from [':'.join(proxy) for proxy in proxies]

    @staticmethod
    def freeProxy06():
        """ 89免费代理 https://www.89ip.cn/ """
        urls = ['https://www.89ip.cn/']
        while True:
            try:
                url = urls.pop()
            except IndexError:
                break

            r = WebRequest().get(url, timeout=10)
            proxies = re.findall(
                r'<td.*?>[\s\S]*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})[\s\S]*?</td>[\s\S]*?<td.*?>[\s\S]*?(\d+)[\s\S]*?</td>',
                r.text)
            if not proxies:
                # 没了
                break

            yield from [':'.join(proxy) for proxy in proxies]

            # 下一页
            r = re.findall(r'<a\s+href=\"(index_\d+.html)\"\s+class=\"layui-laypage-next\"\s+data-page=\"\d+\">下一页</a>', r.text)
            if r:
                next_url = urllib.parse.urljoin(url, r[0])
                urls.append(next_url)
                sleep(1)


    @staticmethod
    def freeProxy07():
        """ 稻壳代理 https://www.docip.net/ """
        r = WebRequest().get("https://www.docip.net/data/free.json", timeout=10)
        try:
            for each in r.json['data']:
                yield each['ip']
        except Exception as e:
            print(e)

    '''被防火墙拦截'''
    @staticmethod
    def freeProxy08():
        """ https://proxy-list.org/english/index.php """
        with sync_playwright() as p:
            for i in range(1, 11):
                sleep(2)
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto(f'https://proxy-list.org/chinese/index.php?setlang=chinese&p={i}')
                html_content = page.content()
                proxies = re.findall(r'<li class="proxy"><script type="text/javascript">.*</script>(.*)</li>', html_content)
                for proxy in proxies:
                    yield proxy
                browser.close()

    @staticmethod
    def freeProxy09():
        urls = ['https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-%s' % n for n in range(1, 7)]
        request = WebRequest()
        for url in urls:
            r = request.get(url, timeout=10)
            proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
            for proxy in proxies:
                yield ':'.join(proxy)

    @staticmethod
    def freeProxy10():
        url = 'https://gh-proxy.com/https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.json'
        r = WebRequest().get(url, timeout=10)
        proxies = [f'{proxy["ip"]}:{proxy["port"]}' for proxy in  r.json]
        yield from proxies
    
    @staticmethod
    def freeProxy11():
        url = 'https://gh-proxy.com/https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt'
        r = WebRequest().get(url, timeout=10)
        proxies = [proxy for proxy in r.text.split('\n') if proxy]
        yield from proxies
    
    @staticmethod
    def freeProxy12():
        url = 'https://sunny9577.github.io/proxy-scraper/proxies.json'
        r = WebRequest().get(url, timeout=10)
        proxies = [f'{proxy["ip"]}:{proxy["port"]}' for proxy in  r.json]
        yield from proxies
    
    @staticmethod
    def freeProxy13():
        urls = ['https://gh-proxy.com/https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt', 'https://gh-proxy.com/https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt']
        for url in urls:
            r = WebRequest().get(url, timeout=10)
            proxies = [':'.join(proxy.split(':')[:2]) for proxy in r.text.split('\n') if proxy]
            yield from proxies
    
    @staticmethod
    def freeProxy14():
        for i in range(1, 70):
            url = f'https://iproyal.com/free-proxy-list/?page={i}&entries=100'
            sleep(2)
            r = WebRequest().get(url, timeout=10)
            proxies = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</div><div class=\"flex items-center astro-lmapxigl\">(\d+)</div><div class=\"flex items-center astro-lmapxigl\">(https?)</div>', r.text)
            yield from [':'.join(proxy[:2]) for proxy in proxies]
    
    '''不知道有没有用，先保留'''
    @staticmethod
    def freeProxy15():
        urls = ['http://pubproxy.com/api/proxy?limit=5&https=true', 'http://pubproxy.com/api/proxy?limit=5&https=false']
        proxies = set()
        for url in urls:
            for _ in range(10):
                sleep(1)
                r = WebRequest().get(url, timeout=10)
                for proxy in [proxy['ipPort'] for proxy in r.json['data']]:
                    if proxy in proxies:
                        continue
                    yield proxy
                    proxies.add(proxy)
    
    @staticmethod
    def freeProxy16():
        urls = ['https://freeproxylist.cc/servers/']
        while True:
            try:
                url = urls.pop()
            except IndexError:
                break

            r = WebRequest().get(url, timeout=10)
            proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
            yield from [':'.join(proxy) for proxy in proxies]

            r = re.findall(r'''<a\s+href='(https://freeproxylist\.cc/servers/\d+\.html)'>&raquo;</a></li>''', r.text)
            if r:
                urls.append(r[0])
                sleep(1)
    
    @staticmethod
    def freeProxy17():
        url = 'https://hasdata.com/free-proxy-list'
        r = WebRequest().get(url, timeout=10)
        proxies = re.findall(r'<tr><td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d+)</td><td>HTTP', r.text)
        yield from [':'.join(proxy) for proxy in proxies]

    @staticmethod
    def freeProxy18():
        '''
        这个网址不可用，先删了
        https://www.freeproxy.world/?type=https&anonymity=&country=&speed=&port=&page=1
        '''
        urls = ['https://www.freeproxy.world/?type=http&anonymity=&country=&speed=&port=&page=%s' % n for n in range(1, 90)]
        for url in urls:
            r = WebRequest().get(url, timeout=10)
            proxies = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*</td>\s*<td>\s*<a href=\"/\?port=\d+\">(\d+)</a>', r.text)
            yield from [':'.join(proxy) for proxy in proxies]

    '''被防火墙拦截'''
    @staticmethod
    def freeProxy19():
        url = 'https://free-proxy-list.net/'
        r = WebRequest().get(url, timeout=10)
        proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d+)</td>', r.text)
        yield from [':'.join(proxy) for proxy in proxies]

    @staticmethod
    def freeProxy20():
        '''Proxy Site List https://proxysitelist.net/'''
        url = 'https://proxysitelist.net/'
        r = WebRequest().get(url, timeout=10)
        proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d+)</td><td>([a-zA-Z]+)</td>', r.text)
        for proxy in proxies:
            ip, port, protocol = proxy
            if protocol.startswith('Http') or protocol.startswith('Https'):
                yield f"{ip}:{port}"

    '''有cf盾，待研究'''
    @staticmethod
    def freeProxy21():
        url = "https://hide.mn/cn/proxy-list/#list"
        r = WebRequest().get(url, timeout=10)
        proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d+)</td>', r.text)
        yield from [':'.join(proxy) for proxy in proxies]
        # 后面几页
        # 换页有cf盾
        #for i in range(1, 198):
        #    turl = f"https://hide.mn/en/proxy-list/?start={64 * i}#list";
        #    sleep(5)
        #    r = WebRequest().get(turl, timeout=10)
        #    proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d+)</td>', r.text)
        #    yield from [':'.join(proxy) for proxy in proxies]
    
    '''被防火墙拦截'''
    @staticmethod
    def freeProxy22():
        url = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&proxy_format=protocolipport&format=json"
        r = WebRequest().get(url, timeout=10)
        proxies = [f'{proxy["ip"]}:{proxy["port"]}' for proxy in r.json["proxies"]]
        for proxy in proxies:
            yield proxy


if __name__ == '__main__':
    p = ProxyFetcher()
    for _ in p.freeProxy01():
        print(_)
