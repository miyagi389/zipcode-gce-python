# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

from google.appengine.ext import ndb

from app.api_messages import ZipCodeResponseMessage


class ZipCode(ndb.Model):
    """Model to store scores that have been inserted by users.

    Since the played property is auto_now_add=True, Scores will document when
    they were inserted immediately after being stored.
    """
    jis_code = ndb.StringProperty(
            required=True,
            verbose_name=u"全国地方公共団体コード(JIS X0401、X0402)"
    )

    old_code = ndb.StringProperty(
            required=True,
            verbose_name=u"郵便番号(旧)"
    )

    code = ndb.StringProperty(
            required=True,
            verbose_name=u"郵便番号(新",
            indexed=True
    )

    prefecture_kana = ndb.StringProperty(
            required=True,
            verbose_name=u"都道府県名(カナ)"
    )

    city_kana = ndb.StringProperty(
            required=True,
            verbose_name=u"市区町村名(カナ)"
    )

    town_kana = ndb.StringProperty(
            required=True,
            verbose_name=u"町域名(カナ)"
    )

    prefecture = ndb.StringProperty(
            required=True,
            verbose_name=u"都道府県名"
    )

    city = ndb.StringProperty(
            required=True,
            verbose_name=u"市区町村名"
    )

    town = ndb.StringProperty(
            required=True,
            verbose_name=u"町域名"
    )

    town_divide = ndb.IntegerProperty(
            required=True,
            verbose_name=u"一町域が二以上の郵便番号で表される場合の表示。1:該当、0:該当せず"
    )

    koaza_banchi = ndb.IntegerProperty(
            required=True,
            verbose_name=u"小字毎に番地が起番されている町域の表示。1:該当、0:該当せず"
    )

    tyoume = ndb.IntegerProperty(
            required=True,
            verbose_name=u"丁目を有する町域の場合の表示。1:該当、0:該当せず"
    )

    has_some_town = ndb.IntegerProperty(
            required=True,
            verbose_name=u"一つの郵便番号で二以上の町域を表す場合の表示。1:該当、0:該当せず"
    )

    update_state = ndb.IntegerProperty(
            required=True,
            verbose_name=u"更新の表示。0:変更なし、1:変更あり、2:廃止(廃止データのみ使用)"
    )

    update_reason = ndb.IntegerProperty(
            required=True,
            verbose_name=u"変更理由。0:変更なし、1:市政・区政・町政・分区・政令指定都市施行、2:住居表示の実施、3:区画整理、4:郵便区調整等、5:訂正、6:廃止(廃止データのみ使用)"
    )

    def to_message(self):
        """Turns the ZipCode entity into a ProtoRPC object.

        :rtype: app.api_messages.ZipCodeResponseMessage
        :return:
        """
        return ZipCodeResponseMessage(
                jis_code=self.jis_code,
                old_code=self.old_code,
                code=self.code,
                prefecture_kana=self.prefecture_kana,
                city_kana=self.city_kana,
                town_kana=self.town_kana,
                prefecture=self.prefecture,
                city=self.city_kana,
                town=self.town,
                town_divide=self.town_divide,
                koaza_banchi=self.koaza_banchi,
                tyoume=self.tyoume,
                has_some_town=self.has_some_town,
                update_state=self.update_state,
                update_reason=self.update_reason
        )

    @classmethod
    def query_all(cls, q = None):
        return cls.query().order(cls.code)

    @classmethod
    def query_code(cls, code = None):
        """
        :type code: str
        :param code: ZIP code. 前方一致検索
        :rtype: ZipCode
        :return: 検索結果
        """
        if code is None:
            query = cls.query()
        else:
            query = cls.query(cls.code >= code, cls.code < code + u'\ufffd')

        # if code is not None:
        #     query = query.filter('code >=', code).filter('code <', code + u'\ufffd')
        query = query.order(cls.code)
        return query
