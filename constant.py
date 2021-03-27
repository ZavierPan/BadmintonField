ZHONGZHENG_FIELD_INFO = """
中正活動中心
已被長租之場地 (2021/3/7更新)
週六 8~10 ABC
週六 10~12 AB
週六 14~16 ABC
週日 8~10 ABC
週日 10-12 BC

每周日晚上必搶 周日8~10 D E

# A號場 1112
# B號場 1113
# C號場 1114
# D號場 1115
# E號場 1116
"""

ZHONGZHENG_URL = "https://www.cjcf.com.tw/jj01.aspx"

# [8am, 9am, 10am, 11am]
ZHONGZHENG_FIELD_XPATH_IDs = {'A': [12, 17, 22, 27], 
                            'B': [13, 18, 23, 28],
                            'C': [14, 19, 24, 29],
                            'D': [15, 20, 25, 30],
                            'E': [16, 21, 26, 31]}
ZHONGZHENG_FIELD_ID = {'A': 1112, 
                        'B': 1113,
                        'C': 1114,
                        'D': 1115,
                        'E': 1116}

XINYI_FIELD_INFO = """
信義運動中心
已被長租之場地 (2021/3/13更新)
週六 10~12 ABC
週六 14~16 CD
週六 16~18 CD
週日 10~12 ABC
週日 16-18 B
週日 20-22 BD

每周六晚上必搶 周六10~12 D
每周日晚上必搶 周日10~12 B

# A號場 1140
# B號場 1141
# C號場 1144
# D號場 1145
"""

XINYI_URL = "https://scr.cyc.org.tw/tp04.aspx"

# [8am, 9am, 10am, 11am]
XINYI_FIELD_XPATH_IDs = {'A': [10, 14, 18, 22], 
                            'B': [11, 15, 19, 23],
                            'C': [12, 16, 20, 24],
                            'D': [13, 17, 21, 25]}
XINYI_FIELD_ID = {'A': 1140, 
                        'B': 1141,
                        'C': 1144,
                        'D': 1145}