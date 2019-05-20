#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .anythingnovel import AnythingNovelCrawler
from .babelchain import BabelchainCrawler
from .bestlightnovel import BestLightNovel
from .boxnovel import BoxNovelCrawler
from .chinesefantasy import ChineseFantasyNovels
from .comrademao import ComrademaoCrawler
from .creativenovels import CreativeNovelsCrawler
from .crescentmoon import CrescentMoonCrawler
from .fourscanlation import FourScanlationCrawler
from .fullnovellive import FullnovelLiveCrawler
from .gravitytales import GravityTalesCrawler
from .idqidian import IdqidianCrawler
from .litnet import LitnetCrawler
from .lnmtl import LNMTLCrawler
from .machinetrans import MachineNovelTrans
from .meionovel import MeionovelCrawler
from .mtlednovels import MtledNovelsCrawler
from .myoniyonitrans import MyOniyOniTranslation
from .novelall import NovelAllCrawler
from .novelfull import NovelFullCrawler
from .novelplanet import NovelPlanetCrawler
from .novelspread import NovelSpreadCrawler
from .noveluniverse import NovelUniverseCrawler
from .novelv import NovelvCrawler
from .readln import ReadLightNovelCrawler
from .readnovelfull import ReadNovelFullCrawler
from .romanticlb import RomanticLBCrawler
from .royalroad import RoyalRoadCrawler
from .scribblehub import ScribbleHubCrawler
from .tapread import TapreadCrawler
from .volarenovels import VolareNovelsCrawler
from .webnonline import WebnovelOnlineCrawler
from .webnovel import WebnovelCrawler
from .worldnovelonline import WorldnovelonlineCrawler
from .wuxiaco import WuxiaCoCrawler
from .wuxiacom import WuxiaComCrawler
from .wuxiaonline import WuxiaOnlineCrawler
from .yukinovel import YukiNovelCrawler
from .zenithnovels import ZenithNovelsCrawler
from .indomtl import IndoMTLCrawler

crawler_list = {
    # Do not forget to append a slash(/) at the end of the url
    # 'http://fullnovel.live/': FullnovelLiveCrawler,
    # 'https://www.noveluniverse.com/': NovelUniverseCrawler,
    # 'https://www.novelv.com/': NovelvCrawler,
    # 'https://m.chinesefantasynovels.com/': ChineseFantasyNovels,
    'https://indomtl.com/': IndoMTLCrawler,
    'http://gravitytales.com/': GravityTalesCrawler,
    'http://novelfull.com/': NovelFullCrawler,
    'http://www.machinenoveltranslation.com/': MachineNovelTrans,
    'http://zenithnovels.com/': ZenithNovelsCrawler,
    'https://4scanlation.xyz/': FourScanlationCrawler,
    'https://anythingnovel.com/': AnythingNovelCrawler,
    'https://bestlightnovel.com/': BestLightNovel,
    'https://boxnovel.com/': BoxNovelCrawler,
    'https://comrademao.com/': ComrademaoCrawler,
    'https://creativenovels.com/': CreativeNovelsCrawler,
    'https://crescentmoon.blog/': CrescentMoonCrawler,
    'https://litnet.com/': LitnetCrawler,
    'https://lnmtl.com/': LNMTLCrawler,
    'https://m.novelspread.com/': NovelSpreadCrawler,
    'https://m.romanticlovebooks.com/': RomanticLBCrawler,
    'https://m.wuxiaworld.co/': WuxiaCoCrawler,
    'https://meionovel.com/': MeionovelCrawler,
    'https://mtled-novels.com/': MtledNovelsCrawler,
    'https://myoniyonitranslations.com/': MyOniyOniTranslation,
    'https://novel.babelchain.org/': BabelchainCrawler,
    'https://novelplanet.com/': NovelPlanetCrawler,
    'https://readnovelfull.com/': ReadNovelFullCrawler,
    'https://webnovel.online/': WebnovelOnlineCrawler,
    'https://wuxiaworld.online/': WuxiaOnlineCrawler,
    'https://www.idqidian.us/': IdqidianCrawler,
    'https://www.novelall.com/': NovelAllCrawler,
    'https://www.novelspread.com/': NovelSpreadCrawler,
    'https://www.readlightnovel.org/': ReadLightNovelCrawler,
    'https://www.romanticlovebooks.com/': RomanticLBCrawler,
    'https://www.royalroad.com/': RoyalRoadCrawler,
    'https://www.scribblehub.com/': ScribbleHubCrawler,
    'https://www.tapread.com/': TapreadCrawler,
    'https://www.volarenovels.com/': VolareNovelsCrawler,
    'https://www.webnovel.com/': WebnovelCrawler,
    'https://www.worldnovel.online/': WorldnovelonlineCrawler,
    'https://www.wuxiaworld.co/': WuxiaCoCrawler,
    'https://www.wuxiaworld.com/': WuxiaComCrawler,
    'https://yukinovel.me/': YukiNovelCrawler,
    # Do not forget to append a slash(/) at the end of the url
}
