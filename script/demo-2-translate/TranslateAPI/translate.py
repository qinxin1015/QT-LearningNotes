import re
import requests


class Translate:
    """
        >>> b = Translate()
        >>> b.translate("add a button")
        '添加按钮'
    """

    def __init__(self):

        headers = {
            'Cookie': 'BIDUPSID=231955F6F7B8CDE571A430E352A51DE4; PSTM=1598755049; '
                      'BAIDUID=231955F6F7B8CDE5389C32E219DE2CD1:FG=1; REALTIME_TRAN'
                      'S_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD'
                      '_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=U9XdVB3M0ZkdkRTLUhDY'
                      'k9hVk9ESS1PdDhqSzhGVjE0RnNZeFgwc1czNFVxajlnRVFBQUFBJCQAAAAAA'
                      'AAAAAEAAADd2hsDemx5NzE3MjE2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                      'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQdGGAUHRhgQ; BDUSS_'
                      'BFESS=U9XdVB3M0ZkdkRTLUhDYk9hVk9ESS1PdDhqSzhGVjE0RnNZeFgwc1c'
                      'zNFVxajlnRVFBQUFBJCQAAAAAAAAAAAEAAADd2hsDemx5NzE3MjE2AAAAAAA'
                      'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                      'AAAAAABQdGGAUHRhgQ; __yjs_duid=1_0c47b7317b6524a3b8416372a06'
                      'f3eeb1613655493923; BAIDUID_BFESS=809941277758E5FD2DAF021DA2'
                      '50F489:FG=1; BDRCVFR[sIY70V9lLzm]=9xWipS8B-FspA7EnHc1QhPEUf;'
                      ' delPer=0; PSINO=7; BCLID=11337131384018520836; BDSFRCVID=uY'
                      '-OJeC629I97jQebwKEesbzZ70QdKbTH6aoPAoBfj1YE2tHqk9eEG0P_x8g0K'
                      'AbKGwbogKKLmOTHpuF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF'
                      '=tJPj_CKaJIL3eJ3pht__KJoH-UnLqbQkHmOZ0l8KtDTzbD3F0toD5UPkbqb'
                      'ahqIftN6babomWIQHDUJqhU5tM6_4QH5JBnoWfCT4KKJxX-PWeIJoLt5vQn-'
                      'VhUJiBM7LBan7QP5IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbRO4-TF'
                      '5DTvbjU5; BCLID_BFESS=11337131384018520836; BDSFRCVID_BFESS='
                      'uY-OJeC629I97jQebwKEesbzZ70QdKbTH6aoPAoBfj1YE2tHqk9eEG0P_x8g'
                      '0KAbKGwbogKKLmOTHpuF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_'
                      'SF_BFESS=tJPj_CKaJIL3eJ3pht__KJoH-UnLqbQkHmOZ0l8KtDTzbD3F0to'
                      'D5UPkbqbahqIftN6babomWIQHDUJqhU5tM6_4QH5JBnoWfCT4KKJxX-PWeIJ'
                      'oLt5vQn-VhUJiBM7LBan7QP5IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnL'
                      'hbRO4-TF5DTvbjU5; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDRCVF'
                      'R[C0p6oIjvx-c]=I67x6TjHwwYf0; BDORZ=B490B5EBF6F3CD402E515D22'
                      'BCDA1598; H_PS_PSSID=33517_33260_33272_31660_33594_26350_332'
                      '64; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1613655494,16137'
                      '45551,1613784460,1614227695; Hm_lpvt_64ecd82404c51e03dc91cb9'
                      'e8c025574=1614227695; ab_sr=1.0.0_MTg3ZWY3NjY4NzU2ZWEwNTlkZT'
                      'RjNmFhM2E2ZDIyZTI0OTBiNWYzNzYyN2RjNDc2NTk5YTY5MDljZjllODBhNz'
                      'FiYWY4ZWRiMTc1NGJmMDkzMDk0ZmJiNjg3ODE3ZjY5; __yjsv5_shitong='
                      '1.0_7_fddeb8c526787188f2d26e917d00b1ce2f41_300_1614227716151'
                      '_36.148.68.217_29cf29d4',
            'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/53'
                          '7.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }

        # 创建session实例，用于发送请求
        self.session = requests.session()
        self.session.headers = headers

        self._token = self.token()

    def translate(self, w):
        """
            w: The words or sentences you are going to translate
            return: The result of translation
        """

        url = 'https://fanyi.baidu.com/v2transapi'

        _from = self.lan(w)

        # 英译汉，汉译英
        if _from == 'zh':
            params = {'from': 'zh', 'to': 'en'}
        elif _from == 'en':
            params = {'from': 'en', 'to': 'zh'}
        else:
            params = {}

        data = {
            'query': w,
            'sign': self.sign(w),
            'token': self._token,
        }

        res = self.session.post(url, data, params=params)

        # 判断一下，是否拿到正确的数据，增强容错性
        if res.json().get('trans_result'):
            return res.json()['trans_result']['data'][0]['dst']
        else:
            return "请输入合法的单词或语句"

    def lan(self, w):
        """自动检测语言种类"""

        url = 'https://fanyi.baidu.com/langdetect'

        res = self.session.post(url, {'query': w})

        # 如果检测不到，就当成英语语种
        if res.json().get('lan'):
            return res.json().get('lan')
        else:
            return "en"

    def token(self):
        """获取token参数"""

        url = 'https://fanyi.baidu.com'
        res = self.session.get(url)

        t = re.findall("token: '(.*?)',", res.text)

        return t[0] if t else ""

    def encrypt(self, r, o):
        """sign加密"""

        t = 0
        while t < len(o)-2:
            a = o[t+2]
            a = ord(a[0]) - 87 if a >= "a" else int(a)
            a = r >> a if "+" == o[t+1] else r << a
            r = r + a & 4294967295 if "+" == o[t] else r ^ a
            t += 3

        return r

    def sign(self, w):
        """获取sign参数"""

        u, m, s, S = "320305.131321201", 320305, 131321201, []

        for v in range(len(w)):
            A = ord(w[v])

            if 128 > A:
                S.append(A)
            else:
                if 2048 > A:
                    S.append(A >> 6 | 192)
                else:
                    if (55296 == (64512 & A)) and (v+1 < len(w)) and (56320 == (64512 & ord(w[v+1]))):
                        v += 1
                        A = 65536 + (1023 & A) << 10 + 1023 & ord(w[v])
                        S.append(A >> 18 | 240)
                        S.append(A >> 12 & 63 | 128)
                    else:
                        S.append(A >> 12 | 224)

                    S.append(A >> 6 & 63 | 128)

                S.append(63 & A | 128)

        p, F, D = m, "+-a^+6", "+-3^+b+-f"

        for b in range(len(S)):
            p += S[b]
            p = self.encrypt(p, F)

        p = int((self.encrypt(p, D) ^ s) % 1e6)

        return str(p) + "." + str(p ^ m)
