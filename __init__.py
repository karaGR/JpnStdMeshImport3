# -*- coding: utf-8 -*-

#===================================
#標準地域メッシュコードインポートプラグイン
#QGS3.0に対応
#===================================

def classFactory(iface):
    from .main import main
    return main(iface)