# -*- coding: utf-8 -*-
"""Colaboratory'ye Hoş Geldiniz adlı not defterinin kopyası adlı not defterinin kopyası

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oUTa84AJHvz61sK4HxOHUimUo5Yt8h7R
"""

class Ogrenci:
    def __init__(self, ogrenci_adi, ogrenci_soyadi, no, cinsiyeti, sinifi, notlari):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.no = no
        self.cinsiyeti = cinsiyeti
        self.sinifi = sinifi
        self.notlari = notlari

        bilgi =  {"ogrenci_adi": self.ogrenci_adi,
                "ogrenci_soyadi": self.ogrenci_soyadi,
                "no": self.no,
                "cinsiyeti": self.cinsiyeti,
                "sinifi": self.sinifi,
                "notlari": self.notlari}

    def not_ortalamasi(self):
        ortalama = sum(self.notlari.values())/len(self.notlari)
        return ortalama

ogrenci1 = Ogrenci("Sedef","Gökduman",100,"Kadın",3,{"Matematik":60,"Türkçe":90,"Fen" : 59})

ogrenci1.not_ortalamasi()

