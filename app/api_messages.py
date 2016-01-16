# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

from protorpc import messages


class ZipCodeResponseMessage(messages.Message):
    u"""ProtoRPC message definition to ZIP code."""

    u"""全国地方公共団体コード(JIS X0401、X0402)"""
    jis_code = messages.StringField(1, required=True)

    u"""郵便番号(旧)"""
    old_code = messages.StringField(2, required=True)

    u"""郵便番号(新)"""
    code = messages.StringField(3, required=True)

    u"""都道府県名(カナ)"""
    prefecture_kana = messages.StringField(4, required=True)

    u"""市区町村名(カナ)"""
    city_kana = messages.StringField(5, required=True)

    u"""町域名(カナ)"""
    town_kana = messages.StringField(6, required=True)

    u"""都道府県名"""
    prefecture = messages.StringField(7, required=True)

    u"""市区町村名"""
    city = messages.StringField(8, required=True)

    u"""町域名"""
    town = messages.StringField(9, required=True)

    u"""一町域が二以上の郵便番号で表される場合の表示。1:該当、0:該当せず"""
    town_divide = messages.IntegerField(10, required=True)

    u"""小字毎に番地が起番されている町域の表示。1:該当、0:該当せず"""
    koaza_banchi = messages.IntegerField(11, required=True)

    u"""丁目を有する町域の場合の表示。1:該当、0:該当せず"""
    tyoume = messages.IntegerField(12, required=True)

    u"""一つの郵便番号で二以上の町域を表す場合の表示。1:該当、0:該当せず"""
    has_some_town = messages.IntegerField(13, required=True)

    u"""更新の表示。0:変更なし、1:変更あり、2:廃止(廃止データのみ使用)"""
    update_state = messages.IntegerField(14, required=True)

    u"""変更理由。0:変更なし、1:市政・区政・町政・分区・政令指定都市施行、2:住居表示の実施、3:区画整理、4:郵便区調整等、5:訂正、6:廃止(廃止データのみ使用)"""
    update_reason = messages.IntegerField(15, required=True)


class ZipCodeListResponse(messages.Message):
    items = messages.MessageField(ZipCodeResponseMessage, 1, repeated=True)


# class ZipCodeListRequest(messages.Message):
#     u"""ProtoRPC message definition to represent a ZIP code query."""
#
#     limit = messages.IntegerField(1, default=100)
#
#     code = messages.StringField(2)
