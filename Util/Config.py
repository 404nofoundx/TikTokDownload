#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:Config.py
@Date       :2022/07/29 23:18:47
@Author     :JohnserfSeed
@version    :1.0
@License    :MIT License
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
2022/07/29 23:18:47 : Init
2022/08/16 18:34:27 : Add log moudle
2023/03/08 14:42:05 : Add cookie,interval,update; conf
-------------------------------------------------
'''

import Util

class Config:

    def __init__(self):
        self.default = {
            'uid': 'https://v.douyin.com/k9NXNcH/',
            'music': 'no',
            'cover': 'no',
            'desc': 'no',
            'path': 'Download',
            'folderize': 'yes',
            'mode': 'post',
            'naming': '{create}_{desc}',
            'cookie':'请扫码登录，cookie会自动保存',
            'interval':'all',
            'update':'yes',
            'limit': 'all',
            'max_connections': 10,
            'max_tasks': 10
        }

    def check(self):
        """
        检查配置文件，不存在就生成默认配置文件
        Returns:
            self.cf: 配置文件对象
        """

        if Util.os.path.isfile("conf.ini") == True:
            # 用utf-8防止出错
            self.cf = Util.ConfigObj('conf.ini', encoding='utf-8')
        else:
            Util.progress.console.print('[  提示  ]:没有检测到配置文件，生成中!\r')
            Util.log.info('[  提示  ]:没有检测到配置文件，生成中!')
            try:
                # 实例化读取配置文件
                self.cf = Util.ConfigObj('conf.ini', encoding='utf-8')
                # 往配置文件写入内容
                self.cf['uid'] = 'https://v.douyin.com/JcjJ5Tq/'
                # 添加注释
                self.cf.comments['uid'] = ['用户主页(非视频链接)',
                                            '单视频请用TikTokDownload或TikTokWeb']
                self.cf['music'] = 'yes'
                self.cf.comments['music'] = ['',
                                            '视频原声保存(yes|no)']
                self.cf['cover'] = 'no'
                self.cf.comments['cover'] = ['',
                                            '视频封面保存(yes|no)']
                self.cf['desc'] = 'no'
                self.cf.comments['desc'] = ['',
                                            '视频文案保存(yes|no)']
                self.cf['path'] = 'Download'
                self.cf.comments['path'] = ['',
                                            '作品保存位置，只支持相对路径',
                                            '不了解不用修改']
                self.cf['folderize'] = 'yes'
                self.cf.comments['folderize'] = ['',
                                            '作品保存到单独的文件夹(yes|no)',
                                            '如果设置了保存原声、封面、文案的建议开启该选项']
                self.cf['mode'] = 'post'
                self.cf.comments['mode'] = ['',
                                            '下载模式(post|like|listcollection|wix合集暂未更新)',
                                            '下载他人喜欢页、收藏视频请确保是开放所有人可见',
                                            '如果是扫码登陆的下载自己的喜欢与收藏则无需设置所有人可见']
                self.cf['naming'] = '{create}_{desc}'
                self.cf.comments['naming'] = ['',
                                            '全局作品文件命名',
                                            '{create}发布时间、{desc}作品文案、{id}作品id',
                                            '只允许下划线_ 减号- 作为文件名间隔符',
                                            '该配置会影响folderize中的作品文件夹命名']
                self.cf['cookie'] = ''
                self.cf.comments['cookie'] = ['',
                                            '置空该选项本程序会自动打开二维码获取cookie',
                                            '本程序不会共享、存储、处理、加密、上传你的cookie配置',
                                            '请妥善保管你个人的cookie信息，发issues贴log文件的时候注意脱敏，防止泄露！']
                self.cf['interval'] = 'all'
                self.cf.comments['interval'] = ['',
                                            '根据作品发布日期区间下载作品',
                                            '例如2022-01-01|2023-01-01下载的是2022年所有作品',
                                            '填all即是下载全部时间']
                self.cf['update'] = 'yes'
                self.cf.comments['update'] = ['',
                                            '自动更新(yes|no)',
                                            '由于更新频率快，默认yes可以保持最新版本',
                                            '关闭后仅提示有新版可下载']
                self.cf['max_connections'] = 10
                self.cf.comments['max_connections'] = ['',
                                            '网络请求并发连接数',
                                            '不宜设置过大，如遇错误可适当降低']
                self.cf['max_tasks'] = 10
                self.cf.comments['max_tasks'] = ['',
                                            '异步的任务数',
                                            '不宜设置过大，如遇错误可适当降低']

                # 写入到文件
                self.cf.filename = 'conf.ini'
                self.cf.write()
                Util.progress.console.print('[  配置  ]:配置文件生成成功!\r')
                Util.log.info('[  配置  ]:配置文件生成成功!')

            except Exception as writeiniError:
                Util.progress.console.print('[  配置  ]:配置文件写入失败!\r')
                Util.log.error('[  配置  ]:配置文件写入失败! %s' % writeiniError)
                self.download()

        return self.cf
            # 是否自动升级
            Util.Updata(self.cf['update'])

    def download(self) -> None:
        """
        下载配置文件
        """
        try:
            Util.progress.console.print('[  提示  ]:从GitHub为您下载配置文件!\r')
            Util.log.info('[  提示  ]:从GitHub为您下载配置文件!')
            r = Util.requests.get(
                'https://cdn.jsdelivr.net/gh/Johnserf-Seed/TikTokDownload@main/conf.ini')
            with open("conf.ini", "w") as f:
                f.write(r.content)
            Util.progress.console.print('[  提示  ]:下载配置成功!\r')
            Util.log.info('[  提示  ]:下载配置成功!')
        except Exception as iniError:
            Util.progress.console.print('[  提示  ]:下载失败，请检查网络!\r')
            Util.log.info('[  提示  ]:下载失败，请检查网络!')
            Util.log.error(iniError)

    def save(self, cookie) -> None:
        if Util.os.path.isfile("conf.ini") == True:
            # 用utf-8防止出错
            self.cf = Util.ConfigObj('conf.ini', encoding='utf-8')
            self.cf['cookie'] = cookie
            # 写入到文件
            self.cf.filename = 'conf.ini'
            self.cf.write()
            Util.progress.console.print('[  配置  ]:cookie更新成功!\r')
            Util.log.info('[  配置  ]:cookie更新成功!')
            Util.log.info(cookie)
        else:
            self.check()

        return self.cf
