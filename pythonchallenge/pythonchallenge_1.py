in_tab = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
out_tab = "c d e f g h i j k l m n o p q r s t u v w x y z a b"
tran_tab = str.maketrans(in_tab, out_tab)
s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb " \
       "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(s.translate(tran_tab))
