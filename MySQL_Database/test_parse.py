

import sqlparse
c ='-- ----------------------------' + '\n'+ '-- Records of m_blacklist' + '\n' +'-- ----------------------------'


print c
parsed = sqlparse.parse(c, encoding="utf-8")
stmt = parsed[0]
print stmt.tokens
comments = str(stmt.tokens[0])